from .game_service import IGameService
from domain.models.game import Game
from domain.models.board import Board
from typing import Optional


class MinimaxGameService(IGameService):

  def get_next_move(self, game: Game) -> Optional[tuple[int, int]]:
    best_score = -float('inf')
    best_move = None
    empty_cells = self.__get_empty_cells(game.board.cells)

    if not empty_cells:
      return None  # Нет куда ходить — игра закончена

    for i, j in empty_cells:
      game.board.cells[i][j] = game.board.PLAYER_O
      score = self.__minimax(game, False)
      game.board.cells[i][j] = game.board.EMPTY

      if score > best_score:
        best_score = score
        best_move = (i, j)

    return best_move

  def validate_board(self, game: Game, new_board: list[list[int]]) -> bool:
    for row, col in game.move_history:
      if new_board[row][col] != game.board.get_cell(row, col):
        return False
    return True

  def is_game_over(self, game: Game) -> tuple[bool, Optional[int]]:
    board = game.board
    size = board.size

    if not game.move_history:
      return False, None

    last_row, last_col = game.move_history[-1]
    player = board.get_cell(last_row, last_col)

    if all(board.get_cell(last_row, j) == player for j in range(size)):
      return True, player

    if all(board.get_cell(i, last_col) == player for i in range(size)):
      return True, player

    if last_row == last_col and all(
        board.get_cell(i, i) == player for i in range(size)):
      return True, player

    if last_row + last_col == size - 1 and all(
        board.get_cell(i, size - 1 - i) == player for i in range(size)):
      return True, player

    return board.is_full(), None

  def __score(self, game: Game) -> Optional[int]:
    over, winner = self.is_game_over(game)
    if not over:
      return None
    if winner == Board.PLAYER_X:
      return -10
    elif winner == Board.PLAYER_O:
      return 10
    else:
      return 0

  def __get_empty_cells(self, board):
    """Возвращает список пустых клеток"""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

  def __minimax(self, game: Game, isMaximizing: bool):
    current_score = self.__score(game)
    if current_score is not None:
      return current_score

    if isMaximizing:
      best = -float('inf')
      for i, j in self.__get_empty_cells(game.board.cells):
        game.board.cells[i][j] = game.board.PLAYER_O
        game.move_history.append((i, j))

        best = max(best, self.__minimax(game, False))

        game.board.cells[i][j] = game.board.EMPTY
        game.move_history.pop()
      return best
    else:
      best = float('inf')
      for i, j in self.__get_empty_cells(game.board.cells):
        game.board.cells[i][j] = game.board.PLAYER_X
        game.move_history.append((i, j))

        best = min(best, self.__minimax(game, True))

        game.board.cells[i][j] = game.board.EMPTY
        game.move_history.pop()
      return best
