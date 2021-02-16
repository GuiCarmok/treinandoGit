agenda = {"Ana":"(11)956687-9633"}
'''
1.
Implemente a função consulta que recebe uma agenda (um dicionário)
e uma pessoa, e retorna o telefone dessa pessoa.
'''
def consulta(dicionario, pessoa):
    return dicionario[pessoa]

print(consulta(agenda, "Ana"))
'''
2.
Implemente a função adiciona que recebe uma agenda (um dicionário)
uma pessoa e um telefone, e adiciona o telefone dessa pessoa na agenda.

Adicionar um item num dicionário é simples:
dicionario['chave'] = valor
'''

def adiciona(dicionario, pessoa, telefone):
    dicionario[pessoa] = telefone

adiciona(agenda, "Marcos", "98855")

print(agenda)

'''
Uma terceira feature que precisamos para a nossa agenda é
a possibilidade de verificar se uma pessoa já está na base de dados.

Simplesmente verificar agenda['pessoa'] não funciona:
se você acessar uma pessoa que não existe, o python dará um KeyError.

Precisamos, então usar o seguinte: 'chave' in dicionario
    Isso é um teste que retorna True se a chave está no dicionário,
    e False caso contrário.

Temos, por exemplo, os prints seguintes, que verificam se algumas
pessoas estão na agenda.
'''
#print('maria esta na agenda?')
#print('maria' in agenda_exemplo)

#print('damiao esta na agenda?')
#print('damiao' in agenda_exemplo)

#pessoa = 'marcos'
#print('a string da variavel pessoa é uma chave da agenda?')
#print(pessoa in agenda_exemplo)



'''
3.
Assim sendo, implemente a função verifica, que recebe uma agenda
e um nome de pessoa, e verifica se a pessoa está na agenda
(retorna True se a pessoa está e False caso contrário).
'''
def verificar(dicionario, pessoa):
    return pessoa in dicionario
''' 
Para definir um dicionário vazio, fazemos o seguinte:
'''
vazio = {}

'''
4.
Usando seus conhecimentos de dicionário até agora, implemente a função
conta_letras que recebe uma palavra e retorna um dicionário com o número de
ocorrências de cada letra.

Por exemplo, conta_letras('abacaxi') deve retornar o seguinte dicionário:
    {'a':3,'b':1,'c':1,'x':1}

NÃO USE nenhuma função mágica do python. Escreva a lógica usando dicionários.

O seguinte trecho de código pode ser util:

palavra = 'ganancia'
nro_a = 0
for letra in palavra:
    print('estou olhando para', letra)
    if letra == 'a':
        nro_a = nro_a+1

Ele produz como resultado:
estou olhando para g
estou olhando para a
estou olhando para n
estou olhando para a
estou olhando para n
estou olhando para c
estou olhando para i
estou olhando para a

E no final, a variável nro_a vai estar valendo 3.
'''
def conta_letras(palavra):
    dicio = {}
    for i in palavra:
        if i not in dicio:
            dicio[i] = 1
        else:
            dicio[i] += 1
    return dicio

print(conta_letras("abacaxi"))
        
'''
Agora, vamos usar listas e dicionários para criar uma agenda
um pouco mais completa. Veja o exemplo:
'''
agenda_melhor1 = {
    'jadir (professor)': {
        'email': 'jadir.junior@faculdadeimpacta.com.br',
        'telefones': [11999888999, 1177788899]
    },
    'maria' : {
        'email': 'maria.aparecida@exemplo.com',
        'telefones': [84999777444]
    },
    'valdirene': {
        'telefones': [1177788899]
    }
}

'''
5.
Implemente a função e-mail, que recebe uma agenda (dessas melhoradas, como
no exemplo acima) e uma pessoa. Ela retorna o e-mail da pessoa.

Não precisa se preocupar com o caso do registro da pessoa não ter e-mail
(faremos isso mais pra frente).
'''
def email(agenda, pessoa):
    return agenda[pessoa]['email']

print(email(agenda_melhor1,'maria'))

'''
6.
Implemente a função telefone_principal, que recebe uma agenda (nessa versão
mais nova) e uma pessoa. Ela retorna o primeiro telefone da lista de
telefones da pessoa.
'''

def telefone_principal(agenda, pessoa):
    return agenda[pessoa]['telefones'][0]

z = telefone_principal(agenda_melhor1,'jadir (professor)')
print(z)

'''
7.
Se você quiser verificar todas as chaves de um dicionário,
pode fazer como a seguir:

for chave in agenda_melhor1:
    print(chave)

Ele vai produzir como saída:
jadir (professor)
maria
valdirene

Assim sendo, implemente a função sem_email, que recebe uma agenda (nessa versão
mais nova) e retorna uma lista de todos os contatos sem e-mail.

Por exemplo, sem_email(agenda_melhor1) deve retornar uma
lista com um único contato: ['valdirene']
'''
def sem_email(agenda):
    nome = []
    for chave in agenda:
        try:
            agenda[chave]['email']
        except KeyError:
            nome.append(chave)

    return nome
    

f = sem_email(agenda_melhor1)
print(f)

'''
8.
Implemente uma função conta telefones, que recebe uma agenda (nessa versão
mais nova) e retorna a quantidade de números de telefone registrados.

Se houver telefones repetidos (o exemplo agenda_melhor1 tem!),
conte as repetições (então, para agenda_melhor1 a resposta deve
ser 4, por mais que o mesmo número apareça no item valdirene
e no item jadir (professor)
'''
def conta_telefones(agenda):
    contador = 0
    for i in agenda.values():
        contador += len(i['telefones'])
    return contador

k = conta_telefones(agenda_melhor1)
print(k)


'''
9.
Por último, vamos criar uma função conta_ocorrencias
que dirá quantas vezes um telefone ocorre na agenda.

Ela recebe uma agenda melhorada (um dicionário nesse formato
que estamos usando) e devolve um dicionário. As chaves são
os números de telefone, e os valores, às vezes que cada
número apareceu na agenda.
'''