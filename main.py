#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total = float(input("What is the total bill? $"))
percent = float(input("What percentage tip would you like to give? 15, 20, or 25? "))
people = float(input("How many people are splitting the bill? "))

price_per_person = "{:.2f}".format(total * ((percent/100+1))/people)

print(f"Each person should pay: ${price_per_person}")