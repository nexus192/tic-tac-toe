from datasource.storage import GameStorage
from datasource.repositories.repository import GameRepository
from datasource.services.data_service import GameDataService
from domain.services.minimax import MinimaxGameService


class Container:

  def __init__(self):
    self._storage = GameStorage()
    self._game_repo = GameRepository(self._storage)
    self.game_data_service = GameDataService(self._game_repo)
    self.domain = MinimaxGameService()
