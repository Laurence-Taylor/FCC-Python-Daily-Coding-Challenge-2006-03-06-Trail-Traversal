def navigate_trail(map):

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
    start_row, start_col, rows, cols = find_start_pos(matrix_map)
    
    print()

    return map

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