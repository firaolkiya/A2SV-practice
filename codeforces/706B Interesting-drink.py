n = int(input())
shop = list(map(int,input().split()))
shop.sort()
def ablityCalc(ablity):
    left,right,best=0,n-1,-1
    while left<=right:
        mid=(left+right)//2
        if shop[mid]>ablity:
            right=mid-1
        else:
            best=mid
            left=mid+1
    return best+1

days=int(input())
for _ in range(days):
    ablity = int(input())
    print(ablityCalc(ablity))
