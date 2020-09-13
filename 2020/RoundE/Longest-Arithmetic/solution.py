ans = []
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))
    
    diff = [(arr[i-1]-arr[i]) for i in range(1, len(arr))]
    if len(diff)==1:
        ans.append(2)
        continue
    
    res = []
    count = 1
    for i in range(1, len(diff)):
        if diff[i]==diff[i-1]:
            count+=1
            if i==len(diff)-1:
                res.append(count)
        else:
            res.append(count)
            count = 1
            if i == len(diff)-1:
                res.append(1)
    
    ans.append(max(res)+1)
    
    
for i in range(len(ans)):
    print("Case #{0}: {1}".format(i+1, ans[i]))
