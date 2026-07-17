from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Welcome!"}

@app.get("/about")
def about():
    return {"message": "This is a beginner FastAPI project."}