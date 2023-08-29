import asyncio
from random import randint


async def async_function(number, sleep_count):
    print(f"Function {number} was run")
    await asyncio.sleep(sleep_count)
    print(f"Function {number} is done")


async def main():
    tasks = []

    for i in range(1, 6):
        task = asyncio.create_task(async_function(i, randint(1, 5)))
        tasks.append(task)

    await asyncio.gather(*tasks)

asyncio.run(main())
