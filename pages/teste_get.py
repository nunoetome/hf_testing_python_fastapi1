#import streamlit as st
from typing import Union
from fastapi import FastAPI

#st.title("pages/teste_get.py")
APP = FastAPI()

@APP.get("/")
async def readv_root():
    return {"Hello": "World"}