from web.models.game import WebGame
from domain.models.game import Game


class WebMapper:

  @staticmethod
  def from_web_to_domain(current_game: WebGame) -> Game:
    game = Game(current_game.game_id)
    game.board.cells = current_game.game_board.cells
    return game

  @staticmethod
  def from_domain_to_web(game: Game) -> WebGame:
    return WebGame(game_id=game.game_id, board=game.board.cells)

  @staticmethod
  def layer_synchronisation(domain_game: Game, web_game: WebGame):
    if domain_game.game_id == web_game.game_id:
      web_game.game_board.cells = domain_game.board.cells
