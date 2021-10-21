import time
from data import data
import tracemalloc
import csv
from multiprocessing import Pool


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


def pool_handler():
    p = Pool()
    p.map(single_function, data)


header()
if __name__ == '__main__':

    tracemalloc.start()
    start = time.time()
    pool_handler()

    print("Current %d, Peak %d" % tracemalloc.get_traced_memory())
    print("All done! {}".format(time.time() - start))
