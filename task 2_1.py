
# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

print('Введите через пробел список целых чисел:')
arr = list(map(int, input().split()))

def minimum(arr):
  for i in range(len(arr)-1):
    for j in range (len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
bubble_for(arr)
print("Минимальное значение из списка: ", minimum(arr)[0])
def minimum(arr):
  for i in range(len(arr)-1):
    for j in range (len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
bubble_for(arr)
print("Максимальное значение из списка: ",bubble_for(arr)[len(arr) - 1])
