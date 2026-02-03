def swap_case(s):
    answer = []
    for i in range(len(s)):
        if s[i] == s[i].lower():
            answer.append(s[i].upper())
        else:
            answer.append(s[i].lower())
    return "".join(answer)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)