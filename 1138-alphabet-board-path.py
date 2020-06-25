def alphabetBoardPath(target):
    res = ''
    cur_pos = (0,0)
    for char in target:
        char_val = ord(char)-97
        next_pos = (char_val // 5, char_val % 5)
        row_moves = next_pos[0] - cur_pos[0]
        col_moves = next_pos[1] - cur_pos[1]
        if col_moves > 0:
            res += 'R' * col_moves
        else:
            res += 'L' * -col_moves
        if row_moves > 0:
            res += 'D' * row_moves
        else:
            res += 'U' * -row_moves
        res += '!'
        cur_pos = next_pos
    return res

target = 'code'
print(alphabetBoardPath(target))
