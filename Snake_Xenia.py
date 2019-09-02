N = 50 # grid size

class Snake:
    def __init__(self):
      self.pos = [(0,0), (0,1)]
      print('Hello Master Otos! & Co-Master Souli!')
      # si x = 0 alors x = 10 ok --> ca on va gerer apres
    def get_direction(self):
      # hna khasna nzido
      h1 = self.pos[-1]
      h2 = self.pos[-2]
      if h1[0]< h2[0]:
        direction = 'up'
      elif h1[0]> h2[0]:
        direction = 'down'
      elif h1[1]>h2[1]:
        direction = 'right'
      elif h1[1]<h2[1]:
        direction = 'left'
      return direction

    def grow(self):
      self.move(action=self.get_direction(), delete_tail=False)

    def move(self, action, delete_tail=True):
      print('Of course, doing what you ask sir')
      assert action in ['up','down','right','left']# chouf mzyan
      # direction = self.get_direction()
      # to continue just call self.move(direction)
      h1 = self.pos[-1]
      h2 = self.pos[-2]

      direction = self.get_direction()

      if action == 'up':
        if direction in ['down']:
          pass
        new_x = h1[0] - 1
        new_y = h1[1]
        new_pos = (new_x,new_y)
      elif action == 'down':
        if direction in ['up']:
          pass
        h1[0]< h2[0]
        new_x = h1[0] + 1
        new_y = h1[1]
        new_pos = (new_x,new_y)
      elif action == 'right':
        if direction in ['left']:
          pass
        new_x = h1[0]
        new_y = h1[1] + 1
        new_pos = (new_x,new_y)
      elif action == 'left':
        if direction in ['right']:
          pass
        new_x = h1[0] 
        new_y = h1[1] - 1
        new_pos = (new_x,new_y)

      self.pos.append(new_pos) # add new position ~ move the head
      if delete_tail:
        self.pos = self.pos[1:]

snake = Snake()

import random
for i in range(4):
  action = random.choice(['up','down','left','right'])
  print(action)
  print('before: ',snake.pos)
  snake.move(action, delete_tail=True)
  print('after: ',snake.pos)


# il reste a faire quoi ?
# le générateur de nourriture -> ca c facile on verra en dernier
# et le règles de jeu
# quelles sont les regles ?
# il faut pas que le head se coïncide avec une partie de son tail

# mohim --> github et tu continues demain, tu ajoutes les regles