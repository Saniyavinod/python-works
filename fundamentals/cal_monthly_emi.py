# loan_amout
# tenure 
# interest rate


loan_amount=200000   #p

annual_interest_rate=9  #R

tenure_year=10 #T

monthly_interest_rate=annual_interest_rate/(12*100)    #covert annual interest to monthly =r

monthly_installment=tenure_year*12    #converst tenure year to monthly installment=t

emi=(loan_amount*monthly_interest_rate*(1+monthly_interest_rate)**monthly_installment)/((1+monthly_interest_rate)**monthly_installment-1)
#for calculating emi : (p*r*(1+r)**t)/(1+r)**t)-1)

#total amount paid over loan tenure

total_amount_paid=emi-monthly_installment
print(f"total amount paid={total_amount_paid}")

#total interest payable
total_interest_payable=total_amount_paid-loan_amount
print(f"total interest payable={total_interest_payable}")

print(f"monthly emi is:{emi}")