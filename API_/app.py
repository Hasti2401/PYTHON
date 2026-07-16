from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

from security import create_access_token,verify_token

app = FastAPI()

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#user for learning
user = {
    "username" : "admin",
    "password" : "1234"
}


#Home
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI JWT Authentication"}


#Login API
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    if(
        form_data.username != user["username"] or
        form_data.password != user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Username or Password"
        )
    
    access_token = create_access_token(
        data={"sub": form_data.username}
    )

    return{
        "access_token": access_token,
        "token_type": "bearer"
    }


#Get ALL Employees
@app.get("/employees")
def read_all(
    current_user: str = Depends(verify_token),
    db: Session = Depends(get_db)
    ):

    return crud.get_employees(db)


#Create Employee
@app.post("/employees")
def create(employee: schemas.EmployeeCreate,
           current_user: str = Depends(verify_token),
           db: Session = Depends(get_db)):
    
    return crud.create_employee(db, employee)


#Get Employee By ID 
@app.get("/employees/{emp_id}")
def read_one(emp_id: int,
             current_user: str = Depends(verify_token),
             db: Session = Depends(get_db)):
    

    employee = crud.get_employee(db, emp_id)

    if employee is None:
        raise HTTPException(status_code=404,
                            detail="Employee not found")
    
    return employee


#Update Employee
@app.put("/employees/{emp_id}")
def update(emp_id: int,
           employee: schemas.EmployeeCreate,
           current_user: str = Depends(verify_token),
           db: Session = Depends(get_db)):
    
    updated = crud.update_employee(db, emp_id, employee)

    if updated is None:
        raise HTTPException(status_code=404,
                            detail="Employee not found")
    
    return updated


#Delete Employee
@app.delete("/employees/{emp_id}")
def delete(emp_id: int,
           current_user: str = Depends(verify_token),
           db: Session = Depends(get_db)):
    
    deleted = crud.delete_employee(db, emp_id)

    if deleted is None:
        raise HTTPException(status_code=404,
                            detail="Employee not found")
    
    return {"message" : "Employee deleted Successfully"}