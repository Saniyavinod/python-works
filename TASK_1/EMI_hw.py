loan_amount=int(input("Enter the loan amount:"))

Tenure=int(input("Enter the tenure in year:"))

interest_rate_annual=int(input("Enter the annual interest rate:"))

Tenure_monthly=Tenure*12

monthly_intrest_rate=interest_rate_annual/12/100

EMI=(loan_amount*monthly_intrest_rate*(1+monthly_intrest_rate)**Tenure_monthly)/((1+monthly_intrest_rate)**Tenure_monthly-1)

print(f"EMI={EMI}")

#total amount paid over loan tenure

total_amount_paid=EMI-Tenure_monthly

print(f"total amount paid={total_amount_paid}")

#total interest payable
total_interest_payable=total_amount_paid-loan_amount

print(f"total interest payable={total_interest_payable}")