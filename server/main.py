from fastapi import FastAPI
from app_parse.routers import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()




app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    pass

@app.on_event("shutdown")
async def shutdown_event():
    pass







