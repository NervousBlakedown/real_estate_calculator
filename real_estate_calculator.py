# Real Estate Calculator.
import numpy as np

def get_float_input(prompt, min_value=None):
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a value greater than {min_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_monthly_mortgage_payment(principal, annual_interest_rate, loan_term_months):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    mortgage_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / ((1 + monthly_interest_rate) ** loan_term_months - 1)
    return mortgage_payment

def calculate_pmi(loan_amount, down_payment_percentage, pmi_rate):
    if down_payment_percentage < 20:
        return (pmi_rate / 100) * loan_amount / 12  # PMI rate as a percentage
    return 0

print("\nThanks for using Blake's Real Estate Calculator.\n")

# Input Section with Validation
sales_price = get_float_input("Enter sales price of house in US dollars: ", 0)
down_payment_percentage = get_float_input("Enter down payment as a percentage of sales price: ", 0)
mortgage_years = get_float_input("Enter mortgage length in years: ", 0)
annual_interest_rate = get_float_input("Enter loan interest rate as a percentage: ", 0)
monthly_utilities = get_float_input("Enter estimated monthly utilities amount: ", 0)
monthly_insurance = get_float_input("Enter monthly homeowner insurance amount: ", 0)
monthly_hoa_fees = get_float_input("Enter monthly HOA amount: ", 0)
property_tax_rate = get_float_input("Enter your county's property tax rate as a percentage: ", 0)
pmi_rate_input = get_float_input("Enter PMI rate as a percentage (default is 1%): ", 0)

# Calculation Section
down_payment_amount = sales_price * (down_payment_percentage / 100)
loan_amount = sales_price - down_payment_amount
loan_term_months = int(12 * mortgage_years)

monthly_mortgage_payment = calculate_monthly_mortgage_payment(loan_amount, annual_interest_rate, loan_term_months)
pmi_amount = calculate_pmi(loan_amount, down_payment_percentage, pmi_rate_input)

yearly_property_tax_amount = (property_tax_rate / 100) * sales_price
closing_costs = 0.04 * sales_price  # Assuming 4% closing costs

# Output Section
print(f"\nHouse price: ${sales_price}")
print(f"Down payment: {down_payment_percentage}% or ${down_payment_amount}")
print(f"Loan amount: ${loan_amount}")
print(f"Loan term: {loan_term_months} months or {mortgage_years} years")
print(f"Interest rate: {annual_interest_rate}%")
print(f"Monthly mortgage payment (P&I): ${round(monthly_mortgage_payment, 2)}")
if pmi_amount > 0:
    print(f"Estimated monthly PMI amount (required if down payment < 20%): ${round(pmi_amount, 2)}")
else:
    print("No PMI required (down payment >= 20%).")
print(f"Estimated average monthly utilities: ${monthly_utilities}")
print(f"Monthly homeowner insurance: ${monthly_insurance}")
print(f"Monthly HOA fees: ${monthly_hoa_fees}")
print(f"Yearly property tax: ${yearly_property_tax_amount}")
print(f"Estimated closing costs: ${closing_costs}\n")
print("Happy House Hunting.")
