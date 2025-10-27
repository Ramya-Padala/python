#Interview Question From GE
def find_anagram(string1,string2):
    if len(string1) == len(string2):
        string1_list = list(string1)
        for x in string2:
            if x in string1_list:
                pass
            else:
                #print(f'Both {string1} and {string2} are NOT anagrams')
                return (f'Both {string1} and {string2} are NOT anagrams')
    else:
        return (f'Both {string1} and {string2} are NOT anagrams')
    return (f'Both {string1} and {string2} are anagrams')

#Interview Question From GE
def factorial(n):
    for i in range(1,n):
        n = n * i
    return n

