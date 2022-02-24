'''
Smallest Submatrix - Min and Max Integers

The program must accept an integer matrix of size R*C contain containing only unique integers as the
input. The program must print the smallest possible submatrix having the minimum integer and the
maximum integer in the matrix.

Boundary Condition(s):

2 <= R, C <= 50

1 <= Matrix element value <= 10^4

Input Format:

The first line contains R and C separated by a space. The next R lines, each contains C integer values
separated by a space.

Output Format:

The lines contain the smallest possible submatrix having the minimum integer and and the maximum
integer in the matrix

Example Input/Output 1:

input:

5 6

73 31 19 10 27 12

82 66 15 23 64 89

17 40 74 41 99 38

46 79 91 28 57 35

94 97 45 55 33 56

Output:

10 27

23 64

41 99

Explanation:

The minimum integer in the matrix is 10. The maximum integer in the matrix is 99.
So the smallest submatrix with 10 and 99 is given 2117 So the smallest s below.

10 27

23 64

41 99

Example Input/Output 2:

Input:

8 7

556 808 424 922 560 423 973

219 146 679 906 444 474 185

664 409 294 472 884 377 508

166 386 703 133 768 390 919

715 538 861 840 110 378 102

798 981 130 759 860 769 277

463 940 328 942 313 623 151

514 450 779 883 764 157 733

Output:

538 861 840 110 378 102
981 130 759 860 769 277
'''
row=int(input())
col=int(input())
a=[]
b=[]
for i in range(row):
    b=[]
    for i in range(col):
        b.append(int(input()))
    a.append(b)
min=a[0][0]
max=a[0][0]
i1=0
i2=0
i3=0
i4=0
i=0
j=0
while i<row:
    j=0
    while j<col:
        if a[i][j]>max:
            max=a[i][j]
            i3=i
            i4=j
        if a[i][j]<min:
            min=a[i][j]
            i1=i
            i2=j
        j=j+1
    i=i+1
if(i1>i3):
    temp=i1
    i1=i3
    i3=temp
if i2>i4:
    temp=i2
    i2=i4
    i4=temp

i=i1
while i<=i3:
    j=i2
    while j<=i4:
        print(a[i][j],end=' ')
        j=j+1
    print()
    i=i+1








