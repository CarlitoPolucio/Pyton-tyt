# ---------------------------------------------------------------------------------------
# Original decision:
# import random
#
# def generate_random_data(depth):
#   if depth == 0:
#     return random.randint(1, 10)
#   struct = {}
#   for _ in range(random.randint(1, 2)):
#     key = random.randint(1, 10)
#     struct[key] = generate_random_data(depth - 1)
#
#   return struct
#
#
# depth = random.randint(1, 3)
# random_strict = generate_random_data(depth)
# print(random_strict)


# site = {
#   'html': {
#     'head': {
#       'title': 'Мой сайт'
#     },
#     'body': {
#       'h2': 'Здесь будет мой заголовок',
#       'div': 'Тут, наверное, какой-то блок',
#       'p': 'А вот здесь новый абзац'
#     }
#   }
# }


# def get_max_depth(strict):
#   if isinstance(strict, (dict, list)):
#     if isinstance(strict, dict):
#       depths = [get_max_depth(value) for value in strict.values()]
#     else:
#       depths = [get_max_depth(value) for value in strict]
#     return 1 + max(depths)
#   return 0
#
#
# def search_value_key(struct, key, depth=get_max_depth(random_strict)):
#   if key in struct:
#     return struct[key]
#   if depth == 1:
#     return None
#   if isinstance(struct, dict):
#     for value in struct.values():
#       return search_value_key(value, key, depth - 1)
#
#
# def selecting():
#   target_key = int(input('Enter the integer-key you are looking for: '))
#   while True:
#     select = input('Do you want to enter maximum depth?Y/N ').lower().strip()
#     if select == 'y':
#       while True:
#         depth = int(input('Enter the depth: '))
#         if depth > 0:
#           return target_key, depth
#         else:
#           print('Depth must be more 0.')
#     if select == 'n':
#       return target_key, None
#     print('Enter Y or N.')
#
#
# target, depth_in = selecting()
#
# if isinstance(depth_in, int):
#   print(f'Value key: {search_value_key(random_strict, target, depth_in)}')
# else:
#   print(f'Value key: {search_value_key(random_strict, target)}')

# ---------------------------------------------------------------------------------------

# Alternative decision:
import random

def generate_random_data(depth):
  if depth == 0:
    return random.randint(1, 10)
  elif depth > 0:
    data = {}
    for _ in range(random.randint(1, 3)):
      key = random.randint(1, 10)
      data[key] = generate_random_data(depth - 1)
    return data


depth = random.randint(1, 3)
random_data = generate_random_data(depth)
print(random_data)


def get_max_depth_data(struct):
  if isinstance(struct, (dict, list)):
    if isinstance(struct, list):
      values = struct
    else:
      values = struct.values()
    depths = [get_max_depth_data(value) for value in values]
    if depths:
      return 1 + max(depths)
  return 0
print(f'Maximum depth: {get_max_depth_data(random_data)}')

matches = []

def data_search(struct, key, depth=get_max_depth_data(random_data), current_depth=1):
  if isinstance(struct, dict):
    if key in struct:
      matches.append((struct[key], current_depth))
    if depth == 1:
      return matches
    if isinstance(struct, dict):
      for value in struct.values():
        data_search(value, key, depth - 1, current_depth + 1)
    return matches





def select():
  while True:
    select_user = input('Do you want to enter maximum depth?Y/N ').strip().lower()
    if select_user == 'y':
      while True:
        depth = int(input('Enter the depth: '))
        if depth > 0:
          break
        print('Depth can`t be lower 1')
      break
    if select_user == 'n':
      return None
    print('Wrong number.')
  return depth


print('Please enter the integer number!')
request = int(input('\nEnter the key you are looking for: '))
depth_custom = select()
print('\nTotal Info: ')
max_depth = get_max_depth_data(random_data)
if depth_custom is not None:
  balance = max_depth - depth_custom
  result = data_search(random_data, request, depth_custom)
  if result is not None:
    if balance < 0:
      print(f'{'\n'.join([f"Value key: {value}. Depth: {depth}." for value, depth in matches])}\n'
        f'Total matches: {len(matches)}\n'
        f'Difference custom and maximum actual depth: {abs(balance)} levels\n')

    else:
      print(f'{'\n'.join([f"Value key: {value}. Depth: {depth}." for value, depth in matches])}\n'
            f'Total matches: {len(matches)}\n'
          f'We`ar reached the custom border. To the bottom: {balance} levels')
  else:
    if balance < 0:
      print(f'We`ar reached the bottom on level: {max_depth}\n'
            f'Key not found.')
    else:
      print(f'We`ar reached the custom border. To the bottom: {balance} levels')
else:
  result = data_search(random_data, request)
  if result is not None:
    print(f'{'\n'.join([f"Value key: {value}. Depth: {depth}." for value, depth in matches])}\n'
        f'Total matches: {len(matches)}.')
  else:
    print(f'We`ar reached the bottom on level: {max_depth}\n'
          f'Key not found.')