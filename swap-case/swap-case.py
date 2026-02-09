def swap_case(s):
    ans=""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                ans+=ch.lower()
            else:
                ans+=ch.upper()
        else:
            ans+=ch
                
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)