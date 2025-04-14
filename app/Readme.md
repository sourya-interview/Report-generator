# Report Generator Microservice

A FastAPI-based microservice that:

- Accepts large CSV uploads (up to 1GB)
- Applies transformation rules from a config file
- Generates output reports by merging with reference data
- Secured with API key authentication

---

## Features

- Upload `input.csv` and `reference.csv`
- Configurable transformation rules via `config.json`
- Generate reports with merged and transformed fields
- Download final `output.csv`
- Secured endpoints using API Key (`x-api-key`)
- Automatically documented via Swagger UI
- Unit tested with pytest (5 tests included)
- Logging for observability

---

## API Overview

> All requests require a header: 
> `x-api-key: supersecret123`

### `POST /upload/`

Upload `input.csv` and `reference.csv` files.

- **Form-data**:
  - `input_file`: CSV file
  - `reference_file`: CSV file

### `GET /generate-report/`

Generates a report based on uploaded files and rules defined in `config.json`.

### `GET /download-report/`

Downloads the generated report as `output.csv`.

---

## Sample Transformation Rules (`config.json`)

```json
{
  "outfield1": "field1 + field2",
  "outfield2": "refdata1",
  "outfield3": "refdata2 + refdata3",
  "outfield4": "field3 * max(field5, refdata4)",
  "outfield5": "max(field5, refdata4)"
}

---

Sample Input Files

input.csv

field1,field2,field3,field4,field5,refkey1,refkey2
Hello,World,2,0,10,A,X
Good,Morning,3,0,5,B,Y
Nice,Day,4,0,8,C,Z

reference.csv

refkey1,refdata1,refkey2,refdata2,refdata3,refdata4
A,RefA,X,R2A,R3A,15
B,RefB,Y,R2B,R3B,12
C,RefC,Z,R2C,R3C,9

---

Getting Started

1. Install dependencies

pip install -r requirements.txt

2. Run the application

uvicorn app.main:app --reload

3. Access Swagger UI

http://127.0.0.1:8000/docs

Click Authorize and enter:

x-api-key: supersecret123

---

Run Tests

pytest

Test suite covers:

File upload

Report generation

Download

Unauthorized access

Invalid API key


---

Project Structure

report-generator/
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── server.py
│   ├── config.json
│   ├── routes/
│   │   └── api.py
│   └── sample_input/
│       ├── input.csv
│       └── reference.csv
├── output/
│   └── output.csv
├── tests/
│   └── test_main.py
├── requirements.txt
├── Dockerfile
└── README.md

---

Author

Developed as part of a backend internship assignment. Built with FastAPI, Pandas, and Python.