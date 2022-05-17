# Real Estate Calculator.
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sb
import numpy as np
print("\n")

print("Thanks for using Blake's Real Estate Calculator.")
print("")

sales_price = float(input("Enter sales price of house in US dollars (without commas), then hit the return key: "))
down_payment =  float(input("Enter down payment as a percentage of Sales Price, e.g. '5' for 5%, then hit the return key: "))
down_payment_dollars = down_payment * (sales_price / 100)

remaining_loan_amount = sales_price * (1 - down_payment / 100)
pmi_rate = (0.01 * remaining_loan_amount) / 12 # 1%; average pmi rate ranges from .55% to 2.25%; median is 1.2%

Loan_Amount = sales_price*(1-down_payment/100)
Mortgage_Type =  float(input("Enter mortgage length in years, e.g. '15' for 15 years, then hit the return key: "))

Loan_Term = int(12 * Mortgage_Type)
yearly_loan_term = Loan_Term / 12

Interest_Rate =  float(input("Enter loan interest rate as a percentage, e.g. '4' for 4%, then hit the return key: "))
R = 1 +(Interest_Rate)/(12*100)
X = Loan_Amount*(R**Loan_Term)*(1-R)/(1-R**Loan_Term)

utilities = float(input("Enter estimated monthly utilities amount: "))

homeowner_insurance = float(input("Enter monthly homeowner insurance amount: "))
hoa = float(input("Enter monthly HOA amount: "))

property_tax = float(input("Enter your county's property tax rate, e.g. '3' for 3%, then hit the return key: "))
yearly_property_tax = property_tax * (sales_price / 100)

yearly_homeowner_insurance = homeowner_insurance * 12
yearly_hoa = hoa * 12

closing_cost = .04 * sales_price

Monthly_Interest = []
Monthly_Balance  = []

for i in range(1, Loan_Term + 1):
    Interest = Loan_Amount * (R - 1)
    Loan_Amount = Loan_Amount - (X - Interest)
    Monthly_Interest = np.append(Monthly_Interest, Interest)
    Monthly_Balance = np.append(Monthly_Balance, Loan_Amount)

# Print those sweet, sweet outputs.
print("\n")

print("House price: " + str('$')+ str(sales_price))
print("Down payment: " + str(down_payment) + str('%') + ", or " + str('$') + str(down_payment_dollars))
print("Loan length: " + str(Loan_Term)+str(' months') + ", or " + str(yearly_loan_term) + " years")
print("Interest rate on the annual percentage basis: " + str(Interest_Rate)+str('%'))
print("Remaining loan amount: " + str('$') + str(sales_price*(1-down_payment/100)))
print("Total interest paid over life cycle of loan: " + str('$') + str(np.round(np.sum(Monthly_Interest), 0)))

print("") # print() or print("") does a single space instead of a double space.
print("Monthly mortgage payment (P & I): " + str('$')+str(np.round(X, 0)))
print("Est. avg. monthly utilites amount: " + str('$') + str(utilities))
print("Monthly homeowner insurance amount: " + str('$') + str(homeowner_insurance))
print("Monthly HOA amount: " + str('$') + str(hoa))

if down_payment < 20:
    print("Est. monthly PMI amount at 1% rate (required if down payment < 20%): " + str('$') + str((np.round(np.sum(pmi_rate), 0))))
else:
    print("You owe no PMI since your down payment is twenty percent or greater. Congrats!")
# print("Your monthly PMI amount (required if down payment < 20%) is " + str('$') + str(pmi_rate * (remaining_loan_amount / 12)))

print("")
print("Yearly homeowner insurance amount: " + str('$') + str(yearly_homeowner_insurance))
print("Yearly HOA amount: " + str('$') + str(yearly_hoa))
print("Yearly property tax amount: " + str('$') + str(yearly_property_tax))
print("Closing cost: " + str('$') + str(closing_cost)) # avg. est. 4% of house cost

print("") # line break. "\n" does double-space.
print("Happy House Hunting.")

# print("\n")
# print("Your total amount for each month on this house is " + str('$') + str(yearly_hoa) + str(yearly_property_tax))
# Visualization if you'd like
# plt.plot(range(1,Loan_Term+1),Monthly_Interest, 'r',lw=2)
# plt.xlabel('month')
# plt.ylabel('monthly interest ($)')
# plt.show()
#
# plt.plot(range(1,Loan_Term+1),Monthly_Balance,'b',lw=2)
# plt.xlabel('month')
# plt.ylabel('monthly loan balance ($)')
# plt.show()
