from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from secrets import token_urlsafe
from typing import Any

app = FastAPI()
database = {}

def generate_code():
    return token_urlsafe(6)

@app.post("/url-shorten")
def short_link(url: str) -> dict[str, Any]:
    for code, link in database.items():
        if link == url:
            return {"shortened": code}
    code = generate_code()
    database[code] = url
    return {"shortened": code}

@app.get("/{short_code}")
def redirect_to_url(short_code: str):
    if short_code not in database:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(status_code=302, url=database[short_code])