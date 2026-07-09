# FastAPI CSV Management API 

## Overview

The FastAPI CSV Management API is a backend application built using FastAPI that allows users to upload, read, process, and manage CSV files efficiently through REST APIs.

This project demonstrates API development, file handling, and data processing using Python and FastAPI.

## Features

* Upload CSV files through API endpoints.
* Read and process CSV data.
* Retrieve CSV records using API requests.
* Convert CSV data into JSON format.
* Fast and lightweight API performance.
* Interactive API documentation using Swagger UI.

## Technologies Used

* **Python**
* **FastAPI**
* **Pandas**
* **Uvicorn**
* **CSV Module**

## Project Structure

```text
fastapi-csv/
│
├── app.py
├── requirements.txt
├── data/
│   └── sample.csv
├── uploads/
├── README.md
└── .gitignore
```

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/fastapi-csv.git
```

### Move to project directory

```bash
cd fastapi-csv
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server using:

```bash
uvicorn app:app --reload
```

The application will run on:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

* Swagger UI:

  ```text
  http://127.0.0.1:8000/docs
  ```

* ReDoc:

  ```text
  http://127.0.0.1:8000/redoc
  ```

## Example Workflow

1. Start the FastAPI server.
2. Upload a CSV file using the upload endpoint.
3. The API processes the CSV data.
4. Retrieve the processed data in JSON format using API endpoints.

## Sample API Endpoints

| Method | Endpoint     | Description                |
| ------ | ------------ | -------------------------- |
| POST   | `/upload`    | Upload a CSV file          |
| GET    | `/data`      | Retrieve all CSV records   |
| GET    | `/data/{id}` | Retrieve a specific record |

## Future Enhancements

* CSV validation before processing.
* Database integration with PostgreSQL or MySQL.
* Authentication and authorization.
* Data filtering and pagination.
* Export data to Excel or JSON formats.

## Author
Ritik Aryan

## License

This project is developed for educational and learning purposes.
