
n,m = map(int,input().split())
old_word = list(input())

word_indx = {}

for i in range(len(old_word)):
    if old_word[i] in word_indx:
        word_indx[old_word[i]].append(i)
    else:
        word_indx[old_word[i]] = [i]
    

for j in range(m):
    xi,yi = input().split()
    if xi in word_indx:
        if yi in word_indx:
            word_indx[xi],word_indx[yi] = word_indx[yi],word_indx[xi]
        else:
            word_indx[yi] = word_indx[xi]
            del word_indx[xi]
    else:
        if yi in word_indx:
            word_indx[xi] = word_indx[yi]
            del word_indx[yi]
        

Result = ["-" for _ in range(len(old_word))]

for wrd in word_indx:
    for k in word_indx[wrd]:
        Result[k] = wrd

print("".join(Result))