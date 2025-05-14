from datasource.storage import GameStorage
from datasource.repositories.repository import GameRepository
from datasource.services.data_service import GameDataService
from datasource.data_mapper import GameMapper
from domain.services.minimax import MinimaxGameService
from uuid import UUID


class Container:

  def __init__(self):
    self._storage = GameStorage()
    self._game_repo = GameRepository(self._storage)
    self.game_data_service = GameDataService(self._game_repo)
    self.domain = MinimaxGameService()
