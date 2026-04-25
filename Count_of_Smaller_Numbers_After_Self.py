
def bin_merge_sort(l,r,nums,indx,res):
    if r-l<=1:
        return res,indx
    m=(l+r)//2
    res,indx = bin_merge_sort(l,m,nums,indx,res)
    res,indx = bin_merge_sort(m,r,nums,indx,res)

    temp = []
    i,j = l,m
    rc = 0

    while i<m and j<r:
        if nums[indx[j]]<nums[indx[i]]:
            temp.append(indx[j])
            rc += 1
            j+=1
        else:
            res[indx[i]]+=rc
            temp.append(indx[i])
            i+=1

    while i<m:
        res[indx[i]] += rc
        temp.append(indx[i])
        i+=1

    while j<r:
        temp.append(indx[j])
        j+=1

    indx[l:r] = temp

    return res,indx
    

def small_counter(nums):
    n = len(nums)
    res = [0]*n
    indx = list(range(n))
    bin_merge_sort(0,n,nums,indx,res)
    return res

if __name__ == "__main__":
    inp = [0]
    if not len(inp) or len(inp)>(10**5):
        raise ValueError('invalid input')
    res=small_counter(inp)
    print(res)