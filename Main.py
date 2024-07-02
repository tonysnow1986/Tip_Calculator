# Prints the name of the application
print("Welcome to the Timmy's Tip Calculator!")
# the variable bill return the input as a float
bill = float(input("What's your bill total? $"))
# tip returns an integer input of the percentage the tip will be
tip = int(input("How generous will your tip be? "))
# returns an integer of how many people are on the bill
people = int(input("How many people on the bill?"))
# The tip included in the bill
# bill_with_tip = tip / 100 * bill + bill
# the tip divided by 100
tip_as_percent = tip / 100
# it takes the bill, and multiply it times the tip_as _percent variable
total_tip_amount = bill * tip_as_percent
# the total bill adds the bill to the total tip amount
total_bill = bill + total_tip_amount
# this variable divides the bill by how many people are accounted for
bill_per_person = total_bill / people
# rounds the number by 2 decimal places
# final_amount = round(bill_per_person, 2)
# formatting the final amount to display the second decimal number
final_amount = "{:.2f}".format(bill_per_person)
# print the result
print(f"Each person split is ${final_amount}")
