# Report Generator Microservice

This is a Python-based backend microservice built using FastAPI. It allows uploading large input and reference CSV files, processes them based on transformation rules, and generates an output report which can be downloaded via API. The system includes authentication, Swagger UI for API testing, and a structured file organization.

---

## Installation & Setup (Step-by-step)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/report-generator.git
   cd report-generator```

2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
uvicorn main:app --reload
```
5. Open the API Docs Visit: http://localhost:8000/docs



---

Tech Stack Used

Language: Python 3.x

Framework: FastAPI

Data Processing: pandas

API Testing: Swagger UI (via FastAPI)

Security: API Key via header (x-api-key)

Testing: pytest (basic tests included)

Other Tools: Uvicorn (ASGI server), JSON config for rule flexibility


---

Features Implemented

[x] Upload input.csv and reference.csv via /upload/

[x] Generate report via /generate-report/ using transformation rules

[x] Download final output.csv via /download-report/

[x] Configurable rules via app/config.json

[x] API key authentication using x-api-key header

[x] Auto-generated API documentation (/docs)

[x] Sample input and output files included

[x] Clean and modular folder structure


---

API Authentication

Every request must include this header:

x-api-key: supersecret123

---

Project Structure

report-generator/
├── app/
│   ├── __init__.py
│   ├── auth.py              # API key verification
│   ├── config.json          # Transformation rules
│   ├── main.py              # FastAPI entry point
│   ├── server.py
|   ├── utils.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── api.py           # API endpoints
│   └── sample_input/
│       ├── input.csv        # Sample input
│       └── reference.csv    # Sample reference
├── output/
│   └── output.csv           # Generated report
├── tests/
│   └── test_main.py         # Unit tests (basic)                       
├── .gitignore
|── README.md
├── requirements.txt         # Dependencies    

---

What's Not Yet Done (As per given assessment)

The following features were expected but are not implemented due to time constraints:

Dynamic rule configuration via GET/POST /rules/ endpoints

Scheduled report generation using cron expressions

Support for .xlsx and .json formats

Monitoring and observability (Prometheus)

Structured logging with rotation

Full pytest coverage with edge cases

Optimized performance for 1GB+ files using chunk processing


---

Future Enhancements

Dynamic Rule Configuration:
Add API endpoints to get/update transformation rules via HTTP instead of manual file edit.

Scheduling:
Use APScheduler or Celery to schedule report generation at configurable intervals.

File Format Flexibility:
Support uploading and parsing .xlsx and .json formats alongside CSV.

Monitoring & Observability:
Integrate Prometheus metrics for request/processing stats and performance tracking.

Logging:
Add log rotation and structured JSON logs using loguru.

Performance Optimization:
Use pandas.read_csv(chunksize=...) to process very large files efficiently.

Comprehensive Testing:
Expand pytest coverage with upload, edge cases, and failure scenarios.


---

Final Notes

While the core requirements of the assignment have been implemented and tested, some advanced features are scoped for future improvements. The project is structured for easy extension, and I’m confident in building on this foundation with the right guidance.
