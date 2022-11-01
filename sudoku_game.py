def sudokuGame():
    array = [10][10]
    for column in array:
        for row in column:
            value = column + row + 1
            if value > 9:
                array[column][row] = value % 10 + 1
            else:
                value
    output(array)


def output(self, array):
    for sudoku in array:
        print(sudoku)

    return array


if __name__ == '__main__':
    sudokuGame()
