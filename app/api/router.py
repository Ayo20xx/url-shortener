from datetime import timedelta, timezone
import datetime
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
async def short_link(url: Url,session:SessionDep)->dict[str,Any] :
   url_str=str(url.url)
   statement= select(URL).where(URL.url==url_str)
   result=(await session.exec(statement)).first()

   if result :
       return {"shortened_url": f"http://localhost:8000/{result.short_code}"}
    
   url_shortener=URL(url=url_str,
        short_code= generate_code()
    )
   await session.add(url_shortener)
   session.commit()
   await session.refresh(url_shortener)
   return {"shortened_url": f"http://localhost:8000/{url_shortener.short_code}"}



@router.get("/{short_code}")
async def redirect_to_url(short_code:str,session:SessionDep):
    statement= select(URL) .where(URL.short_code== short_code)
    result=session.exec(statement).first()

    if result is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    
    if datetime.now(timezone.utc) - result.created_at > timedelta(days=30):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, details=" expired code")
    
    result.click_count += 1
    await session.commit()
    

    return RedirectResponse(status_code=302, url=str(result.url))
