from .game_service import IGameService
from domain.models.game import Game
from domain.models.board import Board
from typing import Optional


class MinimaxGameService(IGameService):

  def get_next_move(self, game: Game) -> tuple[int, int]:
    for row in range(game.board.size):
      for col in range(game.board.size):
        if game.board.get_cell(row, col) == Board.EMPTY:
          return (row, col)
    raise ValueError("No valid moves")

  def validate_board(self, game: Game, new_board: list[list[int]]) -> bool:
    for row, col in game.move_history:
      if new_board[row][col] != game.board.get_cell(row, col):
        return False
    return True

  def is_game_over(self, game: Game) -> tuple[bool, Optional[int]]:
    board = game.board
    size = board.size
    for i in range(size):
      if all(board.get_cell(i, j) == Board.PLAYER_X for j in range(size)):
        return (True, Board.PLAYER_X)
      if all(board.get_cell(j, i) == Board.PLAYER_O for j in range(size)):
        return (True, Board.PLAYER_O)
    if all(board.get_cell(i, i) == Board.PLAYER_X for i in range(size)):
      return (True, Board.PLAYER_X)
    if all(
        board.get_cell(i, size - 1 - i) == Board.PLAYER_O for i in range(size)):
      return (True, Board.PLAYER_O)
    return (board.is_full(), None)
