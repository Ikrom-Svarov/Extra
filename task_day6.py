""" В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
    A, E, I, O, U, L, N, S, T, R – 1 очко;
    D, G – 2 очка;
    B, C, M, P – 3 очка;
    F, H, V, W, Y – 4 очка;
    K – 5 очков;
    J, X – 8 очков;
    Q, Z – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские буквы.
d = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K',],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

word = input("Введите слово без цифр и спецсимволов: ").upper()
result = 0

for letter in word:
    if letter in d[1]:
        result += 1

    elif letter in d[2]:
        result += 2

    elif letter in d[3]:
        result += 3

    elif letter in d[4]:
        result += 4

    elif letter in d[5]:
        result += 5

    elif letter in d[8]:
        result += 8

    elif letter in d[10]:
        result += 10

print(f"Ваш результат: {result}!")



#2




#3
"""set1=['hey', 'hey', 'hey', 'hey', 'hey']
['helo', 'hello', 'hell', 'hell0', 'heIIo', 'hello']
['this', 'is', 'just', 'a', 'list', 'do', 'not', 'touch', 'me']
print(set1)"""