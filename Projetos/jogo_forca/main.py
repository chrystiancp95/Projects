secret_word = 'test'
guess_word = ['_' for char in secret_word]
used_word = []
game = True
life = 3

while game:
    if life == 0:
        print('Você perdeu!')
        break
    guess_char = input('Digite: ')
    if guess_char in used_word:
        print('Letra já utilizada!')
        continue
    if guess_char in secret_word:
        for index, char in enumerate(secret_word):
            if guess_char == char:
                guess_word[index] = guess_char
    else:
        life -= 1
    used_word.append(guess_char)
    print(''.join([str(char) for char in guess_word]))
