"""
Створіть асинхронну програму,
яка одночасно запускає 3 таймери з інтервалами 2, 3 та 5 секунд.
Кожен раз, коли таймер спрацьовує,
виводьте повідомлення з відповідним інтервалом.
"""

import asyncio


async def timer(interval):

    while True:
        await asyncio.sleep(interval)
        print(f'Timer complete {interval}')


async def main():
    timers = [2, 3, 5]

    tasks = []
    for i in timers:
        tasks.append(asyncio.create_task(timer(i)))

    results = await asyncio.gather(*tasks)
    for i in results:
        print(i)


asyncio.run(main())
