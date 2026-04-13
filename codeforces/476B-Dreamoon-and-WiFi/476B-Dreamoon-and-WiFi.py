def backtrack(i,curr,c):
    global Total_path,Success
    if i == len(s1):
        if curr == Target:
            Success += 1
            
        Total_path += 1
        return
    
    if c == "+":
        curr += 1
        next_char = s2[i+1] if i + 1 != len(s2) else ""
        backtrack(i+1,curr,next_char)
    elif c == "-":
        curr -= 1
        next_char = s2[i+1] if i + 1 != len(s2) else ""
        backtrack(i+1,curr,next_char)
    else:
        backtrack(i,curr,"+")
        backtrack(i,curr,"-")

if len(s1) == 0:
    print(1/1)
else:
    backtrack(0,0,s2[0])
    print(f"{Success / Total_path:.12f}")