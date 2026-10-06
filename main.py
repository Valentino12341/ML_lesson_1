# CLASSIFICATIONS      REGRESION        RECOMENDATION 

#CLASSIFICATIONS   Finit set of input     like male od female cat or dog   car , bike   of train  

#REGRESION  Infinite amount of outputs like predictions like what card will be pulled next what weather it is tomorrow etc 

#RECOMENDATION  Like in a algorithm  for example the movie genres you watch that it recomends more of that genre 




#LINEAR REGRESION 

#m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)
#c = mean(y) – m * mean(x)

x=[2,4,6,8,4,3,9,11]
y=[4,5,6,7,8,9,10,11]

def finding_mean(a):
    return(sum(a)/len(a))

mean_x = finding_mean(x)
mean_y = finding_mean(y)

print("Mean X :",mean_x)
print("Mean Y :",mean_y)


numerator = 0
denomenator = 0


for i in range(len(x)):
    numerator = numerator + ((x[i]-mean_x)*(y[i]-mean_y))
    denomenator = denomenator + pow((x[i]-mean_x),2)

print("manualy finding values for m and c :")

m = numerator/denomenator
m = round(m,3)
print("m =",m)
c = round(mean_y - m*mean_x,1)
print("c =",c)


import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[2],[4],[6],[8],[4],[3],[9],[11]])
y = np.array([[4],[5],[6],[7],[8],[9],[10],[11]])

model = LinearRegression()
model = model.fit(x,y)
print("finding m and c troug machine learning algorithm ")

print("m =",model.coef_)
print("c =",model.intercept_)
