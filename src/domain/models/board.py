class Board:
  EMPTY = 0
  PLAYER_X = 1
  PLAYER_O = 0

  def __init__(self, size: int = 3):
    self.size = size
    self.cells = [[0 for _ in range(size)] for _ in range(size)]

  def get_cell(self, row: int, col: int) -> int:
    return self.cells[row][col]

  def set_cell(self, row: int, col: int, player: int):
    if self.cells[row][col] != self.EMPTY:
      raise ValueError
    self.cells[row][col] = player

  def is_full(self) -> bool:
    return all(cell != self.EMPTY for row in self.cells for cell in row)
