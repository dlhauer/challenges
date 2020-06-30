import collections

def getHint(secret, guess):
    bulls, cows, i = 0, 0, 0
    guess = list(guess)
    secret = list(secret)

    while i < len(guess):
        if guess[i] == secret[i]:
            bulls += 1
            secret.pop(i)
            guess.pop(i)
        else:
            i += 1

    secret_cnt = collections.Counter(secret)
    guess_cnt = collections.Counter(guess)
    for char, count in secret_cnt.items():
        if char in guess_cnt:
            cows += min(count, guess_cnt[char])

    return f"{bulls}A{cows}B"

secret, guess = '64711', '73411'
print(getHint(secret, guess))
