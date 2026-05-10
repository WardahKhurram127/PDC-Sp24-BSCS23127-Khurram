from fastapi import FastAPI
from circuit_breaker import CircuitBreaker
from llm_client import call_llm
from middleware import StudentIDMiddleware

app = FastAPI()

app.add_middleware(StudentIDMiddleware)

cb = CircuitBreaker(threshold=3, reset_timeout=10)

# #System Failing
# @app.get("/generate")
# def generate(prompt: str):

#     try:
#         result = call_llm(prompt)

#         return {
#             "status": "success",
#             "response": result
#         }

#     except Exception as e:

#         return {
#             "status": "error",
#             "response": "LLM failed",
#             "error": str(e)
#         }

#System succeeding
@app.get("/generate")
def generate(prompt: str):

    # Step 1: check circuit breaker state
    if not cb.allow_request():
        return {
            "status": "fallback",
            "response": "Circuit OPEN: Returning cached/fallback response"
        }

    # Step 2: try calling external LLM
    try:
        result = call_llm(prompt)
        cb.record_success()

        return {
            "status": "success",
            "response": result
        }

    except Exception as e:
        cb.record_failure()

        return {
            "status": "error",
            "response": "Fallback response due to LLM failure",
            "error": str(e)
        }





    