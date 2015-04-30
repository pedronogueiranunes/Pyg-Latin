pyg = 'ay' #Variavel que contem o sufixo 'ay'

original = raw_input('Ola Marujo, Enter a English word:') #palavra original de entrada do usuario
word = original.lower() #palavra original convertida para minusculo
first = word[0] #primeira letra da palavra inserida
new_word = word[1:len(new_word)] + first + pyg # concatenação da palavra a partir do indice 1 + primeira letra + sufixo 'ay'

if len(original) > 0 and original.isalpha(): # testa se a palavra inserida é maior do que 0 caracteres e só tem letras
    print new_word
else:
    print 'Palavra Inválida - Invalid Word'