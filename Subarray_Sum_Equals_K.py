def sub_array_counter(nums,k):
    prefix,c,freq = 0,0,{0:1}

    for num in nums:
        prefix += num
        if prefix - k in freq:
            c += freq[prefix-k]

        if prefix in freq:
            freq[prefix]+=1
        else:
            freq[prefix] = 1
    
    return c

if __name__ == "__main__":
    nums,k = [1,2,3],3
    if not len(nums) or len(nums)>(2*(10**4)):
        raise ValueError('invalid input')
    res=sub_array_counter(nums,k)
    print(res)