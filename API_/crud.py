from sqlalchemy.orm import Session
from  models import Employee

#Insert 
def create_employee (db: Session, employee):
    new_employee = Employee(
        name = employee.name,
        age = employee.age,
        city = employee.city
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

#Read All
def get_employees(db: Session):
    return db.query(Employee).all()

#Read One
def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()

#Update
def update_employee(db: Session, emp_id: int, employee):
    db_employee = db.query(Employee).filter(Employee.id == emp_id).first()

    if db_employee:
        db_employee.name = employee.name
        db_employee.age = employee.age
        db_employee.city = employee.city

        db.commit()
        db.refresh(db_employee)

    return db_employee

#Delete
def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(Employee).filter(Employee.id == emp_id).first()

    if db_employee:
        db.delete(db_employee)
        db.commit()
    
    return db_employee
