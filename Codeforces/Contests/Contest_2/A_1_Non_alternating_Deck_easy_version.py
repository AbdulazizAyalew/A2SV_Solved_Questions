
for _ in range(int(input())):
    n = int(input())
    alice = 0
    Bob = 0

    i = 1
    alice_t = True
    bob_t = False
    check_occ = 1

    while n > 0:
        if alice_t:
            if i <= n:
                alice += i
                n -= i
                i += 1
                if check_occ == 1:
                    alice_t = False
                    bob_t = True
                    check_occ = 0
                else:
                    check_occ += 1
                
            else:
                alice += n
                n = 0
        else:
            if i <= n:
                Bob += i
                n -= i
                i += 1
                if check_occ == 1:
                    alice_t = True
                    bob_t = False
                    check_occ = 0
                else:
                    check_occ += 1
            else:
                Bob += n
                n = 0 
    print(f"{alice} {Bob}")
                



