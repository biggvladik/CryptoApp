from fastapi import APIRouter,WebSocket,WebSocketDisconnect,Body,Depends
from .database import *
from .models import *
from fastapi.encoders import jsonable_encoder
import json




router = APIRouter()
@router.get("/test", response_description= "test router")
async def test():
   return 'hello world!'