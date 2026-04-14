from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@app.get("/kata_kata_gmail_com")
def lcm(x: str, y: str):
    try:
        x = int(x)
        y = int(y)

        if x < 0 or y < 0:
            return PlainTextResponse("NaN")

        if x == 0 or y == 0:
            return PlainTextResponse("0")

        result = abs(x * y) // gcd(x, y)
        return PlainTextResponse(str(result))
    except:
        return PlainTextResponse("NaN")