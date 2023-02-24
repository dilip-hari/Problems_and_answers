'''
string_first_and_last_reverse:
the given string first and last letter must be replace by first with last one amd last one with first one

input:
I came to the original solution when I was working on a fuzzy search
 
output:
I eamc ot eht lriginao nolutios nhew I saw gorkinw no a yuzzf hearcs

'''
s=input().split()
for i in range(len(s)):
    n=len(s[i])
    if n>1:
        print(s[i][n-1],end='')
        for j in range(1,n-1):
            print(s[i][j],end='')
        print(s[i][0],end='')
    else:
        print(s[i][0],end='')
    if i<len(s)-1:
        print(' ',end='')

