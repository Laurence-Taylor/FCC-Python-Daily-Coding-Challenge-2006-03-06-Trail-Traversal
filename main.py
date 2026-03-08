def navigate_trail(map):
    # This is a very large and complicated way to resolve the problem... I have to improve it....
    def find_start_pos(matrix_map):
        found = False
        rows = len(matrix_map)
        cols = len(matrix_map[0])
        pos_row = 0
        while not found:
            pos_col = 0
            if matrix_map[pos_row][pos_col] == 'C':return pos_row, pos_col, rows, cols
            while pos_col < cols-1:
                pos_col += 1
                if matrix_map[pos_row][pos_col] == 'C':return pos_row, pos_col, rows, cols
            pos_row += 1

    matrix_map = []
    for item in map:
        matrix_map.append(list(item))
    pos_row, pos_col, rows, cols = find_start_pos(matrix_map)
    path = ''
    prev_col = -1
    prev_row = -1
    is_the_end = False
    while not is_the_end:
        if pos_row - 1 >= 0 and pos_row-1 != prev_row and not is_the_end: 
            if matrix_map[pos_row - 1][pos_col] == 'T': 
                path += 'U'
                prev_row = pos_row
                prev_col = -1
                pos_row -= 1
            elif matrix_map[pos_row - 1][pos_col] == 'G': 
                path += 'U'
                is_the_end = True
                pos_row -= 1
        if pos_row + 1 < rows and pos_row+1 != prev_row and not is_the_end: 
            if matrix_map[pos_row + 1][pos_col] == 'T': 
                path += 'D'
                prev_row = pos_row
                prev_col = -1
                pos_row += 1
            elif matrix_map[pos_row + 1][pos_col] == 'G': 
                path += 'D'
                is_the_end = True
                pos_row += 1
        if pos_col - 1 >= 0 and prev_col != pos_col-1 and not is_the_end: 
            if matrix_map[pos_row][pos_col - 1] == 'T': 
                path += 'L'
                prev_col = pos_col
                prev_row = -1
                pos_col -= 1
            elif matrix_map[pos_row][pos_col - 1] == 'G': 
                path += 'L'
                is_the_end = True
                pos_col -= 1
        if pos_col + 1 < cols and prev_col != pos_col+1 and not is_the_end: 
            if matrix_map[pos_row][pos_col + 1] == 'T': 
                path += 'R'
                prev_col = pos_col
                prev_row = -1
                pos_col += 1
            elif matrix_map[pos_row][pos_col + 1] == 'G': 
                path += 'R'
                is_the_end = True
                pos_col += 1

    return path

if __name__ == '__main__':
    print(navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]))
    print('-----')
    print(navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"]))
    print('-----')
    print(navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]))
    print('-----')
    print(navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"]))
    print('-----')
    print(navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]))