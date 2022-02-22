'''function getintegersWith Same Ends

The function/method getIntegersWithSame Ends  . accepts two arguments str and K. The first argument str
represents a string value containing only digits. The second argument K represents an integer value.

The function/method getintegersWithSame Ends must form all possible K-digit integers with the
same must for ends using the consecutive digits in the given string. Then the program must return an
array of integers  containing the resulting K-digit integers in sorted order. If there is no such
K-digit integer, then the  function must return an array of size 1 with the value as -1.

Note: K-digit integers do not have leading zeroes.

Your task is to implement the function getIntegersWithSameEnds so that it passes all the test cases.


Boundary Condition(s):

1 <= Length of S<= 100

2 <= K <= 9

Example Input/Output 1:

Input:

508562102042022

4

Output:

2022 2042 2102 5085

Explanation:

Here K = 4.

The 4-digit integers with the same ends that can be formed from the string are given below.

5085, 2102, 2042 and 2022

After sorting the 4-digit integers, the integers become

2022 2042 2102 5085

Example Input/Output 2:

Input:

909086733834444

3

Output:

383 444 444 909

Example Input/Output 3:
Input:

909086733834
5

Output:

-1'''
def integer_with_same_ends(n,k):
    i=0
    a=[]
    while i<len(n):
        num=0
        j=i+(k-1)
        if j<len(n) and n[i]==n[j] and n[i]!='0':
            m=i
            while m<=j:
                num=num*10+(int(n[m]))
                m=m+1
            a.append(num)
        i=i+1
    if len(a)==0:
        return -1
    else:
        i=0
        #sorting the list
        while i<len(a)-1:
            j=i+1
            while j<len(a):
                if a[i]>a[j]:
                    #swapping without using temporary variable
                    a[i]=a[i]+a[j]
                    a[j]=a[i]-a[j]
                    a[i]=a[i]-a[j]
                j=j+1
            i=i+1
        return a
print(integer_with_same_ends(n=input(),k=int(input())))
