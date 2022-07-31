'''
Sort Numbers - Factor Count

The program must accept N positive integers as the input and sort them based on the factor count the
factor counts have(lowest to highest factor count). If two numbers have the same factor count, order
based on the value of the numbers in the ascending order.

Input Format:

The first line will contain N. 

The second line will contain N positive integers separated by a space. 

Output Format:

The first line will contain the N positive integers(separated by a space) ordered by their factor count.

Boundary Conditions.

2 <= N = 10000

Example Input/Output 1:

Input:
5

18 23 100 1200 45

Output:

23 18 45 100 1200

Example Input/Output 2:

Input:
3

29 11 101

Output:

11 29 101
'''


n=int(input('Enter a size: '))
s=input('Enter N numbers: ').split()
a=[int(i) for i in s]
#To find the factors of given N numbers and store in 'b' list
b=[]
for i in a:
    j=1
    factors_count=0
    while j<=i:
        if i%j==0:
            factors_count+=1
        j+=1
    b.append(factors_count)
#find the duplicates in the factors and store in new list 'c'
c=[]
for i in range(n):
    j=0
    while j<i:
        if b[j]==b[i]:
            break
        j+=1
    if j==i:
        c.append(b[i])
#sor the list c (duplicate removed)
for i in range(len(c)-1):
    for j in range(i+1,len(c)):
        if c[i]>c[j]:
            temp=c[i]
            c[i]=c[j]
            c[j]=temp

i=0 
#duplicate removed and sorted 'c' list compared with 'b' list contains factors of a numbers in 'a' list
print('sorted numbers by factors count')
while i<len(c):
    d=[]
    j=0
    #'c' list matched with 'b' list using this, index is used to append the number in 'a' list
    while j<n:
        if b[j]==c[i]:
            d.append(a[j])
        j=j+1
    #sort the 'd' list appended the numbers of 'a' list
    for k in range(len(d)-1):
        for l in range(k+1,len(d)):
            if d[k]>d[l]:
                temp=d[k]
                d[k]=d[l]
                d[l]=temp
    for m in d:
        print(m,end=' ')
    i=i+1
        
        
    


