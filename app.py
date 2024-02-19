from typing import Union
from fastapi import FastAPI
import streamlit as st
from transformers import pipeline

MODELS = [
            "google/vit-base-patch16-224", #Classifição geral
            "nateraw/vit-age-classifier" #Classifição de idade
            
]

app = FastAPI()


def main():
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}


    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    main()