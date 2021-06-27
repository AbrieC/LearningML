"""# Acquire the inputs from the data
Sepal_width = float(input ("Please Enter your sepal width (Cm) [range between 2.0 and 4.4 cm ] :"))
Sepal_length = float(input ("Please Enter your sepal length (Cm) [range between 4.9 and 7.9 cm ]:"))
Petal_width = float(input("Please Enter your petal width (Cm) [range between 0.1 and 2.5 cm ]: "))
Petal_length = float(input("Please Enter your petal length (Cm) [range between 1.0 and 6.9 cm ]: "))
"""

SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm = input("Please enter the feature values in correct order as shown in Iris.csv, start with SepalLengthCm, ..").split()

print(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)

#define classification criteria

if (2.3 <= SepalWidthCm <= 4.4 and 4.3 <= SepalLengthCm <= 5.8 and  # i used the output from task 4 irisGetInfo.py to classfiy using the min and max values of the features (sepal width,
    0.1 <= PetalWidthCm <= 0.6 and 1.0 <= PetalLengthCm <= 1.9 ):   # sepal length , petal width , petal length )
    print ("It is Setosa") # output
elif (2.0 <= SepalWidthCm <= 3.4 and 4.9 <= SepalLengthCm <= 6.9 and
    1.0 <= PetalWidthCm <= 1.8 and 3.0 <= PetalLengthCm <= 5.1):
    print ("It is Versi-color") #output
elif (2.2 <= SepalWidthCm <= 3.8 and 4.9 <= SepalLengthCm <= 7.9 and
    1.4 <= PetalWidthCm <= 2.5 and 4.5 <= PetalLengthCm <= 6.9):
    print ("It is Virginica")    #output
else :

    print ("it is undefined")           #output      
#End

"""
SepalLengthCm	SepalWidthCm	PetalLengthCm	PetalWidthCm

5.9	3.2	4.8	1.8
"""