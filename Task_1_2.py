
# Задача 2
# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
import datetime
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02]
]

songs=(random.sample(my_favorite_songs,3)),

total_sum = songs[0][0]+songs[0][1]+songs[0][2]
print('Пункт А.Три случайные песни из списка:', total_sum)
sum_time=total_sum[1]+total_sum[3]+total_sum[5]
print(sum_time)

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

song_name1, time1 = random.choice(list(my_favorite_songs_dict.items()))
song_name2, time2 = random.choice(list(my_favorite_songs_dict.items()))
song_name3, time3 = random.choice(list(my_favorite_songs_dict.items()))
print('Пункт B.Три случайные песни из словаря: ',song_name1, time1,' ,', song_name2, time2,' ,', song_name3, time3)
sum_time2 = time1+time2+time3
print(sum_time2)


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random



songs=(random.sample(my_favorite_songs,5))
print('Пункт C.Случайный набор из 5 песен:', songs)

# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

timeList = ['4.02','5.4','3.7']
print('Значения времени:', timeList)
mysum = datetime.timedelta()
for i in timeList:
    (m, s) = i.split('.')
    d = datetime.timedelta( minutes=int(m), seconds=int(s))
    mysum += d
print('Пункт D.Суммарное значение времени: ', str(mysum))