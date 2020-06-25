def alphabetBoardPath(target):
    res = ''
    cur_pos = (0,0)
    for char in target:
        char_val = ord(char)-97
        next_pos = (char_val // 5, char_val % 5)
        print(next_pos)

target = 'leet'
alphabetBoardPath(target)
