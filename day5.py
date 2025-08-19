res=[]
def leader_No(n_list):
    n=len(n_list)
    max_element=n_list[-1]
    res.append(max_element)
    for i in range(n-2,-1,-1):
        if n_list[i]>max_element:
            max_element=n_list[i]
            res.insert(0,n_list[i])
            max_element=n_list[i]
    return res

n_list=list(map(int,input().split()))
print(leader_No(n_list))
