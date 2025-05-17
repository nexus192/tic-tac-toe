from flask import Flask, request, redirect, url_for, render_template
from web.models.game import WebGame
from di.Container import Container
from web.web_mapper import WebMapper
from datasource.data_mapper import SourceMapper
from uuid import UUID

app = Flask(__name__, template_folder='templates')


class Conroller:

  def __init__(self, app: Flask, di_game: Container, web_mapper: WebMapper,
               source_mapper: SourceMapper):
    self.app: Flask = app
    self.DI: Container = di_game
    self.web_mapper: WebMapper = web_mapper
    self.source_mapper: SourceMapper = source_mapper

    self.register_routes()

  def register_routes(self):
    self.app.add_url_rule('/', view_func=self.start_window)
    self.app.add_url_rule('/new_game', view_func=self.new_game)
    self.app.add_url_rule('/all_games', view_func=self.all_games)
    self.app.add_url_rule('/game/<game_id>',
                          view_func=self.game_view,
                          methods=['POST', 'GET'],
                          endpoint='game')

  def game_view(self, game_id):
    game_id = UUID(game_id)

    game = self.web_mapper.from_domain_to_web(
        self.source_mapper.from_storage_to_domain(
            self.DI.game_data_service.get_current_game(game_id)))

    if request.method == 'POST':
      row = int(request.form['row'])
      col = int(request.form['col'])
      if game.game_board.cells[row][col] == 0:
        self.web_mapper.from_web_to_domain(game).make_move(
            row, col, game.game_board.PLAYER_X)
        ai_move = self.DI.domain.get_next_move(
            self.web_mapper.from_web_to_domain(game))
        if ai_move is not None:
          row_ai, col_ai = ai_move
          self.web_mapper.from_web_to_domain(game).make_move(
              row_ai, col_ai, game.game_board.PLAYER_O)

    return render_template('board.html',
                           board=game.game_board.cells,
                           game_id=game.game_id)

  def start_window(self):
    return render_template('navigation_bar.html')

  def new_game(self):
    game = WebGame()
    self.DI.game_data_service.save_current_game(
        self.source_mapper.from_domain_to_storage(
            self.web_mapper.from_web_to_domain(game)))
    return redirect(url_for('game', game_id=game.game_id))

  def all_games(self):
    games = self.DI.game_data_service.get_all_games()
    return render_template('all_games.html', games=games.keys())

  @staticmethod
  def get_local_ip():
    import socket
    return socket.gethostbyname(socket.gethostname())
