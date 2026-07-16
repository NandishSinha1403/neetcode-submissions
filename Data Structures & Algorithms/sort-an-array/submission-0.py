class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return divide(nums, 0, len(nums)-1)
        
def divide(A, p , r ):
    if p == r:
        return [A[p]]
    q = (p+r)//2
    a = divide(A,p , q)
    b = divide(A,q+1, r)
    return merge(a,b)

def merge(a,b):
    n1 = len(a)
    n2 = len(b)
    l = 0
    r = 0
    A = []
    for i in range(n1+n2):
        if a[l] < b[r]:
            A.append(a[l])
            l = l+1 
            if l == len(a):
                break
        else :
            A.append(b[r])
            r = r+1
            if r == len(b):
                break

    if l == len(a):
        for i in range(r,len(b)):
            A.append(b[i])

    if r == len(b) :
        for i in range(l, len(a)):
            A.append(a[i])      
    return A      

