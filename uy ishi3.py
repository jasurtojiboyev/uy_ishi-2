num = int(input("son kirit:"))
def find_square(num):
    square = num ** 0.5
    return square.is_integer()
print(find_square(num))