class Matrix:
  def __init__(self, rows, columns):
    self._matrix = [[None for j in range(columns)] for i in range(rows)]
    self._rows_count = rows
    self._columns_count = columns

  def set_value(self, row, column, value):
    self._matrix[row][column] = value

  def get_value(self, row, column):
    return self._matrix[row][column]

  def get_rows_count(self):
    return self._rows_count

  def get_columns_count(self):
    return self._columns_count

m = Matrix(10, 10)
for i in range(m.get_rows_count()):
    for j in range(m.get_columns_count()):
        m.set_value(i, j, 1)
print(m._matrix)