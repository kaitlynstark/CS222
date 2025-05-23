#Part 1- BMI Calculator
def calculate_bmi(weight, height):
    bmi = (weight * 703) / (height ** 2)
    return bmi

weight = float(input("Enter weight in lbs: "))
height = float(input("Enter height in inches: "))
result = calculate_bmi(weight, height)
print("Your BMI is: ", result)

if result < 18.5:
    print("Based on your BMI, you are underweight.")
elif 18.5 <= result < 25:
    print("Based on your BMI, you are a normal weight.")
elif result >= 25:
    print("Based on your BMI, you are overweight.")

calculate_bmi(weight, height)

#Part 2 - Sum of All Even Numbers Between 2 and 100
def sum_even_numbers():
    total=0
    for number in range(2, 101, 2):
        total += number
    print("The sum of all even numbers from 2 to 100 is:", total)
# The sum should be 2250
sum_even_numbers()

#Part 3 - Sum of All Odd Numbers Between a and b
def sum_odd_numbers(a,b):
    total = 0
    for number in range(a, b + 1):
        if number % 2 != 0:
            total += number
    print("The sum of all odd numbers between a and b is:", total)
a = int(input("Enter the starting number (a): "))
b= int(input("Enter the ending number (b): "))
sum_odd_numbers(a,b)

#Part 4 - Stock Price
def stock_price_checker():
    target_price = float(input("Enter the target price: "))

    while True:
        current_price = float(input("Enter the current stock price: "))
        if current_price >= target_price:
            print("Shares can be sold now.")
            break
        else:
            print("Shares cannot be sold yet. Current price is below target price.")
stock_price_checker()

#Part 5 - Tuition
def projected_tuition():
    tuition = 8000.00
    increase_rate = 0.03

    for year in range (1, 6):
        tuition += tuition * increase_rate
        print("Projected tuition is: $", round(tuition, 2))
projected_tuition()