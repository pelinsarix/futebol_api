# Documentação da API de Jogadores

## Introdução

O objetivo desta documentação é descrever a API de jogadores, detalhando três tipos de requisições (GET, POST, PUT). A API permite listar jogadores, adicionar novos jogadores e atualizar informações de jogadores existentes.

## Metodologia

As requisições foram realizadas conforme a documentação da API, utilizando os métodos GET, POST e PUT. A seguir, são descritas as requisições, seus objetivos, parâmetros e valores utilizados, bem como os resultados esperados e obtidos.

## Requisições

### 1. GET /jogadores

**Objetivo:** Listar todos os jogadores.

**Parâmetros e Valores Utilizados:** Nenhum.

**Resultados Esperados:** Retornar uma lista de todos os jogadores cadastrados.

**Resultados Obtidos:**

```json
[
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
```

### 2. POST /jogadores

**Objetivo:** Adicionar um novo jogador.

**Parâmetros e Valores Utilizados:**

```json
{
    "id": 31,
    "nome": "Gabriel Jesus",
    "time": "Arsenal"
}
```

**Resultados Esperados:** Retornar o jogador adicionado com status 201.

**Resultados Obtidos:**

```json
{
    "id": 31,
    "nome": "Gabriel Jesus",
    "time": "Arsenal"
}
```

### 3. PUT /jogadores/{id}

**Objetivo:** Atualizar informações de um jogador existente.

**Parâmetros e Valores Utilizados:**

- **ID:** 1
- **Dados:**

```json
{
    "nome": "Neymar Jr.",
    "time": "Al-Hilal"
}
```

**Resultados Esperados:** Retornar o jogador atualizado.

**Resultados Obtidos:**

```json
{
    "id": 1,
    "nome": "Neymar Jr.",
    "time": "Al-Hilal"
}
```
