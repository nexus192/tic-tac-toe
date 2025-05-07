class Board:
  EMPTY = 0
  PLAYER_X = 1
  PLAYER_O = 0

  def __init__(self, size: int = 3):
    self.size = size
    self.cells = [[0 for _ in range(size)] for _ in range(size)]
