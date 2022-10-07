'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXMCcO16Vi8DFAWv&categoryId=AXMCcO16Vi8DFAWv&categoryType=CODE
Date : 2020-07-22
Memo :
'''
#%%
T = int(input())
for test_case in range(1, T+1):
    print("#%d " % (test_case), end="")
    j_happiness = 0
    h_happiness = 0
    dishes = int(input())
    dishes_happiness = dict()
    for d in range(dishes):
        a,b = map(int,input().split())
        dishes_happiness[d] = [a,b]
    j_dishes_happiness = {k:v[0] for k,v in sorted(dishes_happiness.items(),key=lambda x : (x[1][0],x[1][1]),reverse=True)}
    h_dishes_happiness = {k:v[1] for k,v in sorted(dishes_happiness.items(),key=lambda x : (x[1][1],x[1][0]),reverse=True)}

    for d in range(dishes):
        if d % 2 == 0 :
            k = next(iter(j_dishes_happiness))
            j_happiness += j_dishes_happiness[k]
            del j_dishes_happiness[k]
            del h_dishes_happiness[k]
        else :
            k = next(iter(h_dishes_happiness))
            h_happiness += h_dishes_happiness[k]
            del j_dishes_happiness[k]
            del h_dishes_happiness[k]
    print(j_happiness - h_happiness)


# %%

# %%


# %%
