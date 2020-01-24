#!/usr/bin/env python

def verify_number(sudoku, n):
    for i in range(n):
        for j in range(n):
            if 1<=sudoku[i][j]<=9:
                continue
            else:
                return False

    return True

def verify_rows(sudoku, n):
    flag=0
    for i in range(n):
        flag=len(set(sudoku[i])) == len(sudoku[i])
        if not flag:
            return False

    return True
    

def verify_columns(sudoku, n):
    flag=0
    column_list=[]
    for i in range(n):
        for j in range(n):
            column_list.append(sudoku[j][i])

        #print(new_list)
        flag=len(set(column_list)) == len(column_list)
        #print(flag)
        if not flag:
            return False
        else:
            column_list=[]
            continue

    return True

def CheckInBox(sudoku,row,col):
    flag=0
    box_list=[]
    for i in range(3):
        for j in range(3):
            val=sudoku[i+row][j+col]
            box_list.append(val)

    flag=len(set(box_list)) == len(box_list)
    if not flag:
        return False
        
    return True

def verify_box(sudoku):
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not CheckInBox(sudoku,i,j):
                return False

    return True

def check_len(sudoku, n):
    for i in range(n):
        if len(arr[i]) > n or len(arr[i]) < n:
            return False
        else:
            continue

    return True

if __name__ == "__main__":

    arr=[]
    for i in range(9):
        arr.append(map(int,raw_input().split()))
        
    
    #arr=[[5, 3, 4, 6, 7, 8, 9, 1, 2],
    #     [6, 7, 2, 1, 9, 5, 3, 4, 8],
    #     [1, 9, 8, 3, 4, 2, 5, 6, 7],
    #     [8, 5, 9, 7, 6, 1, 4, 2, 3],
    #     [4, 2, 6, 8, 5, 3, 7, 9, 1],
    #     [7, 1, 3, 9, 2, 4, 8, 5, 6],
    #     [9, 6, 1, 5, 3, 7, 2, 8, 4],
    #     [2, 8, 7, 4, 1, 9, 6, 3, 5],
    #     [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    if verify_columns(arr, 9) and verify_rows(arr, 9) and verify_box(arr) and check_len(arr, 9):
        print("True")
    else:
        print("False")
