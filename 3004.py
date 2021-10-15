for _ in range(int(input())):
    cont = 0
    envelopes = list(map(int, input().split()))
    envelope1, envelope2 = envelopes[:2], envelopes[2:]
    menor1 = min(envelope1)
    menor2 = min(envelope2)
    if menor1 < menor2:
        cont += 1
        envelope1.remove(menor1)
        envelope2.remove(menor2)
        if envelope1[0] < envelope2[0]:
            cont += 1
    if cont == 2:
        print("S")
    else:
        print("N")
