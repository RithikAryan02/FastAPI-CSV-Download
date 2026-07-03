from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

@app.get("/download")
def download_csv():
    file_path = "employees.csv"

    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            filename="employees.csv",
            media_type="text/csv"
        )

    return {"message": "CSV file not found"}
