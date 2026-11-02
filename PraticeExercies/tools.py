
def findMax(value):
    maxvalue = -1
    for val in value:
        if val > maxvalue:
            maxvalue = val
    return maxvalue
def countOccurances(l,f):
    count = 0
    for val in l:
        if f == val:
            count+=1
    return count
def filterbyvalue(d,t):
    ans = {}
    for key,val in d.items():
        if val >= t:
            ans[key] = val
    return ans
print(findMax([10,20,30]))
print(countOccurances(["a","b","c","a"],"a"))
print(filterbyvalue({"ana":15,"banaa":5},10))