# Problem Formulation

## State Description

Board size NxN

## Inital State

Board(SIZE)

## Actions

* TAB

## Transition model

| Operator | Pre-conditions | Changes |
| -------- | -------------- | ------- |
| `tab(row, col)` | (row - 1, col) == true OR <br> (row, col - 1) == true OR <br> (row, col + 1) == true OR <br> (row + 1, col) == true | toggle value at (row - 1, col) AND <br> toggle value at (row, col - 1) AND <br> toggle value at (row, col + 1) AND <br> toggle value at (row + 1, col)  on board |

## Goal State

```
sub allCellsAreEmpty(board)
	for row in board
		for cell in row
			if cell is true
				return false
	return true
```

# Path Cost

* TAB = +1
