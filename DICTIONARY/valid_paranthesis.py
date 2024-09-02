# # Taking input from the user
# user_input = input("Enter a string with parentheses to check: ")

# stack = []
# # Dictionary to keep track of matching pairs
# matching_parentheses = {')': '('}

# is_valid = True  # Flag to indicate if the parentheses are valid

# for char in user_input:

#     if char in matching_parentheses.values():

#         stack.append(char)

#     elif char in matching_parentheses.keys():

#         if stack == [] or stack.pop() != matching_parentheses[char]:

#             is_valid = False

#             break

# if stack != []:
    
#     is_valid = False

# if is_valid:
#     print("The parentheses are balanced and valid.")
# else:
#     print("The parentheses are not balanced or valid.")



user_input="["

symbol_table={
        "<":">",
        "[":"]",
        "(":")",
        "{":"}"
    }
stack=[]
top=-1
is_valid=True
for symbol in user_input:
    if symbol in symbol_table:
        top+=1
        stack.append(symbol)
    else:
        if len(stack)<1:
            is_valid=False
            break    
        current_symbol=stack[top]
        current_symbol_closing=symbol_table[current_symbol]
        if symbol==current_symbol_closing:
            stack.pop()
            top-=1
        else:
            is_valid=False
            break
if len(stack)!=0:
    print(False)
else:
    print(is_valid)    

