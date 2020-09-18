t = int(input())
ans = []

for i in range(t):
    n, bud = list(map(int, input().strip().split(" ")))
    
    prices = list(map(int, input().strip().split(" ")))
    
    prices.sort()
    
    houses = 0
    cost = 0
    
    for price in prices:
        if cost < bud:
            houses+=1
            cost+=price
    
    if cost>bud:
        houses-=1
    ans.append(houses)
    
for i in range(1,t+1):
    print("Case #{0}: {1}".format(i, ans[i-1]))
        
