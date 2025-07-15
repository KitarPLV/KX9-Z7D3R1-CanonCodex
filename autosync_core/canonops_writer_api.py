from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/api/write")
async def write(request: Request):
    try:
        data = await request.json()
        return JSONResponse(content={"status": "received", "data": data}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
