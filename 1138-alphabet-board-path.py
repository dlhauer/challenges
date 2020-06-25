def alphabetBoardPath(target):
    res = ''
    cur_pos = (0,0)
    for char in target:
        char_val = ord(char)-97
        next_pos = (char_val // 5, char_val % 5)
        row_moves = next_pos[0] - cur_pos[0]
        col_moves = next_pos[1] - cur_pos[1]

        if col_moves > 0:
            col_moves = 'R' * col_moves
        else:
            col_moves = 'L' * -col_moves
        if row_moves > 0:
            row_moves = 'D' * row_moves
        else:
            row_moves = 'U' * -row_moves

        if char == 'z':
            res += col_moves + row_moves
        else:
            res += row_moves + col_moves
            
        res += '!'
        cur_pos = next_pos
    return res

target = 'bzv'
print(alphabetBoardPath(target))
