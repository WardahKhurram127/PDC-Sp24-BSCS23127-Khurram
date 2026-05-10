# Wardah Khurram - BSCS23127

# Fault-Tolerant Distributed System using Circuit Breaker Pattern

## Overview

This project demonstrates a resilient distributed system using:

- FastAPI
- Circuit Breaker Pattern
- Fallback Responses
- Simulated LLM Service Failures

The system shows how fault tolerance improves reliability when an external service becomes unstable or unavailable.

---

## Features

- Simulated unreliable LLM service
- Random timeout/failure generation
- Fallback response handling
- Circuit Breaker implementation
- Request testing script
- Fault-tolerant behavior demonstration

---

## Project Structure

```
studysync/
│
├── main.py            # FastAPI application
├── test_fail.py       # Script to test repeated requests
└── README.md
```

---

## Requirements

Install dependencies using:

```
python -m pip install fastapi uvicorn requests
```

---

## How to Run the Project

### Step 1: Open Terminal

Navigate to the project directory:

```
cd C:\studysync
```

---

### Step 2: Start the FastAPI Server

Run:

```
python -m uvicorn main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## How to Run the Tests

Open another terminal and navigate to the same folder:

```
cd C:\studysync
```

Run the test script:

```
python test_fail.py
```

---

## Expected Behavior

### Before Fault Tolerance

The system directly returns errors when the LLM service fails:

```
{
  "status": "error",
  "response": "LLM failed"
}
```

---

### After Fault Tolerance

The system returns fallback responses instead of completely failing:

```
{
  "status": "error",
  "response": "Fallback response due to LLM failure"
}
```

After repeated failures, the Circuit Breaker opens:

```
{
  "status": "fallback",
  "response": "Circuit OPEN: Returning cached/fallback response"
}
```

---

## Concepts Demonstrated

- Fault Tolerance
- Graceful Degradation
- Circuit Breaker Pattern
- Distributed System Resilience
- Failure Recovery

---

## Author

Wardah Khurram  
BSCS23127
```
