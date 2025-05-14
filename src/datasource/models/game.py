from uuid import UUID
from .board import Board


class SourceGame:
  EMPTY = 0
  PLAYER_X = 1
  PLAYER_O = 0

  def __init__(self, game_id: UUID):
    self.game_id: UUID = game_id
    self.game_board = Board()
