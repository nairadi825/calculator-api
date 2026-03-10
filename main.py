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
    
import math
@app.get("/hypotenuse/{a}/{b}", status_code=200)
def hypotenuse(a: float, b: float):
    """
    Calculate the hypotenuse 
    Both a and b must be positive numbers.
    """
    if a <= 0 or b <= 0:
        return {"error": "Both a and b must be a positive number"}
    return {"result": math.sqrt(a*a + b*b)}

@app.get("/fahrenheit_to_celsius/{a}", status_code=200)
def fahrenheit_to_celsius(a: float):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Parameters:
    - a: Temperature in Fahrenheit
    """
    return {"result": (a - 32) * 5/9}

@app.get("/minimum/{a}/{b}/{c}", status_code=200)
def minimum(a: float, b: float, c: float):
    """
    Return the minimum of three values.
    """
    
    values = [a, b, c]

    return {"result": min(values)}
