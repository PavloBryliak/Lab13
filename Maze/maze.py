# Implements the Maze ADT using a 2-D array.
from arrays import Array2D
from lliststack import Stack


class Maze:
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = " *"
    PATH_TOKEN = " x"
    TRIED_TOKEN = " o"

    # Creates a maze object with all cells marked as open.
    def __init__(self, num_rows, num_cols):
        self.stack = Stack()
        self._mazeCells = Array2D(num_rows, num_cols)
        self._startCell = None
        self._exitCell = None
        self.st = Stack()

    # Returns the number of rows in the maze.
    def num_rows(self):
        return self._mazeCells.num_rows()

    # Returns the number of columns in the maze.
    def num_cols(self):
        return self._mazeCells.num_cols()

    # Fills the indicated cell with a "wall" marker.
    def setWall(self, row, col):
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

    # Sets the starting cell position.
    def setStart(self, row, col):
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._startCell = _CellPosition(row, col)

    # Sets the exit cell position.
    def setExit(self, row, col):
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._exitCell = _CellPosition(row, col)

    # Method to find neighbour cells
    def neighbours(self, _row, _col):
        info = []
        for coord in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            row, col = _row + coord[0], _col + coord[1]
            if self._validMove(row, col):
                if not self._mazeCells[row, col]:
                    info.append(_CellPosition(row, col))
        return info

    # Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def findPath(self):
        self.stack.push(self._startCell)

        while len(self.stack):
            current = self.stack.peek()
            row, col = current.row, current.col

            if self._exitFound(row, col):
                self._markPath(row, col)
                return True

            fine_cells = self.neighbours(row, col)
            if fine_cells:
                self._markPath(row, col)
                for element in fine_cells:
                    self.stack.push(element)
            else:
                self._markTried(row, col)
                self.stack.pop()

    # Resets the maze by removing all "path" and "tried" tokens.
    def reset(self):
        for row in range(self._mazeCells.num_rows()):
            for col in range(self._mazeCells.num_cols()):
                if self._mazeCells[row, col] in [" x", " o"]:
                    self._mazeCells[row, col] = None

    # Prints a text-based representation of the maze.
    def draw(self):
        for row in range(self._mazeCells.num_rows()):
            for col in range(self._mazeCells.num_cols()):
                if self._mazeCells[row, col]:
                    print(self._mazeCells[row, col], end=" ")
                else:
                    print("  ", end=" ")
            print()

    # Returns True if the given cell position is a valid move.
    def _validMove(self, row, col):
        return 0 <= row < self.num_rows() \
               and 0 <= col < self.num_cols() \
               and self._mazeCells[row, col] is None

    # Helper method to determine if the exit was found.
    def _exitFound(self, row, col):
        return row == self._exitCell.row and col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried(self, row, col):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def _markPath(self, row, col):
        self._mazeCells[row, col] = self.PATH_TOKEN


# Private storage class for holding a cell position.
class _CellPosition(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
