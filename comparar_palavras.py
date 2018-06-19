import difflib

lista = []
manual = []
import csv
with open('nomes.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        lista.append(row[0])

def comparar(palavra):
    palavra_semelhante = difflib.get_close_matches(palavra, lista)
    if palavra_semelhante is not None:
        score_palavra = 0
        palavra_mais_parecida = ''
        for word in palavra_semelhante:
            score_atual = difflib.SequenceMatcher(None, word, palavra).ratio()
            if score_atual > 0.7 and score_atual > score_palavra:
                score_palavra = score_atual
                palavra_mais_parecida = word

        if palavra_mais_parecida != "":
            print(palavra_mais_parecida)
        else:
            print('Palavra não semelhante.')
            manual.append(palavra)


comparar("ZULU")
comparar("BUBA")
comparar("ABBA")
comparar("LELELE")


print("Abaixo os sem correspondência:")
print(manual)







