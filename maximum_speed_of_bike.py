'''
Maximum Speed of Bike

An integer N and N integers are passed as input. A bike racing track is numbered with the given N
integers in the order of their occurrence. Also two integers P and Q are passed as input. Whenever
a racer crosses the number P, the speed of the bike is increased by P units per hour. Whenever a racer
crosses the number Q, the speed of the bike is decreased by Q units per hour. Print the maximum speed
achieved during the race. The initial speed of the bike is 40 units per hour.

Boundary Condition(s):

1 <= N <= 50

1 <= P, Q <= 300

Input Format:

The first line contains N, P and Q separated by space(s). The second line contains N integers
separated by space(s).

Output Format:

The first line contains the maximum speed of the bike.

Example Input/Output 1:

Input:

4 20 10

2 20 20 10

Output:

80

Example Input/Output 2:

Input:

5 10 20

20 10 10 10 20

Output:

50

Explanation:

The initial speed of the bike is 40 units per hour.
When 20 is encountered, the speed is decreased to 20 units per hour. 
When 10 is encountered, the speed is increased to 30 units per hour. 
When 10 is encountered, the speed is increased to 40 units per hour. 
When 10 is encountered, the speed is increased to 50 units per hour. 
When 20 is encountered, the speed is decreased to 30 units per hour. 
The maximum speed achieved during the race is 50 units per hour.
'''
n=input().split()
s=input().split()
#using list comphrehension
a=[int(i) for i in s]
p=int(n[1])
q=int(n[2])
speed=40
max=40
for i in range(int(n[0])):
    if a[i]==p:
        speed=speed+a[i]
    elif a[i]==q:
        speed=speed-a[i]
    if max<speed:
        max=speed
print(max)
