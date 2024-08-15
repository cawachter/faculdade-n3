def calculo_media (b1, b2, b3, b4):
    media = (b1 + b2 + b4 + b4) / 4
    return media

def reprovado (media):
    if media < 6:
        return True
    else:
        return False

def reprovados(nome, matricula, media):
    print(f"Aluno Reprovado: {nome} - Matricula: {matricula} - Média final: {media}")




