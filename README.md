# 💸 Payment Retry API Simulator

A backend microservice that simulates a payment initiation and retry mechanism, built using Python Flask.

## 🔧 Features

- REST API: Initiate and check payment status
- Retry logic for failed payments (up to 3 times)
- In-memory storage for simplicity
- Functional mindset: retry loop is stateless, idempotent requests

## 📦 Tech Stack

- Python 3.10+
- Flask
- Threading
- UUID

## 🚀 API Endpoints

### POST /pay
Initiates a mock payment.

**Request**:
```
{
  "user": "vaibhavee"
}
```
Response:

```
{
  "payment_id": "uuid...",
  "status": "SUCCESS | FAILED"
}
```

### GET /status/<payment_id>
Check status and retry logs.

**Response:**:
```
{
  "payment_id": "...",
  "user": "vaibhavee",
  "status": "SUCCESS",
  "retries": 2,
  "logs": [...]
}
```




## 🧪 Run Locally

- git clone https://github.com/vaibhaveethorat11/payment-retry-api.git
- cd payment-retry-api
- pip install flask
- python app.py
- Server will run at http://127.0.0.1:5000
