#Check indefinite function to check if Alex can keep 
#playing with the current toys.
def check_ind(E, R):
    E_sum = sum(E)

    time = [i+j for i, j in zip(E, R)]
    indices = []
    
    for i in range(len(E)):
        if E_sum - E[i] < R[i]:
            indices.append(i)
            
    if len(indices)>0:
        idx = time.index(max(time))
        return False, idx
    return True, -1
    


def solve(E, R):
    if len(E)==0:
        return "Sum All"
    
    global count
    
    val, index = check_ind(E, R)
    
    if val:
        return str(count) + " " + "INDEFINITELY"     
    else:
        del E[index]
        del R[index]
        
        count += 1
        
        return solve(E, R)    
        
        
t = int(input())
ans = []

for i in range(t):

    count = 0
    
    n = int(input())
    E, R = [], []
    
    for j in range(n):
        e, r = list(map(int, input().split(" ")))
        E.append(e)
        R.append(r)
        
    res = solve(E.copy(), R.copy())
    
    if res == "Sum All":
        val, index = check_ind(E, R)
        x = sum(E)+sum(E[:index])
        
        ans.append("0 "+str(x))
    else:
        ans.append(res)
        

for i in range(t):
    print("Case #{0}: {1}".format(i+1, ans[i]))
        

        
