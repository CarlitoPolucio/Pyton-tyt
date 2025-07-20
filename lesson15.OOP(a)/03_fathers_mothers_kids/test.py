import random


class Child:
  hunger_statuses = {0: 'Fed', 1: 'Hungry'}
  emotions_statuses = {0: 'Calm', 1: 'Crying'}

  def __init__(self, name='Timmy', hunger=0, emotion=0, age=0):
    self.name = name
    self.age = age
    self.emotion = emotion
    self.hunger = hunger

  def info(self):
    print(f'Name: {self.name}\n'
          f'Age: {self.age}\n'
          f'Emotion: {self.emotions_statuses[self.emotion]}\n'
          f'Hunger: {self.hunger_statuses[self.hunger]}\n')


class Parent:

  def __init__(self):
    self.name = 'Sara'
    self.age = 30
    self.childes_list = []

  def info(self, subjects=False):
    if not subjects:
      print(f'Name: {self.name}\n'
            f'Age: {self.age}\n'
            f'Have a childes:')
      self.print_childes()
    else:
      for child in self.childes_list:
        child.info()

  def print_childes(self):
    if len(self.childes_list) == 0:
      print('No child for now.')
    else:
      for child in self.childes_list:
        print(f'{child.name}')

  def chill_out(self, name_child):
    for child in self.childes_list:
      if child.name == name_child:
        child.emotion = 0
        break

  def feeding(self, name_child):
    for child in self.childes_list:
      if child.name == name_child:
        child.hunger = 0
        break

  def check_children_age(self):
    diff_age = []
    for child in self.childes_list:
      difference = self.age - child.age
      if difference < 16:
        diff_age.append(difference)
        print(f'Somthing wrong with {child.name}... (Calling fix_problem method for class Parent and give it diff_age)')
      else:
        print(f'{child.name} Ok')
    return diff_age

  def create_random_child(self, how_many=1, max_age=20):
    print(f'Created new child for {self.name}')
    randon_children = [Child(create_name(), random.randint(0, 1), random.randint(0, 1), random.randint(0, max_age)) for _ in range(how_many)]
    for child in randon_children:
      self.childes_list.append(child)

  def fix_problem(self, errors_list):
    print('Your parent try get more age...')
    try:
      diff = self.age - max(errors_list)
      self.age += diff
    except ValueError:
      print('This fix is not mind, because all child is correct ages.')
      print('Parent not got more years.')


def create_name():
  return input('Give a name for child: ')


timmy = Child('Timmy', 1, 1, 5)
timmy.info()
parent = Parent()
parent.childes_list.append(timmy)
parent.info()
parent.create_random_child(3)
diff_age = parent.check_children_age()
parent.fix_problem(diff_age)
parent.info()
parent.feeding('Timmy')
parent.chill_out('Timmy')
timmy.info()
