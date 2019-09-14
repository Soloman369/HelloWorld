import random

N = 50 # grid size



class Snake:
    def __init__(self):
      self.pos = [(0,0), (0,1)]
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



    def game_over(self, game_over=False):
    	if new_pos in self.pos:
    		print("Game Over")
    		self.game_over = True




    def grow(self):
    	self.move(action=self.get_direction(), delete_tail=False)

    def food(self):
    	f1 = random.choice(range(10))
    	f2 = random.choice(range(10))
    	self.food = [(1,1)]


    def move(self, action, delete_tail=True):
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
        if new_x < 0:
        	new_x = 10
        new_pos = (new_x,new_y)
      elif action == 'down':
        if direction in ['up']:
          pass
        h1[0]< h2[0]
        new_x = h1[0] + 1
        new_y = h1[1]
        if new_x > 10:
        	new_x = 0
        new_pos = (new_x,new_y)
      elif action == 'right':
        if direction in ['left']:
          pass
        new_x = h1[0]
        new_y = h1[1] + 1
        if new_y > 10:
        	new_y = 0
        new_pos = (new_x,new_y)
      elif action == 'left':
        if direction in ['right']:
          pass
        new_x = h1[0] 
        new_y = h1[1] - 1
        if new_y < 0:
        	new_y = 10
        new_pos = (new_x,new_y)


      if new_pos == self.food:
      	self.pos.append(new_pos) # add new position ~ move the head

      else:
      	self.pos.append(new_pos) # add new position ~ move the head

      	self.pos = self.pos[1:]


      if self.game_over == True:
      	print("You have lost")




snake = Snake()

import random


for i in range(2):
  action = random.choice(['down'])
  print(action)
  print('before: ',snake.pos)
  snake.move(action, delete_tail=True)
  print('after: ',snake.pos)
