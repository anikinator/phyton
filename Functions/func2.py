def speak_func(value):
    def yell(text):
        return text.upper() + "..."
    def whisper(text):
        return text.lower() + "..."
    if value > 0.5:
        return yell
    else:
        return whisper

speak = speak_func(0.2)
print(speak('HOw to DEAl wiTH it?'))

# Лексическое замыкание - lexical closures
def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper
print(get_speak_func('Привет, Мир', 0.7)())

# Fabric
def make_adder(n):
    def add(x):
        return x + n
    return add
plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_3(4))
print(plus_5(4))

# Page 74 - collable object: вызываемые объекты
