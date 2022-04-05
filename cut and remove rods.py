'''
Cut and Remove Rods

program must accept N integers representing the length of N rods. A boy cuts the rods into smaller
rods based on the following conditions.

-He finds the length of the shortest rod. Then he cuts that length from each of the longer rods and
then he removes all the pieces of the shortest length. When all the remaining rods are the same length,
they cannot be shortened so he removes those rods.

-He repeats the above process until there are no rods left

The program must print the number of rods remaining before each cutting process.

Boundary Condition(s): 
1 <= N, Length of each rod <= 1000

Input Format: 
The first line contains N.
The second line contains N integers separated by a space representing the length of N rods.

Output Format:

The lines contain the integer values based on the given conditions.

Example Input/Output 1

Input:
6
8 4 2 2 7 8

Output:
6
4
3
2

Explanation:
Here N = 6 and the lengths of the 6 rods are 8 4 2 2 7 8.

Initially, there are 6 rods.
Shortest length = 2 -> 6 2 * * 5 6
Now 4 rods are remaining
Shortest length = 2 -> 4 * * * 3 4
Now 3 rods are remaining 
Shortest length = 3 -> 1 * * * * 1
NOW 2 rods are remaining. Both the rods have the same length, so he removes them.
The asterisks represent the empty spaces,

Example Input/Output 2:
Input:
9
1 2 3 4 5 4 3 2 1

Output:
9
7
5
3
1

'''
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
b=a[:]
print(n)      
j=0
while j<len(b) :
    i=0
    while i<len(b):
        if b[i]!='*':
            min=b[i]
            break
        i=i+1
    if i==len(b):
        break
    #below logic is to find which is minimum
    for i in range(len(b)):
        if b[i]!='*' and b[i]<min:
            min=b[i]
    i=0
    while i<len(b):
        if b[i]!='*':
            b[i]=b[i]-min
        if b[i]!='*' and b[i]==0:
            b[i]='*'
        i=i+1
    count=0
    for i in range(len(b)):
        if b[i]!='*':
            count=count+1
    if count!=0:
        print(count)
    else:
        break
    j=j+1



            
