class Matrix():

    def __init__(self, height, width):
        self.rows = [[None]*width for i in range(height)]
        self.height = height
        self.width = width

    def __str__(self):
        s = "\n" + "\n".join([str(i) for i in [rows for rows in self.rows] ]) + "\n"
        return s

    def __repr__(self):
        return (f'{self.__class__.__name__} ({self.height!r} , {self.width!r})')

    def len(self):
        return self.height * self.width

    def __add__(self, matrix2):
        return

    def __mul__(self, matrix2):
        return

    def remove(self, item):
        return

    def fill_matrix(self, fill_list):
        index = 0
        for i in range(len(self.rows)):
            try:
                for j in range(len(self.rows[i])):
                    self.rows[i][j] = fill_list[index]
                    index += 1
            except IndexError:
                print (f"Матрица не заполнена \nзаполнение Матрицы остановлено на: row {i}, Column {j}")
                break
        return fill_list[index:]

    def add_value(self, *args):
        log = []
        for arg in args:
           try:
               arg_size = len(arg)
           except TypeError:
               log.append(f'Параметр должен быть последовательным, пропущен: {arg}')
               continue

           try:
               if arg_size == 3:
                       self.rows[arg[0]] [arg[1]] = arg[2]
               else:
                   log.append(f'Параметр содержит слишком много или слишком мало данных, пропущен: {arg}')
           except  IndexError:
               log.append(f'Параметры местоположения находятся вне диапазона, пропущен: {arg}')
           except TypeError:
               log.append(f'Обозначения местоположения должны содержать целые типы, пропущен: {arg}')
        return log


myMat = Matrix(5,5)
overflow = myMat.fill_matrix([i for i in range(25)])
Size=myMat.__repr__
print("Размер матрицы строки,колонки:",Size)
print(myMat)
Errors =  myMat.add_value((-1,3,500), (0,0,3),(51,5, 7), (1, 2, 667), [3,4,676], (1), (1,"a", 1), (1,1, "£"))
print(myMat)
