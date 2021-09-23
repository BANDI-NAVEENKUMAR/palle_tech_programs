n=int(input())
sup777exams=0
for a in range(1,n+1):
    for b in range(1,n+1):
        sanket=n-a*b
        if(sanket<1):
            continue
        if(a*b+sanket==n):
            sup777exams+=1
print(sup777exams)