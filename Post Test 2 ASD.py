
def linear_search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i 
        
        elif isinstance(arr[i], list):
            for j in range(len(arr[i])):
                 
                 if arr[i][j] == x:
                     
                     return i, j 
        
    return -1

data = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
print(data)
cari = input("cari data apa: ")

result = linear_search(data, cari)

if result == -1:
    print(f'{cari} not found')
elif isinstance(result, tuple):
    print(f'{cari} found at index {result[0]} columns {result[1]}')
else:
    print(f'{cari} found at index {result}')