import asyncio
import time

async def task():
    await asyncio.sleep(3)
    print("task1: 끝")

async def task2():
    print("task2: 시작")
    await asyncio.sleep(1)
    print("task2: 끝")


async def main():
    await asyncio.gather(task(), task2())


asyncio.run(main())


