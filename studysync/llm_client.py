import random
import time

def call_llm(prompt: str):
    if random.random() < 0.5:
        time.sleep(2)  
        raise Exception("LLM Service Failed / Timeout")

    return f"LLM RESPONSE: {prompt}"