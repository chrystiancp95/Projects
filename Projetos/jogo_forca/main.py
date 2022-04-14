secret_word = 'test'
guess_word = ['_' for char in secret_word]

while True:
    guess_char = input('Digite: ')
    for index, char in enumerate(secret_word):
        if guess_char == char:
            guess_word[index] = guess_char

    print(''.join([str(char) for char in guess_word]))

    print('Teste Git')
