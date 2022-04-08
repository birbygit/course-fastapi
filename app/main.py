from fastapi import FastAPI
from .import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#Since we introduced Alembic, we comment out below instruction
# models.Base.metadata.create_all(bind=engine)

app = FastAPI() #instance of FastAPI

#CORS handling
origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# order of API's matters

#include routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#FastAPI Path Operation == Route
@app.get("/") # decorator '@' + app reference + http method-> transform function in API 
def root():  #function plain python  -- name doesn't matter
    return {"message": "Welcome to my APIv3"} # py dictionary -> JSON

