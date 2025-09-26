def atoi(s):
    s = s.lstrip()
    if not s:
        return 0
    i = 0
    sign = 1
    if s[i]=="+":
        i+=1
    elif s[i]=="-":
        i+=1
        sign = -1
    
    convert = 0
    while i<len(s):
        cur = s[i]
        if not cur.isdigit():
            break
        else:
            convert = convert*10+int(cur)
        i+=1
    convert *= sign
    if convert <= -2**31:
        return -2**31
    elif convert > 2**31 -1:
        return 2**31 -1
    else:
        return convert
    