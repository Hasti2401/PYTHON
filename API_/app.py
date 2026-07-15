from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

app = FastAPI()

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "FastAPI Connected to Existing MYSQL Database"}

#Create Employee
@app.post("/employees")
def create(employee: schemas.EmployeeCreate,
           db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)


#Get ALL Employees
@app.get("/employees")
def read_all(db: Session = Depends(get_db)):
    return crud.get_employees(db)


#Get Employee By ID 
@app.get("/employees/{emp_id}")
def read_one(emp_id: int,
             db: Session = Depends(get_db)):
    
    employee = crud.get_employee(db, emp_id)

    if employee is None:
        raise HTTPException(status_code=404,
                            detail="Employee not found")
    
    return employee


#Update Employee
@app.put("/employee/{emp_id}")
def update(emp_id: int,
           employee: schemas.EmployeeCreate,
           db: Session = Depends(get_db)):
    
    updated = crud.update_employee(db, emp_id, employee)

    if updated is None:
        raise HTTPException(status_code=404,
                            detail="Employee not found")
    
    return updated


#Delete Employee
@app.delete("/employees/{emp_id}")
def delete(emp_id: int,
           db: Session = Depends(get_db)):
    
    deleted = crud.delete_employee(db, emp_id)

    if deleted is None:
        raise HTTPException(status_code=404,
                            detail="Employee not found")
    
    return {"message" : "Employee deleted Successfully"}