import importuj
import estimation
import obliczenia
(x,y) = importuj.importuj()
b = estimation.estimation(x,y)
z = obliczenia.obliczenia(b)
print ('Optymalna temperatura to: ' + str(round(z[0],1)) + '°C.')