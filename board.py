import random

# getAffectedCellsByPosition
# retrieves all affected cells based on the given position
# @param {Tuple} position
# @param {Integer} size
# @return {List<Tuple>}
def getAffectedCellsByPosition(position, size):
    row, col = position
    allAffectedCells = []
    # order matters
    if row - 1 >= 0: allAffectedCells.append((row - 1, col))
    if col - 1 >= 0: allAffectedCells.append((row, col - 1))
    if col + 1 < size: allAffectedCells.append((row, col + 1))
    if row + 1 < size: allAffectedCells.append((row + 1, col))

    return allAffectedCells

# buildGrid
# creates a string representation of a matrix based on the given size
# if filler is provided, tiles are not placed randomly
# filler is meant to create specific matrix configurations
# @param {Integer} size (default: 5)
# @param {Function} filler (default: None)
# @return {String}
def buildGrid(size = 5, filler = None):
    rows = list()
    for r in range(size):
        row = list()
        for c in range(size):
            if filler:
                row.append(filler(r, c))
            else:
                row.append('0')
        rows.append('|'.join(row))
    return '\n'.join(rows)

# toggleCell
# toggles the cell's value based on a given location in the given encoded board
# @param {String} board
# @param {Tuple} position
# @return {String}
def toggleCell(board, position):
    rows = board.split('\n')
    affectedCells = getAffectedCellsByPosition(position, len(rows))
    for cell in affectedCells:
        row = rows[cell[0]].split('|')
        row[cell[1]] = '1' if row[cell[1]] == '0' else '0'
        rows[cell[0]] = '|'.join(row)
    return '\n'.join(rows)


# parseBoard
# parses the encoded board into a List<List<String>>
# @param {String} board
# @return {List<List<String>>}
def parseBoard(board):
    rows = []
    encodedRows = board.split('\n')
    for encodedRow in encodedRows:
        rows.append(encodedRow.split('|'))
    return rows