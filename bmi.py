# Feedback pls (SketchyBoi#9799)
#Note: BMI is not an accurate way of determining health since is does not take muscle mass into account.



#Main function, no arguments/parameters
def bmi():
    lbs_or_kgs = str(input("Choose measurement unit (lbs/kgs): "))
    if lbs_or_kgs.lower() == "lbs":
        ft = int(input("Input your height in inches : "))
        lbs = int(input("Input your weight in pounds : "))
        print("Calculating BMI...")
        imp_bmi = (lbs / ft / ft) * 703
        if imp_bmi < 18.5:
            print(f"Your BMI is {imp_bmi}. This is considered underweight.")
        elif imp_bmi >= 18.5 and imp_bmi <= 24.9:
            print(f"Kudos! Your BMI is {imp_bmi}, which is considered a healthy weight.")
        elif imp_bmi >= 25 and imp_bmi <= 29.9:
            print(f"Your BMI is {imp_bmi}. You are therefore considered overweight")
        elif imp_bmi >= 30:
            print(f"Your BMI is {imp_bmi}. This is considered obese")   

    elif lbs_or_kgs.lower() == "kgs":
        height = int(input("Input your height in centimetres : "))  
        weight = int(input("Input your weight in kilograms : "))
        print("Calculating BMI...")
        height_in_metres = height / 100
        met_bmi = weight/(height_in_metres**2)
        if met_bmi < 18.5:
            print(f"Your BMI is {met_bmi}. This is considered underweight.")
        elif met_bmi >= 18.5 and met_bmi <= 24.9:
            print(f"Kudos! Your BMI is {met_bmi}, which is considered a healthy weight.")
        elif met_bmi >= 25 and met_bmi <= 29.9:
            print(f"Your BMI is {met_bmi}. This is considered overweight.")
        elif met_bmi >= 30:
            print(f"Your BMI is {met_bmi}. This is considered obese.")     


bmi()