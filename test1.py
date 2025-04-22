# main.py
from fastapi import FastAPI
import asyncio
import time

app = FastAPI()


@app.get("/download")
async def run_download():
    await asyncio.sleep(10)
    return {"status": "File downloaded completed"}


@app.get("/status")
async def quick_status():
    return {"status": "Server is running"}