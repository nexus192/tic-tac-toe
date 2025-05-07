from flask import Flask, request, jsonify, url_for
from uuid import UUID
from web.web_mapper import WebMapper
from domain.services.game_service import IGameService
from web.models.game import WebGame

app = Flask(__name__)
game_service: IGameService = None  # Будет инициализирован через DI


@app.route('/game', methods=['POST'])
def create_game():
  from uuid import uuid4
  new_game_id = uuid4()
  return jsonify({
      "game_url": url_for('handle_move', game_id=new_game_id, _external=True),
      "game_id": str(new_game_id)
  }), 201


@app.route('/game/<uuid:game_id>', methods=['GET'])
def get_game(game_id: UUID):
  return jsonify({
      "game_url": url_for('handle_move', game_id=game_id, _external=True),
      "status": "Game is ready"
  })


@app.route('/game/<uuid:game_id>', methods=['POST'])
def handle_move(game_id: UUID):
  try:
    data = request.get_json()
    web_game = WebGame(game_id=game_id, board=data['board'])
    domain_game = WebMapper.from_web_to_domain(web_game)

    if not game_service.validate_board(domain_game, data['board']):
      return jsonify({"error": "Invalid board state"}), 400

    row, col = game_service.get_next_move(domain_game)
    domain_game.board.set_cell(row, col, domain_game.board.PLAYER_O)
    is_over, winner = game_service.is_game_over(domain_game)
    response_game = WebMapper.from_domain_to_web(domain_game)

    return jsonify({
        "game_id": str(response_game.game_id),
        "board": response_game.board,
        "is_over": is_over,
        "winner": winner,
        "next_move_url": url_for('handle_move', game_id=game_id, _external=True)
    })
  except Exception as e:
    return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
  app.run(debug=True)
