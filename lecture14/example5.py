
import asyncio


async def async_function(progress_callback):
    for i in range(1, 6):
        await asyncio.sleep(1)
        progress_callback(i * 20)
    return "Done!"


async def main():
    def progress_callback(progress):
        print(f"Progress: {progress}%")

    task = asyncio.create_task(async_function(progress_callback))

    while not task.done():
        await asyncio.sleep(0.5)

    print(await task)


asyncio.run(main())
