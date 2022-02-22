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
