import numpy as np

def fix_text(text): #функция приводит текст в порядок (приводит к регистру, удаляет неслова)
    cnt = 0
    for i in range(len(text)):
        if (ord("а") <= ord(text[i][len(text[i]) - 1]) <= ord("я")) and (ord("а") <= ord(text[i][0]) <= ord("я")):
            text[i] = text[i].lower()
        else:
            text[i] = "*"
        if text[i] == "*":
            cnt += 1
    for i in range(cnt):
        text.remove("*")
    return text

#путь к файлу для обучения, путь к файлу для записи нового текста, размер нового текста и его первые слова предлагается ввести пользователю

file_name = input("Введите путь к файлу для обучения: ")
file1 = open(f"{file_name}")
text = fix_text(file1.read().split())
file1.close()
new_text_size = int(input("Введите размер генерируемое текста: "))
first_words = input("Введите первые слова нового текста: ")
file_name = input("Введите путь к файлу для записи исходного текста: ")


possible_next_word = {} # словарь вероятностей для следущих слов после данного

#работа со словарем
for i in range(len(text) - 1):
    possible_next_word[text[i]] = {}

for i in range(len(text) - 1):
    if text[i] in possible_next_word and text[i + 1] in possible_next_word[text[i]]:
        possible_next_word[text[i]][text[i + 1]] += 1
    else:
        possible_next_word[text[i]][text[i + 1]] = 1
for i in possible_next_word:
    summ = 0
    for j in possible_next_word[i]:
        summ += possible_next_word[i][j]
    for j in possible_next_word[i]:
        possible_next_word[i][j] = possible_next_word[i][j] / summ


#создание нового текста
new_text = first_words

first_words_arr = first_words.split()
last_word_of_new_text = first_words_arr[len(first_words_arr) - 1]
current_word = last_word_of_new_text #слово, для которого генерируется следующее

#алгоритм добавление нового слова в текст
for j in range(new_text_size):
    following_the_current_words = []
    p_for_following_words = []
    for i in possible_next_word[current_word]:
        following_the_current_words.append(i)
        p_for_following_words.append(possible_next_word[current_word][i])
    current_word = np.random.choice(following_the_current_words, 1, p_for_following_words)
    current_word= current_word[0]
    new_text += current_word + " "

#запись нового текста
file2 = open(f"{file_name}", 'w')
file2.write(new_text)
file2.close()





