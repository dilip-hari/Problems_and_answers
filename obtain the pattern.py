'''
''ZOHO interview question''

Understand the below pattern and obtain the output.

input1:
5

output1:
    1
   121
  12321
 1234321
123454321

input2:
7

output2:
      1
     121
    12321
   1234321
  123454321
 12345654321
1234567654321

'''
def pattern(n):
    i=1
    while i<=n:
        a=[]
        j=1
        while j<=n-i:
            print(" ",end='')
            j=j+1
        j=1
        while j<=i:
            print(j,end='')
            a.append(j)
            j=j+1
        k=len(a)-2
        while k>=0:
            print(a[k],end='')
            k=k-1
        print()
        i=i+1
pattern(int(input()))

