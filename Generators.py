def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)


## Generators have __iter()__ and __next()__ methods which are created automatically.
# Local variables and execution states are saved automatically between calls