import random

class Dice:
    def __init__(self, possibilities=[1,2,3,4,5,6]):
        self.possibilities = possibilities
    def launch(self):
        return random.choice(self.possibilities)

class Player:
  def __init__(self, name=''):
    self.pawns = [0,0,0,0] # 0 c'est la maison, ok? et les position c'est 1..68
    self.name = name if name != '' else 'Inconnu' # tu comprends ca ? -->non
    # si pendant la creation de l'instance de player on donne name='Otos'
    # on va mettre self.name = 'Otos'
    # si on ne specifie pas de nom, alors on va mettre self.name = 'Inconnu'--> aah ok

  def play(self, dices):
    samples = [dice.launch() for dice in dices]
    # donc ici on va avoir les valeur retourne par chaque des samples=(1,2) par exemple ..
    print(samples)

class Partchi:
  def __init__(self, players=[]):
    self.dices = [Dice(), Dice()]
    if len(players)==0: # si on ne donne pas de player pendant la creation du jeu
      self.players = [Player() for i in range(4)]
    else:
      self.players = players

  def play(self):
    for player in self.players:
      player.play()

# ici on va creer deux joueurs
otos = Player(name='Otos')
souli = Player(name='Souli')
print(otos.pawns)


