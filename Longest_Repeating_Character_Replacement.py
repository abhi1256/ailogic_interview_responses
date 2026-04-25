def char_replacer(s,k):
    c = [0]*26
    l,max_frq,res = 0,0,0

    for r in range(len(s)):
        indx = ord(s[r]) - 65
        c[indx] +=1

        if c[indx]>max_frq:
            max_frq = c[indx]

        while (r-l+1) - max_frq >k:
            c[ord(s[l])-65] -= 1
            l +=1
        
        current_len = r - l + 1
        if current_len>res:
            res = current_len
    return res

if __name__ == "__main__":
    s,k = "AABABBA",1
    if not len(s) or len(s)>(10**5) or k<0 or k>len(s):
        raise ValueError('invalid input')
    res=char_replacer(s,k)
    print(res)