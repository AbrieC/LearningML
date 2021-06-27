# To make it easier and faster, the user will enter only petal length and width
PetalLength = float(input("Enter the Petal Length in Cm: "))
PetalWidth = float(input("Enter the Petal Width in Cm: "))

# From statistic: we use the max and min values
if 1.9 >= PetalLength >= 1 and 0.6 >= PetalWidth >= 0.1:
    print("The species is Setosa")
elif (4.4 >= PetalLength >= 3 and 1.3 >= PetalWidth >= 1)\
        or (4.5 > PetalLength >= 3 and 1.8 >= PetalWidth >= 1)\
        or (5.1 > PetalLength > 3 and 1.4 > PetalWidth >= 1):
    print("The species is Versicolor")
elif (6.9 >= PetalLength >= 5.2 and 2.5 >= PetalWidth >= 1.9)\
        or (6.5 >= PetalLength > 5.1 and 2.5 >= PetalWidth > 1.4)\
        or (6.5 >= PetalLength > 4.5 and 2.5 >= PetalWidth > 1.8):
    print("The species is Virginica")

# Now, the rang of petal length (4.5-5.1) and petal width (1.4-1.8)
# is a common area between Versicolor and Virginica
# Therefore we need more info from the user
# The user will enter the values of Sepal length and width

else:
    SepalWidth = float(input("Enter the Sepal Width in Cm: "))
    ##From statistic: we use the max and min values
    if 2.2 > SepalWidth >= 2:
        print("The species is Versicolor")
    elif 3.8 >= SepalWidth > 3.4:
        print("The species is Virginica")
    elif 3.4 >= SepalWidth >= 2.2:
        SepalLength = float(input("Enter the Sepal Length in Cm: "))
        if 7.9 >= SepalLength > 7:
            print("The species is Virginica")
        else:
            print("The species could be Versicolor or Virginica")
    else:
        print("Undefined Species")



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
