'''
Next Palindromic Number

An integer N is passed as input. The program must print the immediate next palindromic number of N.

Boundary Condition(s):
1 <= N = 999999999 

Input Format:

The first line contains N

Output Format:

The first line contains the immediate next palindromic number of N.

Example Input/Output 1:

Input:
119

Output:
121

Example Input/Output 2:

Input:
1111

Output:
1221

'''
def next_palindrome(n):
    num=n+1
    while 1:
        rev=0
        temp=num
        #to reverse the number to compare
        while temp:
            rem=temp%10
            rev=rev*10+rem
            temp=temp//10
        if num==rev:
            print('next palindrome number is:',num)
            break
        num=num+1
n=int(input('Enter number: '))
next_palindrome(n)
