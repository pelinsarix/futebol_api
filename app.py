from flask import Flask, request, jsonify

app = Flask(__name__)

jogadores = [
    {"id": 1, "nome": "Neymar", "time": "PSG"},
    {"id": 2, "nome": "Messi", "time": "Inter Miami"},
    {"id": 3, "nome": "Cristiano Ronaldo", "time": "Al-Nassr"},
    {"id": 4, "nome": "Mbappé", "time": "PSG"},
    {"id": 5, "nome": "Lewandowski", "time": "Barcelona"},
    {"id": 6, "nome": "Kevin De Bruyne", "time": "Manchester City"},
    {"id": 7, "nome": "Erling Haaland", "time": "Manchester City"},
    {"id": 8, "nome": "Virgil van Dijk", "time": "Liverpool"},
    {"id": 9, "nome": "Sergio Ramos", "time": "Sevilla"},
    {"id": 10, "nome": "Harry Kane", "time": "Bayern Munich"},
    {"id": 11, "nome": "Karim Benzema", "time": "Al-Ittihad"},
    {"id": 12, "nome": "Luka Modric", "time": "Real Madrid"},
    {"id": 13, "nome": "Mohamed Salah", "time": "Liverpool"},
    {"id": 14, "nome": "Sadio Mané", "time": "Al-Nassr"},
    {"id": 15, "nome": "Son Heung-min", "time": "Tottenham"},
    {"id": 16, "nome": "Antoine Griezmann", "time": "Atlético Madrid"},
    {"id": 17, "nome": "Paulo Dybala", "time": "AS Roma"},
    {"id": 18, "nome": "Bruno Fernandes", "time": "Manchester United"},
    {"id": 19, "nome": "Casemiro", "time": "Manchester United"},
    {"id": 20, "nome": "N'Golo Kanté", "time": "Al-Ittihad"},
    {"id": 21, "nome": "Phil Foden", "time": "Manchester City"},
    {"id": 22, "nome": "Gavi", "time": "Barcelona"},
    {"id": 23, "nome": "Vinícius Júnior", "time": "Real Madrid"},
    {"id": 24, "nome": "Marcus Rashford", "time": "Manchester United"},
    {"id": 25, "nome": "João Félix", "time": "Barcelona"},
    {"id": 26, "nome": "Romelu Lukaku", "time": "Chelsea"},
    {"id": 27, "nome": "Thiago Silva", "time": "Chelsea"},
    {"id": 28, "nome": "Raphael Varane", "time": "Manchester United"},
    {"id": 29, "nome": "Jude Bellingham", "time": "Real Madrid"},
    {"id": 30, "nome": "Pedri", "time": "Barcelona"}
]


@app.route('/jogadores', methods=['GET'])
def get_jogadores():
    return jsonify(jogadores)

@app.route('/jogadores/<int:id>', methods=['GET'])
def get_jogador_por_id(id):
    jogador = next((j for j in jogadores if j['id'] == id), None)
    if jogador is None:
        return jsonify({"erro": "Jogador não encontrado"}), 404
    return jsonify(jogador)

@app.route('/jogadores', methods=['POST'])
def add_jogador():
    novo_jogador = request.get_json()
    jogadores.append(novo_jogador)
    return jsonify(novo_jogador), 201

@app.route('/jogadores/<int:id>', methods=['PUT'])
def update_jogador(id):
    jogador = next((j for j in jogadores if j['id'] == id), None)
    if jogador is None:
        return jsonify({"erro": "Jogador não encontrado"}), 404
    dados = request.get_json()
    jogador.update(dados)
    return jsonify(jogador)

if __name__ == '__main__':
    app.run(debug=True)
