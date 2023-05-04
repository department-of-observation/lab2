def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("bmi is=" + str(bmi))
    if bmi > 25.0:
        print("Over Weight")
        bmi=1
        return bmi

    if bmi >= 18.5 or bmi <= 25:
        print("Normal Weight")
        bmi=0
        return bmi
    if bmi < 18.5:
        print("Under Weight")
        bmi=-1
        return bmi



bmi=calculate_bmi(weight=57, height=1.73)
print("return value is =" + str(bmi))
