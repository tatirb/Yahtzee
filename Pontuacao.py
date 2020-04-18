def somaColuna(d):
    aux = 0
    for k in d:
        aux += d[k]
    d['total'] = aux
    return d

def mostrarOpcoes(l,dic):
    d = dict()
    d = dic.copy()
    if d['ones'] == 0:
        d['ones'] = calcularOnes(l)
    if d['twos'] == 0:
        d['twos'] = calcularTwos(l)
    if d['threes'] == 0:
        d['threes'] = calcularThrees(l)
    if d['fours'] == 0:
        d['fours'] = calcularFours(l)
    if d['fives'] == 0:
        d['fives'] = calcularFives(l)
    if d['sixes'] == 0:
        d['sixes'] = calcularSixes(l)
    if d['three of a kind'] == 0:
        d['three of a kind'] = calcularThreeOfAKind(l)
    if d['four of a kind'] == 0:
        d['four of a kind'] = calcularFourOfAKind(l)
    if d['full house'] == 0:
        d['full house'] = calcularFullHouse(l)
    if d['small straight'] == 0:
        d['small straight'] = calcularSmallStraight(l)
    if d['large straight'] == 0:
        d['large straight'] = calcularLargeStraight(l)
    if d['chance'] == 0:
        d['chance'] = calcularChance(l)
    if d['yahtzee'] == 0:
        d['yahtzee'] = calcularYahtzee(l)
    return d
    

def calcularSmallStraight(l):
    new_list = []
    l.sort()
    nl = l.copy()
    ant = nl[0]
    for i in nl[1:]:
        if ant == i:
            nl.remove(i)
        else:
            ant = i
    if nl[0]!=1 and nl[0]!=2 and nl[0]!=3:
        return 0
    if nl[1]!=2 and nl[1]!=3 and nl[1]!=4:
        return 0
    if nl[2]!=3 and nl[2]!=4 and nl[2]!=5:
        return 0
    if nl[3]!=4 and nl[3]!=5 and nl[3]!=6:
        return 0
    return 30

def calcularFours(l): 
    soma = 0
    for i in l:
        if i == 4:
            soma += 4
    return soma

def calcularOnes(l): 
    soma = 0
    for i in l:
        if i == 1:
            soma += 1
    return soma

def calcularYahtzee(l): 
    ant = l[0]
    for i in l[1:]:
        if ant != i:
            return 0
        ant = l[i]
    return 50

tabela = {
     'ones':0, 
     'twos':0,
     'threes':0,
     'fours':0,
     'fives':0,
     'sixes':0,
     'total superior':0,
     'bonus superior':0,
     'total bonus':0,
     'three of a kind':0,
     'four of a kind':0,
     'full house':0,
     'small straight':0,
     'large straight':0,
     'chance':0,
     'yahtzee':0,
     'bonus yahtzee':0,
     'total':0
     }