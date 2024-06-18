'''
import numpy as np
from time import time

def count_elapsed_time(f):
    def wrapper():
        # Start counting.
        start_time = time()
        # Take the original function's return value.
        ret = f()
        # Calculate the elapsed time.
        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret
    return wrapper


x = np.array([1,2,3,4,5])
print(x[0])
print(x[:3])
print(x[-2:])
y = np.arange(start=1, stop=11)
print(y)
print(sum(y))
print(y.sum())
print(f'Mean = {y.mean()}') #media
print(f'Min = {y.min()}') #minimo
print(f'Max = {y.max()}') #maximo
print(f'Std dev = {y.std()}') #standard derivation


@count_elapsed_time
def test():
    num1 = np.arange(1000000)
    print(num1.sum())


test()


@count_elapsed_time
def test():
    num1 = list(range(1000000))
    print(sum(num1))


test()

print(np.random.choice(['pizza', 'salad', 'pasta', 'burrito', 'hamburger']))
print(np.random.randint(low=1, high=100))
print(np.random.randint(low=1, high=100, size=100))
print(np.random.randint(low=1, high=100, size=1000000).mean())
'''

from pathlib import Path, PureWindowsPath
from os import system
import pandas as pd
import os

home = os.getcwd()
files_dir = Path(home, 'Files')
file_names = []
files = []


def file_choice(dir, type):
    print(f'Files in {PureWindowsPath(dir)}:')
    for files_ in Path(dir).glob('*' + type):
        file_names.append(files_.stem)
        files.append(PureWindowsPath(files_))
    for i in range(len(file_names)):
        print(f'[{i + 1}]. {file_names[i]}')
    op = input('\nWhich file do you would to open?: ')
    system('cls')
    return int(op) - 1, files


def read_info_file_excel(lista, option):
    orders = pd.read_excel(lista[option])
    col = orders.columns.tolist()
    return orders, col, f'''
    {'*' * 75}
    Name: {Path(lista[option]).stem}
    Rows: {orders.shape[0]}
    Columns: {orders.shape[1]}
    Total data: {orders.shape[0] * orders.shape[1]}
    {'*' * 75}
    '''


def columns_(lista):
    for i in range(len(lista)):
        print(f'{i + 1}. {lista[i]}')


def view_col(dataframe, col):
    return dataframe[col]


def view_columns(dataframe, lista):
    return dataframe[lista]


selection, lista = file_choice(files_dir, '.xlsx')
dataframe, lista, info = read_info_file_excel(lista, selection)
print(info)
print('Columns: ')
columns_(lista)

