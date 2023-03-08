def solve(numlegs, numheads):
    for i in range(1, numheads+1):
        if (i*4)+(numheads-i)*2 == numlegs:
            ans=f"{i} rabbits,{numheads-i} chickens"
            return ans
numlegs=int(input())
numheads=int(input())
print(solve(numlegs,numheads))