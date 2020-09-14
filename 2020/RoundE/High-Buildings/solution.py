ans = []
t = int(input())
for i in range(t):
    n, a, b, c = list(map(int, input().strip().split()))
    if n==1:
        if a==1 and b==1 and c==1:
            ans.append([1])
        else:
            ans.append("IMPOSSIBLE")
        continue
        
    if n==2:
        if c==1 and a==1 and b==2:
            ans.append([2,1])
        elif c==1 and a==2 and b==1:
            ans.append([1,2])
        else:
            ans.append("IMPOSSIBLE")
    
    if (a+b-c)>n:
        ans.append("IMPOSSIBLE")
        continue
    common = [n]*c
    hide = n-(a+b-c)
    res = []

    if c>1:
        left = [n-1]*(a-c)
        hidden = [1]*(n-(a+b-c))
        right = [n-1]*(b-c)
        res = left+common[:1]+hidden+common[1:]+right
        ans.append(res)
    else:
        if hide==0:
            left = [n-1]*(a-1)
            right = [n-1]*(b-1)
            res = left+common+right
            ans.append(res)
        else:
            if a>1 or b>1:
                left = [n-1]*(a-1)
                hidden = [1]*hide
                right = [n-1]*(b-1)
                res = left+common+right
                res = res[:1]+hidden+res[1:]
                ans.append(res)
                continue
            
            else:
                ans.append("IMPOSSIBLE")           
        
        
        
for i in range(len(ans)):
    if type(ans[i])==list:
        print("Case #{0}: {1}".format(i+1, " ".join([str(i) for i in ans[i]])))
    else:
        print("Case #{0}: {1}".format(i+1, ans[i]))
