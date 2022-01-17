# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

cur_age = int(age)

life_years = 90-cur_age
life_months = life_years *12
life_weeks = life_years *52
life_days = life_years *365

print(f"You have {life_days} days, {life_weeks} weeks, and {life_months} months left.")