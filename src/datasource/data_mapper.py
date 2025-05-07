from .models.game import CurrentGame
from domain.models.game import Game


class GameMapper:

  @staticmethod
  def from_storage_to_domain(current_game: CurrentGame) -> Game:
    game = Game()
    game.game_id = current_game.game_id
    game.board.cells = current_game.game_board
    return game

  @staticmethod
  def from_domain_to_storage(game: Game) -> CurrentGame:
    return CurrentGame(game_id=game.game_id, board=game.board.cells)
