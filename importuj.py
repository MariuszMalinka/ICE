import os
import time
import numpy as np
import pandas as pd
import csv
def importuj ():
    

    ## Creating a class containing all important information
    class Data:
        def __init__(self,type,optimal_output,input_variables,column_names,table):
            self.type = type
            self.optimal_output = optimal_output
            self.input_variables = input_variables
            self.column_names = column_names
            self.table = table
    
    data1=Data(0,0,0,0,0)


    ## Import a file
    user_input = input('Please enter file name or path: ')

    if user_input.find ('.xlsx') >= 0 :
        data1.table = pd.read_excel(user_input)
        data1.table.dropna(inplace=True)
        data1.type = 'Excel'
        return importujExcel(data1)

    elif user_input.find ('.csv') >= 0 :
        data1.table = pd.read_csv(user_input)
        data1.type = 'CSV'
        return importujCSV(data1)

    ## Distinguish file extension
    else:
        b=np.array(os.listdir())
        j=0
        for i in range(len(b)):
            d=b[i].split(".")
            if d[0] == user_input:
                j=d[1]
                break
        if j == 'xlsx' :
            data1.table = pd.read_excel(user_input + str('.xlsx'))
            data1.table.dropna(inplace=True) ## Deleting empty rows
            data1.type = 'Excel'
            return importujExcel(data1)
        elif j == 'csv' :
            data1.table = pd.read_csv(user_input + str('.csv'), header=None)
            data1.type = 'CSV'
            return importujCSV(data1)
        else:
            print('Sorry, we could not find such file.')
            time.sleep(5)
            quit()

def importujExcel (data1):
    print('Choose between importing option.\n Write "Standard" if your file is compatible with standard file format.\n Write "Manual" if you want to set data boundaries by yourself.\nFor additional information check the user manual.')

    impsetting = input()

    ## Setting import boundaries according to standard excel file
    if impsetting in ['Standard','standard']:
        wierszstart = 0
        wierszkoniec = None
        optymalna = 2
        wejsc_start = 3
        wejsc_koniec = None
    
    ## User sets import boundaries
    elif impsetting in ['Manual','manual']:
        g = list(data1.table.columns)
        
        wierszstart = int(input('Please enter index of the first row: '))

        wierszkoniec = input('Please enter index of the last row: ')
        if wierszkoniec == 'End':
            wierszkoniec = None
        else:
            wierszkoniec = int(wierszkoniec)
        
        optymalna = input('Please enter index or name of the column with optimal values: ')
        if optymalna in g:
            optymalna = g.index(optymalna)
        else:
            optymalna = int(optymalna)

        wejsc_start = input('Please enter index or name of the first column with input values: ')
        if wejsc_start in g:
            wejsc_start = g.index(wejsc_start)
        else:
            wejsc_start = int(wejsc_start)

        wejsc_koniec = input('Please enter index or name of the last column with input values: ')
        if wejsc_koniec in g:
            wejsc_koniec = g.index(wejsc_koniec) + 1
        elif wejsc_koniec == 'End':
            wejsc_koniec = None
        else:
            wejsc_koniec = int(wejsc_koniec)

    else:
        print('Something went wrong, maybe you misspelled the option.')
        time.sleep(5)
        quit()

    ## Creating arrays for further operations
    data1.column_names = data1.table.columns[wejsc_start:wejsc_koniec]
    data1.input_variables = np.array(data1.table.iloc[wierszstart:wierszkoniec,wejsc_start:wejsc_koniec])
    data1.optimal_output = np.array(data1.table.iloc[wierszstart:wierszkoniec,optymalna:optymalna+1])
    return (data1)

def importujCSV (data1):
    data1.optimal_output = np.array(data1.table.iloc[:,0:1])
    data1.input_variables = np.array(data1.table.iloc[:,1:])
    return (data1)
