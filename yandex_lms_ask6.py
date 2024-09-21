

def main():
    user_input = [input() for x in range(8)]
    user_input = [x.strip() for x in user_input]
    game_word = user_input[0]
    user_input = user_input[1:]
    aplha = {}
    true_words = []
    for x in game_word:
        aplha[x]: game_word.count(x)
    for x in user_input:
        lenght = len(x)
        count = 0
        for symbol in x:
            if symbol in aplha:
                if x.count(symbol) <= aplha[symbol]:
                    count += 1
        if count == lenght:
            true_words.append(x)
    print(true_words)


if __name__ == '__main__':
    main()