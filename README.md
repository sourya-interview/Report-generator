# Report Generator Microservice

A FastAPI-based backend microservice that uploads large CSV files, merges them using transformation rules, and generates a report.

---

## How to Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt

2. Start the server:


uvicorn main:app --reload

3. Open docs in browser:


http://localhost:8000/docs

---

Authentication

All endpoints require an API key.

Include this header:

x-api-key: supersecret123

---

API Endpoints

---

Sample Input

Place your CSVs inside:

app/sample_input/input.csv
app/sample_input/reference.csv

Example columns:

input.csv: field1, field2, field3, field4, field5, refkey1, refkey2

reference.csv: refkey1, refdata1, refkey2, refdata2, refdata3, refdata4


---

Output

Generated report will be saved in: output/output.csv

Fields include: outfield1 to outfield5 as per transformation rules


---

Future Enhancements

GET /rules and POST /rules for dynamic rule management

Cron-based scheduled report generation

Support for .xlsx and .json input formats

Prometheus metrics and observability

Optimized large file handling (1GB+ chunks)

Better test coverage and logging