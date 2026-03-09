from fastapi import FastAPI, status

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: float, b: float):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    return {"result": a + b}

@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: float, b: float):
    """
    Subtract one number from another.

    Parameters:
    - a: First number
    - b: Second number

    Returns:
    - JSON object with the result
    """
    return {"result": a - b}

@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: float, b: float):
    """
    Multiply two numbers together.

    Parameters:
    - a: First number
    - b: Second number

    Returns:
    - JSON object with the result
    """
    return {"result": a * b}

@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: float, b: float):
    """
    Divide one number by another.

    Parameters:
    - a: Numerator
    - b: Denominator

    Returns:
    - JSON object with the result
    """
    if b == 0:
        return {"error": "Divide by zero error. Please enter a non-zero error for the second number"}
    return {"result": a / b}
