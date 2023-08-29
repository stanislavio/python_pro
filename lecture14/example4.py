import asyncio


async def background_task():
    while True:
        print("Фонове завдання виконується...")
        await asyncio.sleep(3)


async def main():
    asyncio.create_task(background_task())

    while True:
        print("Основна програма виконується...")
        await asyncio.sleep(1)


asyncio.run(main())
