import time
from data import data
import tracemalloc
import csv
from faker import Faker
import threading

fake = Faker()


def header():
    with open('data.csv', 'w', encoding='UTF8', newline='') as file:
        header = ['name', 'login', 'password', 'address']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()


def single_function(row):
    header = ['name', 'login', 'password', 'address']
    with open('data.csv', 'a', encoding='UTF8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writerow(row)


header()
threads = []
tracemalloc.start()
start = time.time()
for item in data:
    thread = threading.Thread(target=single_function, args=(item, ))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
print("All done! {}".format(time.time() - start))
