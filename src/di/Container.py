from datasource.storage import GameStorage
from datasource.repositories.repository import GameRepository
from datasource.services.data_service import GameService
from domain.models.game import Game
from domain.services.minimax import MinimaxGameService
from web.web_mapper


class Container:

  def __init__(self):
    self.storage = GameStorage()
    self.game_repo = GameRepository(self.storage)
    self.game_service = GameService(self.game_repo)
    self.game = None
