import asyncio
from random import randint


async def async_function(number, sleep_count):
    await asyncio.sleep(sleep_count)
    return f"Result of function {number}"


async def main():
    tasks = []

    for i in range(1, 6):
        task = asyncio.create_task(async_function(i, randint(1, 5)))
        tasks.append(task)
    print('Before await')
    results = await asyncio.gather(*tasks)
    print("Results:")
    for i, result in enumerate(results, start=1):
        print(f"Function {i}: {result}")

asyncio.run(main())
