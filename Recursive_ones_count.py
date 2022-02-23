'''Recursive Ones Count

The program must accept a string S containing only Os and 1s as the input. The program must print the
number of 1s in the given string S. Then the program must print the number of 1s in the previous result
(i.e., the ones count in the binary representation of the previous result).Then the program must repeat
the process till the number of 1s in the result reaches 1.

Boundary Condition(s):
1 <= Length of S <= 10^6

input Format:

The first line contains S.

Output Format:

The first line contains the integer values separated by a space representing the number of 1s based
on the given conditions.

Example Input/Output 1:

1nput:

1000100101011000101110101111

Output:

15 4 1

Explanation:

Here S="1000100101011000101110101111".
There are 15 ones in the given string S. So 15 is printed.

15 -> 1111-> 4 ones. So 4 is printed.

4 -> 100 > 1 one. So 1 is printed.

Example Input/Output 2:

Input:

1101101111101110111111010

Output:

19 3 2 1 '''

#function to recursive ones count
def count_ones(temp):
    i=0
    count1=0
    while i<len(temp):
        if temp[i]=='1':
            count1=count1+1
        i=i+1
    print(count1,end=' ')
    if count1==1:
        return 0
    num=count1
    count2=0
    #To count the number of base two value present
    while num:
        count2=count2+1
        num=num//2
    num=count1
    i=1
    number=0
    #converting the number into the binary value
    while i<=count2:
        remainder=(num//(2**(count2-i)))%2
        number=number*10+(remainder)
        i=i+1
    return count_ones(str(number))
s=input()
count_ones(s)

#withount using function
print()
temp=s
while 1:
    i=0
    count1=0
    while i<len(temp):
        if temp[i]=='1':
            count1=count1+1 
        i=i+1 
    print(count1,end=' ')
    if count1==1:
        break
    num=count1
    count2=0
    while num:
        count2=count2+1 
        num=num//2 
    num=count1
    i=1 
    number=0
    while i<=count2:
        remainder=(num//(2**(count2-i)))%2
        number=number*10+remainder
        i=i+1 
    temp=str(number)
