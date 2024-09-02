#create a function is_palidrome(word) return true if word is a palindromic string 
#else return false


# def is_palindrome(str):
#     if str[::-1]==str:
#         return True
#     else:
#         return False
# print(is_palindrome("madam"))   



# def is_palindrome(word):
#     reveresed_word=word[::-1]
#     return word==reveresed_word
# print(is_palindrome("madam"))

def reverse(word):
    reverse_word=word[::-1]
    return reverse_word
print(reverse("hlloo"))