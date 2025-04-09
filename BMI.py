from colorama import Fore,Style,init
init()
def cal_BMI(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def comp_BMI(bmi):
    if bmi < 18.5:
        return Fore.GREEN + "Underweight"
    elif 18.5 <= bmi < 24.9:
       return Fore.GREEN + "Normal weight"
    elif 25 <= bmi < 29.9:
       return Fore.GREEN + "Overweight"
    else:
        return Fore.GREEN + "Obese"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = cal_BMI(weight, height)
status = comp_BMI(bmi)

print(f"\n\tYour Body Mass Index is: {Fore.MAGENTA}{bmi:.2f}{Style.RESET_ALL}")
print(f"\tYour Health Status: {status}{Style.RESET_ALL}")