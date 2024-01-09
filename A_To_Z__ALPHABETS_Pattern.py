# A to Z libary
# A
def A():
    for i in range(1, 6):

        if i == 5:
            for j in range(1, 6):
                if j == 1 or j == 5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        elif i == 3:
            for k in range(1, 6):
                if k == 3 or k == 4:
                    print("*", end="   ")
                else:
                    print(" ", end="")
        else:
            for k in range(5, i, -1):
                print(" ", end="")
            for j in range(1, i+1):
                print("*", end=" ")
        print()
    print()


# B
def B():
    for i in range(1, 6):
        if i == 1 or i == 3 or i == 5:
            for j in range(1, 5):
                print("*", end=" ")
        else:
            for k in range(1, 6):
                if k == 1 or k == 5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        print()
    print()


# C
def C():
    for i in range(1, 6):
        for j in range(1, 6):
            if i == 1 and 2 < j or 1 < i < 5 and j == 2 or i == 5 and 2 < j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()


# D
def D():
    for i in range(1, 6):
        for j in range(1, 6):
            if   i == 1 and j < 4:
                print("*", end=" ")
            elif i == 2 and j == 4 or j==1:
                print("*", end=" ")
            elif i == 3 and j == 4 or j==1:
                print("*", end=" ")
            elif i == 4 and j == 4 or j==1:
                print("*", end=" ")
            elif i == 5 and j < 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()


# E
def E():
    for i in range(1,6):
        for j in range(1,5):
            if  i==1 or i==3 or i==5 or i==2 and j==1 or i==4 and j==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
    

# F
def F():
    for i in range(1,6):
        for j in range(1,5):
            if  i==1 or i==3 or i==5 and j==1 or i==2 and j==1 or i==4 and j==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()


# G
def G():
    for i in range(1,6):
        for j in range(1,6):
            if i==1 and 1<j<5 or i==5 and 1<j<4 :
                print("*", end=" ")
            elif i==2 and j==1:
                print("*",end=" ")
            elif i==3 and (j==1 or j==3 or j==4):
                print("*",end=" ")
            elif i==4 and (j==1  or j==4):
                print("*",end=" ")
            else:
                print(" ", end=" ")
        print()
    print()


# H
def H():
    for i in range(1,6):
        if  i==3:
            for j in range(1,6):
                print("*",end=" ")
        else:
            for k in range(1,6):
                if k==1 or k==5:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        print()
    print()
# I
def I():
    for i in range(1,6):
        for j in range(1,4):
            if i==1 or i==5 or j==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()

# J
def J():
    for i in range(1,6):
        for j in range(1,6):
            if (i==1 and 1<j<5) or j==3 and i<5:
                print("*",end=" ")
            elif i==4 and(j==1):
                print("*",end=" ")
            elif i==5 and(j==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()


# K
def K():
    for i in range(1,6):
        for j in range(1,6):
            if j==1:
                print("*",end=" ")
            elif i==1 and j==4 or i==2 and j==3 or i==3 and j==2 or i==4 and j==3 or i==5 and j==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
# L
def L():
    for i in range(1,6):
        for j in range(1,5):
            if  0<i<5 and j==1 or (i==5 and j<4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()

# M
def M():
    for i in range(1,6):
        for j in range(1,6):
            if j==1 or j==5:
                print("*",end=" ")
            elif j==3 and i==3:
                print("*",end=" ")
            elif j==2 and i==2:
                print("*",end=" ")
            elif j==4 and i==2:
                print("*",end=" ")
            
            else:
                print(" ",end=" ")
        print()
    print()
# N
def N():
    for i in range(1,6):
        for j in range(1,6):
            if  j==1 or j==5 or i==3 and j==3 or i==2 and j==2 or i==4 and j==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
# O
def O():
    for i in range(1,6):
        for j in range(1,6):
            if i==1 and j==3 or i==5 and j==3:
                print("*",end=" ")
            elif 1<i<5 and (j==2 or j==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
# P
def P():
    for i in range(1,6):
        for j in range(1,5):
            if i==1 and j<4 or i==3 and j<4 or j==1 or i==2 and (j==1 or j==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
# Q
def Q():
    for i in range(1,6):
        for j in range(1,6):
            if i==1 and j==3 or i==4 and j==3:
                print("*",end=" ")
            elif 1<i<4 and (j==2 or j==4):
                print("*",end=" ")
            elif i==3 and j==3:
                print("*",end=" ")
            elif i==4 and j==4:
                print("*",end="")
            elif i==5 and j==4: 
                print(" *",end="")
            else:
                print(" ",end=" ")
            print()
    print()

# R
def R():
    for i in range(1,6):
        if i==1 or i==3 or i==5 and j==1:
            for j in range(1,5):
                print("*",end=" ")
        else:
            for k in range(1,6):
                if k==1 or k==5:
                    print("*",end="")
                else:
                    print(" ",end=" ")
        print()
    print()

# S
def S():
    for i in range(1,6):
        if i==1 or i==3 or i==5:
            for j in range(1,6):
                print("*",end=" ")
        if i==2:
            print("*",end="")
        if i==4:
            for k in range(1,i+2):
                if k<5:
                    print(" ",end=" ")
                else:
                    print("*",end="")
        print()
    print()


# T
def T():
    for i in range(1,6):
        for j in range(1,6):
            if i==1 or j==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()


# U
def U():
    for i in range(1,6):
        if  i==5:
            for j in range(1,4):
                print(" *",end=" ")
        else:
            for k in range(1,6):
                if k==1 or k==5:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        print()
    print()


# V
def V():
    for i in range(1,6):
        for j in range(1,6):
            if   i==1 and (j==2 or j==4):
                print("*",end=" ")
            elif i==2 and (j==2 or j==4):
                print("*",end=" ")
            elif i==3 and (j==2 or j==4):
                print("*",end=" ")
            elif i==4 and (j==2 or j==3):
                print(" *",end="")
            elif i==5 and j==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()


# W
def W():
    for i in range(1,6):
        for j in range(1,6):
            if  j==1 or j==5 or i==3 and j==3  or i==4 and (j==4 or j==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()


# X
def X():
    for i in range(1,6):
        for j in range(1,6):
            if i==1 and (j==1 or j==5):
                print("*",end=" ")
            elif i==2 and (j==2 or j==4):
                print("*",end=" ")
            elif i==3 and j==3:
                print("*",end=" ")
            elif i==4 and (j==2 or j==4):
                print("*",end=" ")
            elif i==5 and (j==1 or j==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()

        
# Y
def Y():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    for i in range(1,6):
        for j in range(1,6):
            if i==1 and (j==1 or j==5) or i==2 and (j==2 or j==4) or 2<i and j==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()


# Z
def Z():
    for i in range(1,6):
        for j in range(1,6):
            if  i==1 or i==5:
                print("*",end=" ")
            elif i==2 and j==4 or i==3 and j==3 or i==4 and j==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    print()
#CAlling the function

# args=(S,H,U,B,H,A,M)
# for i in args:
    # i()

name=list(input("enter your name :--"))
array = list(name)
for i in array:
    if   i == 'a' or i == 'A':
        A()
    elif i == 'b' or i == 'B':
        B()
    elif i == 'c' or i == 'C':
        C()
    elif i == 'd' or i == 'D':
        D()
    elif i == 'e' or i == 'E':
        E()
    elif i == 'f' or i == 'F':
        F()
    elif i == 'g' or i == 'G':
        G()
    elif i == 'h' or i == 'H':
        H()
    elif i == 'i' or i == 'I':
        I()
    elif i == 'j' or i == 'J':
        J()
    elif i == 'k' or i == 'K':
        K()
    elif i == 'l' or i == 'L':
        L()
    elif i == 'm' or i == 'M':
        M()
    elif i == 'n' or i == 'N':
        N()
    elif i == 'o' or i == 'O':
        O()
    elif i == 'p' or i == 'P':
        P()
    elif i == 'q' or i == 'Q':
        Q()
    elif i == 'r' or i == 'R':
        R()
    elif i == 's' or i == 'S':
        S()
    elif i == 't' or i == 'T':
        T()
    elif i == 'u' or i == 'U':
        U()
    elif i == 'v' or i == 'V':
        V()
    elif i == 'w' or i == 'W':
        W()
    elif i == 'x' or i == 'X':
        X()
    elif i == 'y' or i == 'Y':
        Y()
    elif i == 'z' or i == 'Z':
        Z()
    else:
        print(" ")
    








