#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill_value = float(input("What was the total bill? $"))

tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

num_people = int(input("How many people to split the bill? "))
 

tip_val = (bill_value * tip_percentage) /100

total_bill = bill_value + tip_val

bill_each = total_bill/ num_people

bill_each_final = round(bill_each, 2)

print(f"Each person should pay: ${bill_each_final}")