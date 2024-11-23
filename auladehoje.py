nome=input("Digite seu nome")
nota1=float(input("Digite a nota1"))
nota2=float(input("Digite a nota2"))

media=(nota1+nota2)/2
if media>= 6:
    print("Aluno aprovado")
else:
    nota3=float(input("Digite a nota3"))
    if nota1>=nota2:
        media=(nota1+nota3)/2
    else:
        media=(nota2+nota3)/2

    if media>=6:
        print("Aluno aprovado")
    else:
        print("Aluno Reprovado")

        








"""nome= input("Diga seu nome")
nota1= float(input("Diga sua nota1"))
nota2= float(input("Dig sua not2"))

media= (nota1+nota2)/2
if media >= 6:
    print("aluno aprovado")
else:
    nota3=float(input("Diga a nota3"))
    if nota1 > nota2:
        media = (nota3 +nota1)/2
    else:
        media = (nota3 + nota1)/2
    if media >= 6:
        print("aluno aprovado")
    else:
        print("aluno reprovado")"""