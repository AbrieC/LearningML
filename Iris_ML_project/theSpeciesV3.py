
#Inputs
Sepal_width = float(input ("Please Enter your sepal width (Cm) [range between 2.0 and 4.4 cm ] :"))
Sepal_length = float(input ("Please Enter your sepal length (Cm) [range between 4.9 and 7.9 cm ]:"))
Petal_width = float(input("Please Enter your petal width (Cm) [range between 0.1 and 2.5 cm ]: "))
Petal_length = float(input("Please Enter your petal length (Cm) [range between 1.0 and 6.9 cm ]: "))

if (2.3 <= Sepal_width <= 4.4 and 4.3 <= Sepal_length <= 5.8 and  # i used the output from task 4 irisGetInfo.py to classfiy using the min and max values of the features (sepal width,
    0.1 <= Petal_width <= 0.6 and 1.0 <= Petal_length <= 1.9 ):   # sepal length , petal width , petal length )
    print ("It is Setosa") # output
elif (2.0 <= Sepal_width <= 3.4 and 4.9 <= Sepal_length <= 6.9 and
    1.0 <= Petal_width <= 1.8 and 3.0 <= Petal_length <= 5.1):
    print ("It is Versi-color") #output
elif (2.2 <= Sepal_width <= 3.8 and 4.9 <= Sepal_length <= 7.9 and
    1.4 <= Petal_width <= 2.5 and 4.5 <= Petal_length <= 6.9):
    print ("It is Virginica")    #output
else :

    print ("it is undefined")           #output      
#End

"""
SepalLengthCm   SepalWidthCm    PetalLengthCm   PetalWidthCm

5.9 3.2 4.8 1.8
"""
