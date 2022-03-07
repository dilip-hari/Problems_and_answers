'''
function reduceCharacterFrequency

The function/method reduceCharacterFrequency accepts two arguments str and K representing a string
value and an integer value respectively.

The function/method reduceCharacterFrequency must remove the characters after their Kth occurrence in
the given string(from left to right). Then the function must return the revised string as a new string.

Your task is to implement the function reduceCharacterFrequency so that the program runs successfully.


Example Input/Output 1:
aabbabcdccbab

Output:
aabbcdc

Explanation:

Here the given string is aabbabcdccbab and K=2. After removing the characters that occur more
than 2 times in the given string, the string becomes aabbcdc.


Example Input/Output 2:

Input:
TOOLONGTOURtoolongtour


Output:
TOOLNGTURtoolngtur


'''
def reduceCharacterFrequency(s):
    i=0
    while i<len(s):
        j=0
        while j<i:
            if s[i]==s[j]:
                break
            j=j+1
        if j==i:
            print(s[i],end='')
        else:   
            k=j+1
            while k<i:
                if s[k]==s[i]:
                    break
                k=k+1
            if k==i:
                print(s[i],end='')

        i=i+1
s=input()
reduceCharacterFrequency(s)
