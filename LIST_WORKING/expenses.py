expense=[12000,13000,11000,14000,15000,21000,22000,13000]

#print the count of list

total_expense=0

expense_count=len(expense)

print(expense_count)

#print all expenses
# for i in range(0,expense_count):

#     print(expense[i])

    

#print expenses>15000

for i in range(0,expense_count):
    

        if expense[i]>15000:
            print(expense[i])

        total_expense=total_expense+expense[i]
print(total_expense)


avg_expenses=total_expense/expense_count

print(avg_expenses)



# 
  