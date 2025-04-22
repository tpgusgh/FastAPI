from fastapi import FastAPI
import asyncio
import threading
import multiprocessing
import time

app = FastAPI()


def long_running_task(name="Task", delay=5):
    print(f"{name} 시작")
    time.sleep(delay)
    print(f"{name} 완료")
    return f"{name} 완료됨"


@app.get("/async-task")
async def async_task():
    await asyncio.sleep(5)
    return {"message": "Async 작업 완료"}


@app.get("/thread-task")
def thread_task():
    thread = threading.Thread(target=long_running_task, args=("Thread 작업",))
    thread.start()
    return {"message": "Thread 작업 시작됨 (백그라운드 실행 중)"}


@app.get("/process-task")
def process_task():
    process = multiprocessing.Process(target=long_running_task, args=("Process 작업",))
    process.start()
    return {"message": "Process 작업 시작됨 (백그라운드 실행 중)"}


@app.get("/quick")
def quick():
    return {"message": "빠른 응답입니다!"}