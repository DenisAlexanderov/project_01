data =[
    [4,6,2,1,9,63,-134,566],
    [-52, 56, 30, 29, -54, 0, -110],
    [42, 54, 65, 87, 0],
    [5]
]

for arr in data:
    def minimum(arr):
        for i in range(len(arr)):
            j = i - 1
            var = arr[i]
            while arr[j] > var and j >= 0:
                arr[j+1] = arr[j]
                j -=1
            arr[j+1] = var
        return arr[0]
    def maximum(arr):
        for i in range(len(arr)):
            j = i-1
            var = arr[i]
            while arr[j] > var and j >= 0:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = var
        return arr[-1]
    print (arr, f' -> max = {maximum(arr)}, min = {minimum(arr)}' )