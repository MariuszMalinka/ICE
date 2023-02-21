import time
import importuj
import estimation

## Importing variable for further use
(data1) = importuj.importuj()

## Calculating the coefficients standing by the values in the further equation
b = estimation.estimation(data1.input_variables,data1.optimal_output)

if data1.type == 'Excel':
    ## User enters values to calculate optimal value
    print(b)
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
    ## User enters values to calculate optimal value
    print(b)
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
