import time
import importuj
import estimation
import pandas as pd
from datetime import datetime

## Importing variable for further use
(data1) = importuj.importuj()

if data1.type == 'Excel':

    ## User selects estimation options
    print('Choose between estimation options.\n Write "Hour based" to treat data based on corresponding hour. \n Write "Day based" to treat data based on corresponding day of the week.\n Write "All" to treat all data. \nFor additional information check the user manual.')
    
    estimation_option = input()
    
    if estimation_option in ['Hour based','hour based']:
        hour_check_str = input('Insert the time to which the relevant data should be treated. \n')
        hour_check = datetime.strptime(hour_check_str, '%H:%M:%S').time()
        data1.table.iloc[:, 1] = pd.to_datetime(data1.table.iloc[:, 1], format='%H:%M:%S')
        matching_rows = data1.table.iloc[:, 1].apply(lambda x: x.strftime('%H:%M:%S')) == hour_check_str
        if matching_rows.any():
            data1.input_variables = data1.input_variables[matching_rows]
            data1.optimal_output = data1.optimal_output[matching_rows]
        else:
            pass

    elif estimation_option in ['Day based','day based']:
        day_check = input('Insert the day to which the relevant data should be treated. \n')
        matching_rows = data1.table.iloc[:, 0] == day_check
        matching_rows = matching_rows[:-1]
        if matching_rows.any():
            data1.input_variables = data1.input_variables[matching_rows]
            data1.optimal_output = data1.optimal_output[matching_rows]
        else:
            pass
    elif estimation_option in ['All','all']:
        print('All data will be taken into consideration during estimation.')
    else:
        print('Something went wrong, maybe you misspelled the option. All data will be taken into consideration during estimation.')
        
    ## Calculating the coefficients standing by the values in the further equation
    b = estimation.estimation(data1.input_variables,data1.optimal_output)

    ## User enters values to calculate optimal value
    print('\nPlease enter input values to calculate optimal output value.')
    w=list()
    for i in range(len(data1.column_names)):
        w.append(float(input(str(data1.column_names[i]) + ': ')))
        time.sleep(0.1)

    ## Linear equation consisting of array from estimation and values entered by user
    z=0
    for i in range(len(data1.column_names)):
        z=z+b[i]*w[i]
    
    ## Results presentation to user
    print ('The optimal value is: ' + str(round(z[0],1)))
    time.sleep(5)

if data1.type == 'CSV':

    ## Calculating the coefficients standing by the values in the further equation
    b = estimation.estimation(data1.input_variables,data1.optimal_output)

    ## User enters values to calculate optimal value
    print('\nPlease enter input values to calculate optimal output value.')
    w=list()
    for i in range(data1.input_variables.shape[1]):
        w.append(float(input('Variable ' + str(i+1) + ': ')))
        time.sleep(0.1)
    
    ## Linear equation consisting of array from estimation and values entered by user
    z=0
    for i in range(data1.input_variables.shape[1]):
        z=z+b[i]*w[i]
    
    # Results presentation to user
    print ('The optimal value is: ' + str(round(z[0],1)))
    time.sleep(5)
