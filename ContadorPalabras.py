import csv #para archivos con texto separado por comas
import string #para cadenas de texto

translator = str.maketrans('', '', string.punctuation)

word_count = {} #declarando el arreglo
text = open('declaracion.txt').read() #para abrir el archivo .txt en la variable txt

words = text.split() 
for word in words:
    word = word.translate(translator).lower() #.lower para buscar mayusculas y minusculas sin especificar
    count = word_count.get(word, 0) #contador de palabras
    count += 1 #aumenta por cada iteración
    word_count[word] = count #cada nueva iteracion es una nueva palabra

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])

output_file = open('words.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['word', 'count'])
for word in word_count_list:
    writer.writerow([word, word_count[word]])