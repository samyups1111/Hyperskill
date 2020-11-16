import math

def months_to_years(months):
    years = 0
    if months < 12 and years == 0:
        return f"{months} months"
    else:
        while months >= 12:
            months -= 12
            years += 1
        return f"It will take {years} years and {months} months to repay this loan!"

def n_monthly_payments():
    loan_principal = int(input("Enter the loan principal:\n"))
    monthly_payment = float(input("Enter the monthly payment:"))
    loan_interest = float(input("Enter the loan interest:\n")) / 1200
    months = math.log((monthly_payment / (monthly_payment - (loan_interest * loan_principal))), 1 + loan_interest)
    exact_months = math.ceil(months)
    print(exact_months)
    return months_to_years(exact_months)

def monthly_payment():
    loan_principal = int(input("Enter the loan principal:\n"))
    months = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n")) / 1200
    monthly_payment = loan_principal * ((loan_interest * ((1 + loan_interest)**months)) / (((1 + loan_interest)**months)-1))
    return f"Your monthly payment = {math.ceil(monthly_payment)}!"

def loan_principal():
    monthly_payment = float(input("Enter the annuity payment:\n"))
    months = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n")) / 1200
    loan_principal = monthly_payment / ((loan_interest * ((1 + loan_interest)**months)) / (((1 + loan_interest)**months) - 1))
    return f"Your loan principal = {loan_principal}!"

print('What do you want to calculate?\ntype "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
choice = input('type "p" for loan principal:\n')

if choice == "n":
    print(n_monthly_payments())
elif choice == "a":
    print(monthly_payment())
elif choice == "p":
    print(loan_principal())
