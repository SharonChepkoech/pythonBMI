# height = input("enter your height in m:")
# weight = input("enter your weight in kg:")

# bmi= (weight_as_int/height_as_float*height_as_float) 
# print(bmi_as_int)
height = input("enter your height in m:")
weight = input("enter your weight in kg:")

# bmi= (weight_as_int/height_as_float*height_as_float) 
bmi= float(weight)/float(height) **2


# bmi= round(weight/height **2)
if bmi < 18.5:  
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:  
    print(f"Your bmi is {bmi}, you are clinically obese.")
