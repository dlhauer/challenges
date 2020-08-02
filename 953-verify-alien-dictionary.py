def isAlienSorted(words, order):
    order_dict = {char: i for i, char in enumerate(order)}
    sorted_words = sorted(words, key=lambda w: [order_dict[c] for c in w])
    return sorted_words == words
    