# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в 
# программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

#**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#    **Вывод:** Парам пам-пам  

def count_syllables(word):
    vowels = "аиеёоуыэюя"
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

def check_rhythm(poem):
    phrases = poem.split()
    syllable_count = None

    for phrase in phrases:
        words = phrase.split("-")
        phrase_syllables = sum(count_syllables(word) for word in words)
        
        if syllable_count is None:
            syllable_count = phrase_syllables
        elif syllable_count != phrase_syllables:
            return "Пам парам"
    
    return "Парам пам-пам"

poem = input("Введите стих: ")

result = check_rhythm(poem)

print(result)