from datasource.models.game import SourceGame
from domain.models.game import Game


class SourceMapper:

  @staticmethod
  def from_storage_to_domain(current_game: SourceGame) -> Game:
    game = Game(current_game.game_id)
    game.board.cells = current_game.game_board.cells
    return game

  @staticmethod
  def from_domain_to_storage(game: Game) -> SourceGame:
    source_game = SourceGame(game.game_id)
    source_game.game_board.cells = game.board.cells
    return source_game
