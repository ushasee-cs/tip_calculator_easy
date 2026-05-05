print("Welcome to the tip calculator!")
bill = float(input("What is your billing amount?$"))
tip = int(input("What percentage of tip you want to give? 10, 12, 15 "))
people = int(input("How many people to split the bill?"))
tip_as_percentage = tip / 100
total_bill_amount = bill * tip_as_percentage
total_amount = total_bill_amount + bill
bill_per_person = total_amount / people
final_amount = round(bill_per_person, 2)
print(f"Each  person will have to pay $ {final_amount}")
