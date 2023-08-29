import asyncio
import datetime
from random import randint

import aiohttp


async def fetch_data(url):
    sleep_count = randint(2, 5)
    print(f"Request to {url}, I will work about {sleep_count} s.")

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    start = datetime.datetime.now()
    urls = [
        "http://google.com",
    ]

    # Створюємо список асинхронних об'єктів для функції fetch_data
    tasks = [fetch_data(url) for url in urls]

    # Очікуємо завершення всіх асинхронних завдань
    results = await asyncio.gather(*tasks)

    print("Результати:")
    for result in results:
        print(result)

    print(f'Working time about {(datetime.datetime.now() - start).seconds}')

asyncio.run(main())
