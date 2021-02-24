import sys
import numpy as np
from random import sample
import itertools as IT
from statistics import mean

def fillList(lista, choiceList, counter):
    choices = sample(choiceList,counter)

    for k in choices:
        lista[k] = 1
    return lista

def findHorizontal(arr):
    total = 0
    for row in arr:
        counter = 0
        for i in range(len(row)-1):
            if row[i] == row[i+1] and row[i] == 1:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                total += 1
                counter = 0
    return total

def findVertical(arr):
    total = 0
    for j in range(len(arr)-1):
        counter = 0
        for i in range(len(arr)-1):
            if arr[i][j] == arr[i+1][j] and arr[i][j] == 1:
                counter = counter + 1
            else:
                counter = 0
            if counter == 3:
                total = total +1
                counter = 0
    return total

def find_max_list_idx(list):
    list_len = [len(i) for i in list]
    return np.argmax(np.array(list_len))

def findDiagonal(arr):
    total = 0
    N = len(arr)
    d = dict()
    for i,j in IT.product(range(N), repeat=2):
        d.setdefault(j-i, []).append((i,j))
    arr2 = [[arr[i][j] for i,j in d[k]] for k in range(-N+1,N)]
    arr2 = arr2[find_max_list_idx(arr2)]
    counter = 0
    for i in range(len(arr2)-1):
        if arr2[i] == arr2[i+1] and arr2[i] == 1:
            counter += 1
        else:
            counter = 0
        if counter == 3:
            total += 1
            counter = 0
    return total

if __name__ == '__main__':
    try:
        n = int(input("Give n: "))
    except Exception as e :
        sys.exit(f"Error: {e} \nPlease give integer!")

    reps = 100
    hor = []
    vert = []
    diag = []
    for _ in range(reps):
        arr = np.zeros([n,n], int)
        for i in range(n):
            choices = [num for num in range(0,n)]
            counter = int(round(n/2))
            arr[i] = fillList(arr[i],choices,counter)

        hor.append(findHorizontal(arr))
        vert.append(findVertical(arr))
        diag.append(findDiagonal(arr))

    print(f"Average horizontal consecutives 1 found {mean(hor)}")
    print(f"Average vertical consecutives 1 found {mean(vert)}")
    print(f"Average diagonal consecutives 1 found {mean(diag)}")
