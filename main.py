import time
import importuj
import estimation

## Importing arrays for further use in calculation (x,y) and values names (k)
(x,y,k) = importuj.importuj()

## Calculating the coefficients standing by the values in the further equation
b = estimation.estimation(x,y)

## User enters values to calculate optimal value (4 lines)
print('\nPlease enter input values to calculate optimal output value.')
w=list()
for i in range(len(k)):
    w.append(float(input(str(k[i]) + ': ')))
    time.sleep(0.1)

## Linear equation consisting of array from estimation and values entered by user (3 lines)
z=0
for i in range(len(k)):
    z=z+b[i]*w[i]

## Results presentation to user
print ('The optimal value is: ' + str(round(z[0],1)))
time.sleep(5)