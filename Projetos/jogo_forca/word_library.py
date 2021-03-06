from random import randint


def save_words(words_to_save):
    with open("library.txt", "w+") as file_to_save:
        for word_to_save in words_to_save:
            word_clean = word_to_save.strip('\n')
            file_to_save.write(f'{word_clean}\n')


def add_words(word_to_add):
    new_word = input('Digite a nova palavra: ')
    new_word = new_word.strip().lower()
    word_to_add.append(new_word)
    printer(msg_to_print='Palavra salva com Sucesso!', blank_lines_after=1)
    return new_word


def remove_words(word_to_remove):
    remove_msg = []
    for index in range(len(word_to_remove)):
        remove_msg.append((index, word_to_remove[index]))
    printer(msg_to_print=([word for word in remove_msg]),
            blank_lines_before=1, blank_lines_after=1)
    word = int(input('Digite o n° da palavra para remover: '))
    undo_selection = int(input('Tem certeza? [1] Para sim, [2] para não: '))
    if undo_selection == 1:
        word_to_remove.pop((word - 1))
        printer(msg_to_print='Tarefa removida com sucesso!',
                blank_lines_after=1)
        return word_to_remove
    else:
        printer(msg_to_print='Remoção cancelada', blank_lines_after=1)


def printer(msg_to_print, blank_lines_before=None, blank_lines_after=None):
    if blank_lines_before:
        for num_lines in range(blank_lines_before):
            print()
    print(msg_to_print)
    if blank_lines_after:
        for num_lines in range(blank_lines_after):
            print()


def boot():
    try:
        with open("library.txt", "r") as file:
            lines = file.readlines()
            load_words = [line.strip('\n') for line in lines]
            return load_words

    except FileNotFoundError:
        with open("library.txt", "x"):
            load_words = []
            return load_words


def select_word():
    try:
        with open("library.txt", "r") as file:
            lines = file.readlines()
            load_words = [line.strip() for line in lines]
            max_word_index = len(load_words) - 1
            selected_word = load_words[randint(0, max_word_index)]
            return selected_word
    except FileNotFoundError:
        print('ERROR: Não há dicionário de palavras criado!')


if __name__ == "__main__":
    saved_words = boot()
    welcome_msg = 'Boas vindas ao Gerenciador de Palavras!'
    menu_msg = '[1] Add, [2] Mostrar, [3] Remover, [4] Salvar e Sair'
    printer(welcome_msg, blank_lines_after=1)

    while True:
        user_selection = input(f'{menu_msg}: ')
        if user_selection == '4':
            save_words(saved_words)
            break
        elif user_selection == '1':
            add_words(saved_words)
        elif user_selection == '2':
            printer(saved_words, blank_lines_after=1)
        elif user_selection == '3':
            remove_words(saved_words)
