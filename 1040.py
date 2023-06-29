v =  input().split(" ")
n1 = float(v[0])
n2 = float(v[1])
n3 = float(v[2])
n4 = float(v[3])

media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

print(f'Media: {media:.1f}')
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    nota_exame =  float(input())
    print(f'Nota do exame: {nota_exame}')
    media_final = (media + nota_exame)/2
    if media_final > 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')