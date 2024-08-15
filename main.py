from operacoes import calculo_media, reprovado, reprovados

alunos = dict({
    1: {"nome": "Maria", "matricula": 26},
    2: {"nome": "Ana", "matricula": 101},
    3: {"nome": "Joao", "matricula": 13},
    4: {"nome": "Aghata", "matricula": 37},
    5: {"nome": "Joaquim", "matricula": 72},
    6: {"nome": "Felix", "matricula": 5},
})

notas = dict({
    1:{"matricula": 26, "1b": 8, "2b": 7, "3b": 5, "4b": 9},
    2:{"matricula": 101, "1b": 9, "2b": 9, "3b": 5, "4b": 9},
    3:{"matricula": 13, "1b": 6, "2b": 5, "3b": 5, "4b": 5},
    4:{"matricula": 37, "1b": 8, "2b": 6, "3b": 7.5, "4b": 9},
    5:{"matricula": 72, "1b": 6, "2b": 5.5, "3b": 5, "4b": 7},
    6:{"matricula": 5, "1b": 10, "2b": 8, "3b": 8, "4b": 8},
})

for chave, nota in notas.items():
    media_final = calculo_media(nota['1b'], nota['2b'], nota['3b'], nota['4b'])
    
    aluno_reprovado = reprovado(media_final)

    if aluno_reprovado:
        for chave, aluno in alunos.items():
            if aluno['matricula'] == nota['matricula']:
                nome_aluno = aluno['nome']
                matricula = aluno['matricula']
                reprovados(nome_aluno, matricula, media_final)

