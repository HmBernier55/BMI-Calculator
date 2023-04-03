def get_patient_weight():
    print('BMI Calculator')
    print('Patient WEIGHT')
    print('Enter the weight followed by a space and then units of kg or lb.')
    print('kg = kilograms & lb = pounds')
    print('Example: 45 kg    45 lb')
    patient_weight = input("Enter the patient's weight: ")
    return patient_weight

def get_patient_height():
    print('Patient HEIGHT')
    print('Enter the height followed by a space and then units of in or m.')
    print('in = inches & m = meters')
    print('Example: 72 in    2.2 m')
    patient_height = input("Enter the patient's height: ")
    return patient_height

def convert_weight_kg(input_weight):
    weight_data = input_weight.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight/2.205
    return weight

def convert_height_m(input_height):
    height_data = input_height.split(" ")
    height = float(height_data[0])
    units = height_data[1]
    if units == "in":
        height = height*0.0254
    return height

def bmi_calculation(weight, height):
    bmi = weight/(height**2)
    if bmi < 18.5:
        classification = "underweight"
    elif 18.5 <= bmi < 25:
        classification = "normal weight"
    elif 25 <= bmi < 30:
        classification = "overweight"
    else:
        classification = "obese"
    return bmi, classification

def output_results(bmi, classification, weight, height):
    print("BMI Index and Classification")
    print("For a patient weighing {:.1f} kg and is {:.1f} meters tall,".format(weight,height))
    print(" their BMI is {:.1f} kg/m^2 and they are considered {}.".format(bmi,classification))

def bmi_driver():
    weight_input = get_patient_weight()
    height_input = get_patient_height()
    weight = convert_weight_kg(weight_input)
    height = convert_height_m(height_input)
    bmi, classification = bmi_calculation(weight, height)
    output_results(bmi, classification, weight, height)

if __name__ == '__main__':
    bmi_driver()