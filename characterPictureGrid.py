grille = [['.', '.', '0', '0', '.', '0', '0', '.', '.'],
          ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
          ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
          ['.', '.', '0', '0', '0', '0', '0', '.', '.'],
          ['.', '.', '.', '0', '0', '0', '.', '.', '.'],
          ['.', '.', '.', '.', '0', '.', '.', '.', '.']]

for i in range(6):
    for j in range(9):
        if j != 8:
            print(grille[i][j], end='')
        else:
            print(grille[i][j])