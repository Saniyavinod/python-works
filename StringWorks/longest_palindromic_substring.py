text="RACECAR"

longest_palindrom=""

for i in range(0,len(text)):

    left=i
    right=i

    while(left >=0 and right <len(text) and text[left]==text[right] ):

        left=left-1
        right=right+1

        current_palindrom=text[left:right+1]

        if len(current_palindrom) > len(longest_palindrom):

            longest_palindrom=current_palindrom

print(longest_palindrom)       