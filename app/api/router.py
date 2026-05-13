from typing import Any

from fastapi import APIRouter, HTTPException,status
from fastapi.responses import RedirectResponse
from sqlmodel import select

from app.database.model import URL
from app.database.session import SessionDep
from app.main import generate_code
from app.schemas import Url


router = APIRouter()



@router.post("/url-shorten")
def short_link(url: Url,session:SessionDep) ->dict[str,Any] :
   url_str=str(url.url)
   url_shortener=URL(url=url_str,
    short_code= generate_code()
      
   )
   session.add(url_shortener)
   session.commit()
   session.refresh(url_shortener)
   return {"shortened_url": f"http://localhost:8000/{url_shortener.short_code}"}



@router.get("/{short_code}")
def redirect_to_url(short_code:str,session:SessionDep):
    statement= select(URL) .where(URL.short_code== short_code)
    result=session.exec(statement).first()

    if result is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    return RedirectResponse(status_code=302, url=str(result.url))
