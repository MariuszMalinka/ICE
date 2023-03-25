import os
import time
import numpy as np
import pandas as pd
def importuj ():
    

    ## Define a class called "Data" with various attributes
    class Data:
        def __init__(self,type,optimal_output,input_variables,column_names,table):
            self.type = type
            self.optimal_output = optimal_output
            self.input_variables = input_variables
            self.column_names = column_names
            self.table = table
    
    ## Create an instance of the "Data" class with default values
    imported_data=Data(0,0,0,0,0)

    ## Prompt the user to enter a file name or path
    user_input = input('Please enter file name or path: ')

    ## If the file has a .xlsx extension, read it as an Excel file and store it in imported_data.table
    if user_input.find ('.xlsx') >= 0 :
        imported_data.table = pd.read_excel(user_input)
        imported_data.table.dropna(inplace=True) ## Remove any rows with missing values
        imported_data.type = 'Excel'
        ## Call the importujExcel() function with the imported_data object as an argument
        return importujExcel(imported_data)

    ## If the file has a .csv extension, read it as a CSV file and store it in imported_data.table
    elif user_input.find ('.csv') >= 0 :
        imported_data.table = pd.read_csv(user_input)
        imported_data.type = 'CSV'
        ## Call the importujCSV() function with the imported_data object as an argument
        return importujCSV(imported_data)

    ## If the file has no extension, search the current directory for files with the same name
    else:
        ## Create an array of all files in the current directory
        b=np.array(os.listdir())
        j=0
        ## Iterate through the array and split each filename by the "." character
        for i in range(len(b)):
            d=b[i].split(".")
            ## If the first part of the filename matches the user input, store the extension in j and break the loop
            if d[0] == user_input:
                j=d[1]
                break
        ## If the extension is .xlsx, read the file as an Excel file and store it in imported_data.table
        if j == 'xlsx' :
            imported_data.table = pd.read_excel(user_input + str('.xlsx'))
            imported_data.table.dropna(inplace=True) ## Remove any rows with missing values
            imported_data.type = 'Excel'
            ## Call the importujExcel() function with the imported_data object as an argument
            return importujExcel(imported_data)
        ## If the extension is .csv, read the file as a CSV file and store it in imported_data.table
        elif j == 'csv' :
            imported_data.table = pd.read_csv(user_input + str('.csv'), header=None)
            imported_data.type = 'CSV'
            ## Call the importujCSV() function with the imported_data object as an argument
            return importujCSV(imported_data)
        ## If the file is not found or has an unrecognized extension, print an error message and exit the program
        else:
            print('Sorry, we could not find such file.')
            time.sleep(5)
            quit()

def importujExcel (imported_data):
    ## Prompting user to choose between importing options
    print('Choose between importing option.\n Write "Standard" if your file is compatible with standard file format.\n Write "Manual" if you want to set data boundaries by yourself.\nFor additional information check the user manual.')

    ## Retrieving the user's choice
    impsetting = input()

    ## Setting import boundaries according to standard Excel file
    if impsetting in ['Standard','standard']:
        ## Standard boundary settings for Excel file
        row_start = 0
        row_end = None
        optimal = 2
        column_start = 3
        column_end = None
    
    ## User sets import boundaries
    elif impsetting in ['Manual','manual']:
        ## Retrieving column names for the file
        g = list(imported_data.table.columns)
        
        ## Retrieving row start boundary
        row_start = int(input('Please enter index of the first row: '))

        ## Retrieving row end boundary
        row_end = input('Please enter index of the last row: ')
        if row_end == 'End':
            row_end = None
        else:
            row_end = int(row_end)
        
        ## Retrieving optimal column index or name
        optimal = input('Please enter index or name of the column with optimal values: ')
        if optimal in g:
            optimal = g.index(optimal)
        else:
            optimal = int(optimal)

        ## Retrieving column start index or name
        column_start = input('Please enter index or name of the first column with input values: ')
        if column_start in g:
            column_start = g.index(column_start)
        else:
            column_start = int(column_start)

        ## Retrieving column end index or name
        column_end = input('Please enter index or name of the last column with input values: ')
        if column_end in g:
            column_end = g.index(column_end) + 1
        elif column_end == 'End':
            column_end = None
        else:
            column_end = int(column_end)

    else:
        ## Error message if an incorrect option is chosen
        print('Something went wrong, maybe you misspelled the option.')
        time.sleep(5)
        quit()

    ## Creating arrays for further operations
    imported_data.column_names = imported_data.table.columns[column_start:column_end]
    imported_data.input_variables = np.array(imported_data.table.iloc[row_start:row_end,column_start:column_end])
    imported_data.optimal_output = np.array(imported_data.table.iloc[row_start:row_end,optimal:optimal+1])
    ## Returning the imported data object
    return (imported_data)

def importujCSV (imported_data):
    imported_data.optimal_output = np.array(imported_data.table.iloc[:,0:1])
    imported_data.input_variables = np.array(imported_data.table.iloc[:,1:])
    return (imported_data)
