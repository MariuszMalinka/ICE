import time
import numpy as np
import pandas as pd
def importuj ():
    
    ## Import and distinguish a file (15 lines)
    user_input = input('Please enter file name or path: ')
    try:    
        try:
            a = pd.read_excel(user_input)
            return importujExcel(a)
        except:
            a = pd.read_excel(user_input + str('.xlsx'))
            return importujExcel(a)
    except:
        try:
            a = pd.read_csv(user_input)
            return importujCSV(a)
        except:
            a = pd.read_csv(user_input + str('.csv'))
            return importujCSV(a)

def importujExcel (a):
    print('Choose between importing option.\n Write "Standard" if your file is compatible with standard file format.\n Write "Manual" if you want to set data boundaries by yourself.\nFor additional information check the user manual.')
    impsetting = input()

    ## Setting import boundaries according to standard excel file (6 lines)
    if impsetting == 'Standard' or impsetting == 'standard':
        wierszstart = 0
        wierszkoniec = -1
        optymalna = 2
        wejsc_start = 3
        wejsc_koniec = -1
    
    ## User sets import boundaries (19 lines)
    elif impsetting == 'Manual' or impsetting == 'manual':
        g = list(a.columns)
        wierszstart = int(input('Please enter index of the first row: '))
        wierszkoniec = int(input('Please enter index of the last row: '))
        user_input = input('Please enter index or name of the column with optimal values: ')
        try:
            optymalna = int(user_input)
        except: 
            optymalna = g.index(user_input)
        user_input = input('Please enter index or name of the first column with input values: ')
        try:
            wejsc_start = int(user_input)
        except:
            wejsc_start = g.index(user_input)
        user_input = input('Please enter index or name of the last column with input values: ')
        try:
            wejsc_koniec = int(user_input)
        except:
            wejsc_koniec = g.index(user_input)

    else:
        print('Something went wrong, maybe you misspelled the option.')
        time.sleep(5)
        quit()

    ## Creating arrays for further operations (3 lines)
    k = a.columns[wejsc_start:wejsc_koniec]
    x = np.array(a.iloc[wierszstart:wierszkoniec,wejsc_start:wejsc_koniec+1])
    y = np.array(a.iloc[wierszstart:wierszkoniec,optymalna:optymalna+1])
    return (x,y,k)

def importujCSV (a):
    return 0