import numpy as np
import pandas as pd
def importuj ():
    a = pd.read_excel(input('Nazwa pliku excel: ') + str('.xlsx'))
    #print(np.array(a.iloc[0:-1,2:8]))
    wierszstart = 0#int(input('Wprowadź index wiersza początkowego (domyślnie 0): '))
    wierszkoniec = -1#int(input('Wprowadź index wiersza końcowego (dla całego zbioru wprowadź "-1"): '))
    optymalna = 2#int(input('Wprowadź index kolumny zawierającej wartość optymalną (2): '))
    wejsc_start = 3#int(input('Wprowadź index pierwszej kolumny zawierającej wartości zewnętrzne (3): '))
    wejsc_koniec = 8#int(input('Wprowadź index ostatniej kolumny zawierającej wartości zewnętzrzne (8): '))
    x=np.array(a.iloc[wierszstart:wierszkoniec,wejsc_start:wejsc_koniec])
    y=np.array(a.iloc[wierszstart:wierszkoniec,optymalna:optymalna+1])
    return (x,y)