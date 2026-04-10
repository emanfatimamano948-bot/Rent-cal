## Inputs we need from the user
# total rent
# total food ordered for snacking
# Charge per unit
## output
# Person living in room/flat
# electricity unit spend
# Total amount you have to pay is

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food order = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
person = int(input("Enter the persson of living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill)// person

print("Each person will pay = ", output)