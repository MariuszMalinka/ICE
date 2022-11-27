import time
import numpy as np
import pandas as pd
def importuj ():
    
    ## Importing Excel file (5 lines)
    user_input = input('Please enter excel file name: ')
    try:
        a = pd.read_excel(user_input + str('.xlsx'))
    except:
        a = pd.read_excel(str(user_input))

    ## User states the import settings option (18 lines)
    print('Choose between importing option.\n Type in "Standard" if your file is compatible with standard Excel file format.\n Type in "Manual" if you want to set data boundaries by yourself.\nFor additional information check the user manual.')
    impsetting = input()
    if impsetting == 'Standard' or impsetting == 'standard':
        wierszstart = 0
        wierszkoniec = -1
        optymalna = 2
        wejsc_start = 3
        wejsc_koniec = 8
    elif impsetting == 'Manual' or impsetting == 'manual':
        wierszstart = int(input('Please enter index of the first row: '))
        wierszkoniec = int(input('Please enter index of the last row: '))
        optymalna = int(input('Please enter index of the column with optimal values: '))
        wejsc_start = int(input('Please enter index of the first column with input values: '))
        wejsc_koniec = int(input('Please enter index of the last column with input values: '))
    else:
        print('Something went wrong, maybe you misspelled the option.')
        time.sleep(5)
        quit()

    ## Creating arrays for further operations (3 lines)
    k = a.columns[wejsc_start:wejsc_koniec]
    x = np.array(a.iloc[wierszstart:wierszkoniec,wejsc_start:wejsc_koniec])
    y = np.array(a.iloc[wierszstart:wierszkoniec,optymalna:optymalna+1])
    return (x,y,k)