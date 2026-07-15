from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name : str
    age : int
    city : str

class EmployeeResponse(EmployeeCreate):
    id : int

    class Config: 
        from_attributes = True