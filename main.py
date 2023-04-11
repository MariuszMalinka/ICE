import time
import importuj
import estimation
import pandas as pd
from datetime import datetime

## Importing variable for further use
(imported_data) = importuj.importuj()

if imported_data.type == 'Excel':

    ## This section prompts the user to select an estimation option and modifies the input data based on the option chosen. Prompt the user to choose an estimation option.
    print('Choose between estimation options.\n Write "Hour based" to treat data based on corresponding hour. \n Write "Day based" to treat data based on corresponding day of the week.\n Write "All" to treat all data. \nFor additional information check the user manual.')
    
    ## Get the user's estimation option input.
    estimation_option = input()
    
    ## If the user selected "Hour based", prompt for the hour to use for estimation and modify the input data accordingly.
    if estimation_option in ['Hour based','hour based']:
        ## Prompt the user for the hour to use for estimation.
        hour_check_str = input('Insert the time to which the relevant data should be treated. \n')
        hour_check = datetime.strptime(hour_check_str, '%H:%M:%S').time()
        ## Convert the second column of the imported_data table to datetime format using the given format.
        imported_data.table.iloc[:, 1] = pd.to_datetime(imported_data.table.iloc[:, 1], format='%H:%M:%S')
        ## Check for rows that match the user input.
        matching_rows = imported_data.table.iloc[:, 1].apply(lambda x: x.strftime('%H:%M:%S')) == hour_check_str
        ## If there are matching rows, modify the input variables and optimal output variables accordingly.
        if matching_rows.any():
            imported_data.input_variables = imported_data.input_variables[matching_rows]
            imported_data.optimal_output = imported_data.optimal_output[matching_rows]
        else:
            pass ## Do nothing if there are no matching rows.
    
    ## If the user selected "Day based", prompt for the day to use for estimation and modify the input data accordingly.
    elif estimation_option in ['Day based','day based']:
        day_check = input('Insert the day to which the relevant data should be treated. \n')
        ## Extract rows that match the user's choice of day
        matching_rows = imported_data.table.iloc[:, 0] == day_check
        ## Check if any rows match the user's choice
        if matching_rows.any():
            ## If any matching rows are found, select the corresponding input and output data
            imported_data.input_variables = imported_data.input_variables[matching_rows]
            imported_data.optimal_output = imported_data.optimal_output[matching_rows]
        else:
            pass ## Do nothing if there are no matching rows.
    
    ## If the user selected "All", no modification is necessary.
    elif estimation_option in ['All','all']:
        print('All data will be taken into consideration during estimation.')
    
    ## If the user input an unrecognized option, assume "All" was intended.
    else:
        print('Something went wrong, maybe you misspelled the option. All data will be taken into consideration during estimation.')
        
    ## Calculating the coefficients standing by the values in the further equation
    coefficients = estimation.estimation(imported_data.input_variables,imported_data.optimal_output)

    ## User enters values to calculate optimal value
    print('\nPlease enter input values to calculate optimal output value.')
    entered_values=list()
    for i in range(len(imported_data.column_names)):
        entered_values.append(float(input(str(imported_data.column_names[i]) + ': ')))
        time.sleep(0.1)

    ## Linear equation consisting of array from estimation and values entered by user
    optimal_output=0
    for i in range(len(imported_data.column_names)):
        optimal_output=optimal_output+coefficients[i]*entered_values[i]
    
    ## Results presentation to user
    print ('The optimal value is: ' + str(round(optimal_output[0],1)))
    time.sleep(5)

if imported_data.type == 'CSV':

    ## Calculating the coefficients standing by the values in the further equation
    coefficients = estimation.estimation(imported_data.input_variables,imported_data.optimal_output)

    ## User enters values to calculate optimal value
    print('\nPlease enter input values to calculate optimal output value.')
    entered_values=list()
    for i in range(imported_data.input_variables.shape[1]):
        entered_values.append(float(input('Variable ' + str(i+1) + ': ')))
        time.sleep(0.1)
    
    ## Linear equation consisting of array from estimation and values entered by user
    optimal_output=0
    for i in range(imported_data.input_variables.shape[1]):
        optimal_output=optimal_output+coefficients[i]*entered_values[i]
    
    ## Results presentation to user
    print ('The optimal value is: ' + str(round(optimal_output[0],1)))
    time.sleep(5)
