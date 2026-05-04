from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union, Literal
import uvicorn

app = FastAPI(title="Calculator Sidecar API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculatorRequest(BaseModel):
    operation: Literal["add", "sub", "mul", "div"]
    num1: float
    num2: float

class CalculatorResponse(BaseModel):
    result: float
    error: Union[str, None] = None

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@app.post("/calculate", response_model=CalculatorResponse)
async def calculate(request: CalculatorRequest):
    try:
        if request.operation == "add":
            result = add(request.num1, request.num2)
        elif request.operation == "sub":
            result = subtract(request.num1, request.num2)
        elif request.operation == "mul":
            result = multiply(request.num1, request.num2)
        elif request.operation == "div":
            result = divide(request.num1, request.num2)
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")
        
        return CalculatorResponse(result=result)
    except ValueError as e:
        return CalculatorResponse(result=0, error=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
