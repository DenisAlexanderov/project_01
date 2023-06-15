# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
import sqlite3
# Создание первой таблицы
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL PRIMARY KEY);"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
query = """INSERT INTO Students (Student_Id , Student_Name , School_Id)
VALUES
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);"""
cursor.execute(query)
connection.commit()
connection.close()

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_Student(Student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM Students WHERE Student_Id = ?"""
    cursor.execute(query,(Student_id,))
    records = cursor.fetchall()
    print ("Данные по ID студента:")
    for row in records:
      print ("ID Студента:", row[0])
      print ("Имя Студента:", row[1])
      print ("ID школы", row[2])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ('Ошибка в получении данных ', error)
   
   
get_Student(204)


