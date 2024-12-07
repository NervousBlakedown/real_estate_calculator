import locale
locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')  # Set locale for GBP formatting



def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in {"yes", "no"}:
            return response == "yes"
        print("Invalid input. Please type 'yes' or 'no'.")


def get_float_input(prompt, min_value=None, default=None):
    while True:
        try:
            value = input(prompt + (f" (default: {default}): " if default is not None else ": "))
            if not value and default is not None:
                return float(default)
            value = float(value)
            if min_value is not None and value < min_value:
                print(f"Please enter a value greater than {min_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def format_currency(amount):
    """
    Format the amount as GBP with no decimal places.
    """
    return locale.currency(round(amount), grouping=True)

def calculate_monthly_mortgage_payment(principal, annual_interest_rate, loan_term_months):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    if monthly_interest_rate == 0:
        return principal / loan_term_months  # Handle 0% interest rate
    return principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / \
           ((1 + monthly_interest_rate) ** loan_term_months - 1)

def calculate_stamp_duty(price, first_time_buyer):
    # UK Stamp Duty Land Tax Rates
    if first_time_buyer and price <= 425000:
        return 0
    thresholds = [(0, 0), (250000, 5), (925000, 10), (1500000, 12)]
    tax = 0
    for i, (limit, rate) in enumerate(thresholds):
        if price <= limit or i == len(thresholds) - 1:
            tax += (price - thresholds[i - 1][0]) * rate / 100
            break
        tax += (limit - thresholds[i - 1][0]) * rate / 100
    return tax

print("\nWelcome to Blake's UK Real Estate Calculator, Bruv.\n")

# Input Section
sales_price = get_float_input("Enter sales price of the house in GBP", 0)
first_time_buyer = get_yes_no_input("Are you a first-time buyer? (yes/no): ")
down_payment_percentage = get_float_input("Enter down payment as a percentage of sales price", 5, default=10)
mortgage_years = get_float_input("Enter mortgage length in years", 5, default=25)
annual_interest_rate = get_float_input("Enter loan interest rate as a percentage", 0, default=4)
monthly_utilities = get_float_input("Enter estimated monthly utilities in GBP", 0, default=200)
monthly_insurance = get_float_input("Enter monthly homeowner insurance in GBP", 0, default=50)
solicitor_fees = get_float_input("Enter solicitor/conveyancing fees in GBP", 0, default=1500)
land_registry_fees = get_float_input("Enter land registry fees in GBP", 0, default=500)
council_tax = get_float_input("Enter monthly council tax in GBP", 0, default=150)

# Calculation Section
down_payment_amount = sales_price * (down_payment_percentage / 100)
loan_amount = sales_price - down_payment_amount
loan_term_months = int(12 * mortgage_years)
monthly_mortgage_payment = calculate_monthly_mortgage_payment(loan_amount, annual_interest_rate, loan_term_months)

stamp_duty = calculate_stamp_duty(sales_price, first_time_buyer)
closing_costs = solicitor_fees + land_registry_fees

# Output Section
print("\n--- Calculation Results ---\n")
print(f"House price: {format_currency(sales_price)}")
print(f"Down payment: {down_payment_percentage}% or {format_currency(down_payment_amount)}")
print(f"Loan amount: {format_currency(loan_amount)}")
print(f"Loan term: {loan_term_months} months or {mortgage_years} years")
print(f"Interest rate: {annual_interest_rate}%")
print(f"Monthly mortgage payment: {format_currency(round(monthly_mortgage_payment, 2))}")
print(f"Estimated monthly utilities: {format_currency(monthly_utilities)}")
print(f"Monthly homeowner insurance: {format_currency(monthly_insurance)}")
print(f"Monthly council tax: {format_currency(council_tax)}")
print(f"Stamp Duty Land Tax: {format_currency(stamp_duty)}")
print(f"Solicitor/conveyancing fees: {format_currency(solicitor_fees)}")
print(f"Land registry fees: {format_currency(land_registry_fees)}")
print("\n--- Total Estimated Costs ---")
total_closing_costs = closing_costs + stamp_duty
print(f"Total closing costs (upfront): {format_currency(round(total_closing_costs, 2))}")
print("\nHappy House Hunting, Bruv!\n")
