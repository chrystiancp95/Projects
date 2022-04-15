def check_valid(input_to_valid):
    if input_to_valid.isalpha():
        return True
    else:
        print('Digite uma letra válida de A à Z!!!')
        return False


def clear_request(input_clear):
    input_clear.strip().lower()
    return input_clear


def input_request():
    while True:
        input_user = input('Digite um letra de A à Z ou "EXIT para sair": ')
        valid_input = check_valid(input_user)
        if valid_input:
            clear_request(input_user)
            return input_user


"""
def guess_checker():
    ...
"""


def secret_word_generator():
    return 'test'


def welcome_msg():
    char_in_line = 79
    print('*' * char_in_line)
    print('*******************'
          ' Bem vindo ao jogo da Forca, boa sorte! ********************')
    print('*' * char_in_line)
    print()


def guess_game():
    secret_word = secret_word_generator()
    guess_word = ['_' for _ in secret_word]
    used_word = []
    game = True
    life = 3
    welcome_msg()

    while game:
        if life == 0:
            print('Você perdeu!')
            break
        guess_char = input_request()
        if guess_char == 'exit':
            print('Até a Próxima!')
            break
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
        current_guess_word = ''.join([str(char) for char in guess_word])
        print(current_guess_word)

        if secret_word == current_guess_word:
            print('***** PARABÉNS, VOCÊ VENCEU! *****')


if __name__ == "__main__":
    guess_game()
