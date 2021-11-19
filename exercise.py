# 1  isPalindrome
def is_palindrome(text):
    stringlength = len(text)
    slicedString = text[stringlength::-1]
    if slicedString == text:
        return True
    else:
        return False



print(is_palindrome("aaaaaaaa"))
print(is_palindrome("ravaria"))


#2 minSplit
#variant one 

def minSplit(n, denoms):
    nums = [float('inf') for x in range(n + 1)]
    nums[0] = 0
    for denom in denoms:
        for amount in range(len(nums)):
            if denom <= amount:
                nums[amount] = min(nums[amount], 1 + nums[amount - denom])
    return nums[n] if nums[n] != float('inf') else -1


print(minSplit(93, [1,5,10,20,50]))

print(minSplit(930, [1,5,10,20,50]))


# 3 notContains int

def not_contains_int(array):
    smallest_int = array[0]
    for num in array:
        if num < smallest_int:
            smallest_int = num

            
    new_number = smallest_int - 1
    if new_number != 0 and new_number not in array:
        return new_number
    else:
        print("This array doethnot contains such number!")
    
    


print(not_contains_int([90, 4, 3, 7, 9]))




#4 isProperly

def is_properly(open, close):
    if open == '[' and close == ']':
        return True
    if open == '{' and close == '}':
        return True
    if open == '(' and close == ')':
        return True
    return False


# 5 count variants

def count_variants(n):
    if n <= 2:
        return n

    lookup = [None] * (n + 1)

    lookup[0] = 1
    lookup[1] = 1
    lookup[2] = 2

    for i in range(2, n + 1):
        lookup[i] = lookup[i - 1] + lookup[i - 2]

    return lookup[n]

print("Total ways to reach stears are:", count_variants(4))
    
# 6 delete data structure

















