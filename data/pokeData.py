import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/"
MOVE_URL = "move/"
POKEMON_URL = "pokemon/"

class Data:

  def __init__(self):
    self.knownMoves = {}
    self.knownPokemons = {}

  def getPokemon(self, pkmnName):
    if (pkmnName not in self.knownPokemons):
        self.knownPokemons[pkmnName] = self.getFromAPI(POKEMON_URL, pkmnName)
    return self.knownPokemons[pkmnName]

  def getMove(self, moveName):
    if (moveName not in self.knownMoves):
        self.knownMoves[moveName] = self.getFromAPI(MOVE_URL, moveName)
    return self.knownMoves[moveName]

  def getFromAPI(self, specificUrl, name):
    url = BASE_URL + specificUrl + name
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    print(response.content)
    return json.load(response.content)
