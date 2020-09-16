# -*- coding: utf-8 -*-
import time
import random
import win32api

BLACK = '█'
WHITE = '　'

H_SIZE = 20
W_SIZE = 10
PLAYGROUND = list()

def INIT_PLAYGROUND():
    for i in range(H_SIZE):
        PLAYGROUND.append(list())
        for j in range(W_SIZE):
            PLAYGROUND[i] = list(WHITE * W_SIZE)
            
def PRINT_PLAYGROUND(BOX):
    print('#'*(2*W_SIZE+2))
    for row in range(H_SIZE):
        print('#',end='')
        for col in range(W_SIZE):
            if  [row,col] in BOX:
                print(BLACK,end='')
            else:
                print(PLAYGROUND[row][col],end='')
        print('#')
    print('#'*(2*W_SIZE+2))

def REAL_BOX(BOX,DELTA):
    R_BOX = []
    for index in range(len(BOX)):
        R_BOX.append([
            BOX[index][0] + DELTA[0],
            BOX[index][1] + DELTA[1]
        ])
    return R_BOX
            

def SAVE_BOX(BOX):
    for e in BOX:
        PLAYGROUND[e[0]][e[1]] = BLACK

def TEST_BOX(BOX,P=0,D=1):
    flag = False
    if P == 0:        
        for e in BOX:
            if e[0]+1 >= H_SIZE or PLAYGROUND[e[0]+1][e[1]] == BLACK:
                flag = True
                break
    else:        
        for e in BOX:
            if e[1]+D >= W_SIZE or e[1]+D < 0 or PLAYGROUND[e[0]][e[1]+D] == BLACK:
                flag = True
                break
    return flag

def MOVE_BOX(BOX,P=0,D=1):
    DELTA[P] += D
        

def NEW_BOX(index):
    #return [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9]]
    if index == 0:
        # O
        return [[0,0],[0,1],[1,0],[1,1]]
    if index == 1:
        # L
        return [[0,0],[0,1],[0,2],[1,2]]
    if index == 2:
        # T
        return [[0,1],[1,0],[1,1],[1,2]]
    if index == 3:
        # I
        return [[0,1],[0,2],[0,3],[0,4]]
    if index == 4:
        # J
        return [[0,1],[1,1],[2,0],[2,1]]
    if index == 5:
        # Z
        return [[0,0],[0,1],[1,1],[1,2]]
    if index == 6:
        # S
        return [[0,1],[0,2],[1,0],[1,1]]

# [1,2]
T_BOX = [
    [0, -1],
    [1, 0]
    ]

def T(BOX):
    for index in range(len(BOX)):
        new_point = [
            BOX[index][0] * T_BOX[0][0] + BOX[index][1] * T_BOX[1][0],
            BOX[index][0] * T_BOX[0][1] + BOX[index][1] * T_BOX[1][1],
            ]
        BOX[index] = new_point
            

#################################################

INIT_PLAYGROUND()
COUNT = 0

DELTA = [4,0]
BOX = NEW_BOX(random.randint(0,6))
PRINT_PLAYGROUND(BOX)
while True:
    COUNT+=1
    COUNT=COUNT%5

    if COUNT == 0:
        if not TEST_BOX(REAL_BOX(BOX,DELTA)):
            MOVE_BOX(BOX)
        else:
            SAVE_BOX(REAL_BOX(BOX,DELTA))
            DELTA = [0,0]
            BOX = NEW_BOX(random.randint(0,6))

            res = []
            for r in range(H_SIZE):
                flag = True
                if WHITE in PLAYGROUND[r]:
                        flag = False
                if flag:
                    res.append(r)            
            if len(res) > 0:
                PLAYGROUND_NEW = list()
                for i in range(len(res)):
                    PLAYGROUND_NEW.append(list(WHITE * W_SIZE))
                PLAYGROUND_OLD = [PLAYGROUND[line] for line in range(H_SIZE) if line not in res]
                PLAYGROUND_NEW.extend(PLAYGROUND_OLD)
                PLAYGROUND = PLAYGROUND_NEW
            
            if TEST_BOX(REAL_BOX(BOX,DELTA)):
                SAVE_BOX(REAL_BOX(BOX,DELTA))
                PRINT_PLAYGROUND(REAL_BOX(BOX,DELTA))
                break
        PRINT_PLAYGROUND(REAL_BOX(BOX,DELTA))
        
    #d = random.randint(-3,3)
    #if not TEST_BOX(BOX,P=1,D=d):
    #    MOVE_BOX(BOX,P=1,D=d)
    #    PRINT_PLAYGROUND(BOX)

    if win32api.GetKeyState(87)>>8:
        # W
        T(BOX)
        PRINT_PLAYGROUND(REAL_BOX(BOX,DELTA))
    elif win32api.GetKeyState(65)>>8:
        # A
        if not TEST_BOX(REAL_BOX(BOX,DELTA),P=1,D=-1):
            MOVE_BOX(BOX,P=1,D=-1)
            PRINT_PLAYGROUND(REAL_BOX(BOX,DELTA))
    elif win32api.GetKeyState(83)>>8:
        # S
        if not TEST_BOX(REAL_BOX(BOX,DELTA),P=0,D=1):
            MOVE_BOX(BOX,P=0,D=1)
            PRINT_PLAYGROUND(REAL_BOX(BOX,DELTA))
    elif win32api.GetKeyState(68)>>8:
        # D
        if not TEST_BOX(REAL_BOX(BOX,DELTA),P=1,D=1):
            MOVE_BOX(BOX,P=1,D=1)
            PRINT_PLAYGROUND(REAL_BOX(BOX,DELTA))
    
    time.sleep(0.1)
print('OVER')
