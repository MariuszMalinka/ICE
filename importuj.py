import os
import time
import numpy as np
import pandas as pd
def importuj ():
    
    ## Import a file (24 lines)
    user_input = input('Please enter file name or path: ')

    if user_input.find ('.xlsx') >= 0 :
        a = pd.read_excel(user_input)
        return importujExcel(a)

    elif user_input.find ('.csv') >= 0 :
        a = pd.read_csv(user_input)
        return importujCSV(a)

    ## Distinguish file extension (17 lines)
    else:
        b=np.array(os.listdir())
        for i in range(len(b)):
            d=b[i].split(".")
            if d[0] == 'Data':
                j=d[1]
                break
        if j == 'xlsx' :
            a = pd.read_excel(user_input + str('.xlsx'))
            return importujExcel(a)
        elif j == 'csv' :
            a = pd.read_csv(user_input + str('.csv'))
            return importujCSV(a)
        else:
            print('Sorry, we could not find such file.')
            time.sleep(5)
            quit()

def importujExcel (a):
    print('Choose between importing option.\n Write "Standard" if your file is compatible with standard file format.\n Write "Manual" if you want to set data boundaries by yourself.\nFor additional information check the user manual.')
    impsetting = input()

    ## Setting import boundaries according to standard excel file (6 lines)
    if impsetting in ['Standard','standard']:
        wierszstart = 0
        wierszkoniec = -1
        optymalna = 2
        wejsc_start = 3
        wejsc_koniec = 8
    
    ## User sets import boundaries (21 lines)
    elif impsetting in ['Manual','manual']:
        g = list(a.columns)
        wierszstart = int(input('Please enter index of the first row: '))
        wierszkoniec = int(input('Please enter index of the last row: '))

        user_input = input('Please enter index or name of the column with optimal values: ')
        if user_input in g:
            optymalna = g.index(user_input)
        else:
            optymalna = int(user_input)

        user_input = input('Please enter index or name of the first column with input values: ')
        if user_input in g:
            wejsc_start = g.index(user_input)
        else:
            wejsc_start = int(user_input)

        user_input = input('Please enter index or name of the last column with input values: ')
        if user_input in g:
            wejsc_koniec = g.index(user_input) + 1
        elif user_input == str(-1):
            wejsc_koniec = int(user_input)
        else:
            wejsc_koniec = int(user_input) + 1

    else:
        print('Something went wrong, maybe you misspelled the option.')
        time.sleep(5)
        quit()

    ## Creating arrays for further operations (3 lines)
    k = a.columns[wejsc_start:wejsc_koniec]
    x = np.array(a.iloc[wierszstart:wierszkoniec,wejsc_start:wejsc_koniec])
    y = np.array(a.iloc[wierszstart:wierszkoniec,optymalna:optymalna+1])
    return (x,y,k)

def importujCSV (a):
    print('CSV support coming soon!')
    time.sleep(5)
    quit()