# Задача 1
# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.
print('Первый трек:', my_favorite_songs[0:14])
print('Последний трек:', my_favorite_songs[-13:]) 
print('Второй трек:', my_favorite_songs[16:23]+'\\\''+my_favorite_songs[24:30])
print('Второй трек с конца:',my_favorite_songs[-26:-15])
