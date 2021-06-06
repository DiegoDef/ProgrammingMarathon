n1, n2, n3, n4 = map(float, input().split())
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print("Media:", round(media, 1))

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    print("Nota do exame:", round((n_exame := float(input())), 1))
    media_f = (media + n_exame) / 2
    if media_f < 5:
        print("Aluno reprovado.")
    else:
        print("Aluno aprovado.")
    print("Media final:", round(media_f, 1))
