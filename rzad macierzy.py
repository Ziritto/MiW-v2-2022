#!/usr/bin/env python
# coding: utf-8

# In[13]:


def rzad_macierzy(A):
    rzad = len(A[0])
    for row in range(rzad):
        if A[row][row] != 0:
            for col in range(len(A)):
                if col != row:
                    mnoznik = A[col][row]/A[row][row]
                    for i in range(rzad):
                        A[col][i] -= (mnoznik*A[row][i])
        else:
            redukowanie = True
            for i in range(row+1, len(A)):
                if A[i][row] != 0:
                    A = swap(A, row, i, rzad)
                    redukowanie = False
                break
            
            if redukowanie:
                rzad -= 1
                for i in range(0, len(A)):
                    A[i][row] = A[i][rzad]
            row -= 1
    return rzad
            
def swap(A, rzad1, rzad2, col):
    for i in range(col):
        temp = A[rzad1][i]
        A[rzad1][i] = A[rzad2][i]
        A[rzad2][i] = temp
        
        
A= [[1,1,0,1,1],[1,0,1,1,1],[0,1,1,1,1],[1,1,1,0,1],[1,1,1,1,0]] #5
B= [[2,1,-4],[3,5,-7],[4,-5,-6]] #2

print(rzad_macierzy(A))
print(rzad_macierzy(B))


# In[ ]:




