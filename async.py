import time
from data import data
import tracemalloc
import csv
import asyncio
import itertools
import aiofiles


def header():
    with open('data.csv', 'w', encoding='UTF8', newline='') as file:
        header = ['name', 'login', 'password', 'address']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()


async def single_function(row):
    header = ['name', 'login', 'password', 'address']
    async with aiofiles.open('data.csv', 'a', encoding='UTF8',
                             newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        await writer.writerow(row)


header()

tracemalloc.start()
start = time.time()

loop = asyncio.get_event_loop()
tasks = itertools.starmap(single_function, data)
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
