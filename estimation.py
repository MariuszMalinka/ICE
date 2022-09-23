import numpy as np
#x=np.array([[1,2],[4,3],[9,8]]) # x to macierz składająca się z warunków atmosferycznych
#y=np.array([[3],[6],[10]]) # y to wektor składający się z idealnych wartości nastawienia

def estimation(x,y):
    # b = (X^T X)^(-1) X^T Y # b to wektor współczynników stojących przy wartościach w równaniu wyznaczającym idealną wartość nastawienia
    b=np.matmul(np.matmul(np.linalg.inv(np.matmul(x.T,x)),x.T),y)
    return b