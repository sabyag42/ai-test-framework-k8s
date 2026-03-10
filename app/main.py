from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from ai_generator import AITestGenerator
import uvicorn

app = FastAPI(
    title="AI Test Framework API",
    description="Claude-powered test case generator deployed on Kubernetes",
    version="1.0.0"
)

generator = AITestGenerator()

class GenerateRequest(BaseModel):
    endpoint: str
    method: str = "GET"
    description: str
    num_cases: Optional[int] = 5

class TestCase(BaseModel):
    name: str
    description: str
    input_data: dict
    expected_status: int
    expected_response: dict

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "test-api",
        "kubernetes": True,
        "ai_powered": True
    }

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Test Framework API!",
        "powered_by": "GPT-4o by OpenAI",
        "deployed_on": "Kubernetes"
    }

@app.post("/generate-tests")
def generate_tests(req: GenerateRequest):
    """Use Claude AI to generate test cases for any API endpoint"""
    try:
        cases = generator.generate(
            req.endpoint,
            req.method,
            req.description,
            req.num_cases
        )
        return {
            "endpoint": req.endpoint,
            "method": req.method,
            "test_cases": cases,
            "generated_by": "Claude AI",
            "count": len(cases)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
