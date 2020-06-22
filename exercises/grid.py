def printRow(delimiter, row_spacer):
    print(getRowSegment(delimiter, row_spacer), getRowSegment(delimiter, row_spacer), delimiter)

def getRowSegment(delimiter, spacer):
    return delimiter + spacer * 4

def printGrid():
    row_spacer = ' -'
    row_delimiter = '+'
    column_spacer = '  '
    column_delimiter = '|'
    printRow(row_delimiter, row_spacer)
    printRow(column_delimiter, column_spacer)
    printRow(column_delimiter, column_spacer)
    printRow(column_delimiter, column_spacer)
    printRow(column_delimiter, column_spacer)
    printRow(row_delimiter, row_spacer)
    printRow(column_delimiter, column_spacer)
    printRow(column_delimiter, column_spacer)
    printRow(column_delimiter, column_spacer)
    printRow(column_delimiter, column_spacer)
    printRow(row_delimiter, row_spacer)

printGrid()