# User Input / Output

print("Enter the list elements: ")
lst = list(map(int, input().split()))
print("list elements are: ")
print(lst)

# map() function is used to apply specified function to each element of the iterable (list, tuple, etc) and returns an iterator

def square(x):
    return x * x

nums = [1, 2 , 3, 4, 5]
print(list(map(square, nums)))

# print() takes parameters: object(s), sep, end, file, flush
print('hello', 'my', 'friend', sep=' - ', end = ' * ')

