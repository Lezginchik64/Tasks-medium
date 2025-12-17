# 1
def greet(name, *args):
    return f'Hello, {" and ".join((name,) + args)}!'  # (name,) + args - это кортеж + кортеж


# 2
def greet(name, *args):
    return f'Hello, {name} and {" and ".join(args)}!' if args else f'Hello, {name}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
