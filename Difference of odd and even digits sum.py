'''
Difference of Odd and Even Digits Sum

Given an integer N, the program must print the absolute difference of the sum of odd digits and sum
30282 of even digits.

Input Format:

The first line contains S.

Output Format:

The first line contains the output as specified.

Example Input/Output 1:

Input: 12345

Output:

|((1+3+5)-(2+4))|=3

Input/Output 2:

Input:

89235

Output:

7

Explanation:

|(8+2)-(9+3+5)|=7'''

n=int(input('Enter number: '))
odd=even=0
temp=n
while temp:
    rem=temp%10
    if rem%2==1:
        even=even+rem
    else:
        odd=odd+rem
    temp=temp//10
if even>odd:
    print('difference is',even-odd)
else:
    print('difference is',odd-even)
        
