import word_library


def clear_request(input_clear):
    input_clear.strip().lower()
    return input_clear


def check_valid(input_to_valid):
    if input_to_valid.isalpha() and len(input_to_valid) == 1:
        return True
    else:
        return False


# todo input_request, check_valid and clear_request could be more abstract
def input_request(input_msg, error_input_msg):
    while True:
        input_user = input(input_msg)
        if check_valid(input_user):
            clear_request(input_user)
            return input_user
        print(error_input_msg)


def guess_checker(secret_word, guess_word, guess_char):
    for index, char in enumerate(secret_word):
        if guess_char == char:
            guess_word[index] = guess_char
    return guess_word


def wrong_guess(lives):
    wrong_msg = f'Errou! Você tem mais {lives} tentativas'
    print(wrong_msg)


# todo integração com o módulo word_library
def secret_word_selection():
    secret_word = word_library.select_word()
    return secret_word


def welcome_msg():
    char_in_line = 79
    print('*' * char_in_line)
    print('*******************'
          ' Bem vindo ao jogo da Forca, boa sorte! ********************')
    print('*' * char_in_line)
    print()


def guess_game():
    secret_word = secret_word_selection()
    guess_word = ['_' for _ in secret_word]
    used_word = []
    game = True
    lifes = 5
    lose_msg = 'Você perdeu!'
    exit_msg = 'Até a Próxima!'
    duplicate_msg = 'Letra já utilizada!'
    win_msg = '***** PARABÉNS, VOCÊ VENCEU! *****'
    input_msg = 'Digite um letra de A à Z ou "EXIT para sair": '
    error_input_msg = 'Digite uma letra válida de A à Z!!!'
    welcome_msg()

    while game:
        current_guess_word = ''.join([str(char) for char in guess_word])
        print(f'A palavra secreta é: {current_guess_word} \n')
        if lifes == 0:
            print(f'{lose_msg} \n')
            break
        guess_char = input_request(input_msg, error_input_msg)
        if guess_char == 'exit':
            print(exit_msg)
            break
        if guess_char in used_word:
            print(duplicate_msg)
            continue
        if guess_char in secret_word:
            guess_word = guess_checker(secret_word, guess_word, guess_char)
        else:
            lifes -= 1
            if lifes >= 0:
                wrong_guess(lifes)
        used_word.append(guess_char)
        current_guess_word = ''.join([str(char) for char in guess_word])
        if secret_word == current_guess_word:
            print(win_msg)
            break


if __name__ == "__main__":
    play_msg = 'Deseja jogar? [Y/N]: '
    error_msg = 'Digite Y ou N!'
    while True:
        play = input_request(play_msg, error_msg)
        if play == 'y':
            guess_game()
        if play == 'n':
            break
