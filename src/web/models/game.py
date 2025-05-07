from uuid import UUID
from .board import Board


class WebGame:

  def __init__(self, game_id: UUID):
    self.game_id: UUID = game_id
    self.game_board = Board()
