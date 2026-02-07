string_1 = input().lower()
string_2 = input().lower()

for i in range(len(string_1)):
    if string_1[i] > string_2[i]:
        print(1)
        break
    elif string_1[i] < string_2[i]:
        print(-1)
        break
else:
    print(0)

