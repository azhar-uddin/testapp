board = []
distance=0

for x in range(12):
  board.append(["*"] * 12)

def print_board(board):
  for row in board:
    print " ".join(row)

def validate_input(row, column, inpt):
  while (row < 0 or row > 11) or (column < 0 or column > 11) or board[row][column] == "X":
    print "Kindly Enter a valid Position"
    take_input(inpt)
    if inpt == "Source":
      row, column = source_row, source_col
    if inpt == "Destination":
      row, column = destination_row, destination_col
    if inpt == "Obstacles":
      row, column = obstacle_row, obstacle_col 

def take_input(input):
  global source_row, source_col, destination_row, destination_col, obstacle_row, obstacle_col
  print "Enter the {}".format(input)
  if input == "Obstacles":
    obstacle_row = int(raw_input("Obstacle Row: "))
    obstacle_col = int(raw_input("Obstacle Col: "))
    validate_input(obstacle_row, obstacle_col, input)
  if input == "Source":
    source_row= int(raw_input("Source Row: "))
    source_col = int(raw_input("Source Col: "))
    validate_input(source_row, source_col, input)

take_input("Source")
board[source_row][source_col] = "S"
take_input("Destination")
board[destination_row][destination_col] = "D"

def next_move(row, column):
	if board[row][column] != "X":
		return row, column



print_board(board)
print "Please find the path below"

current_position = [source_row,source_col]

if source_row >= destination_row  and source_col < destination_col:
  while(current_position[0] != destination_row and current_position[1] != destination_col):
    if board[current_position[0]-1][current_position[1]+1] != "X":
      distance += 1
      current_position = [current_position[0]-1, current_position[1]+1]
      board[current_position[0]][current_position[1]] = str(distance)
  if current_position[1] < destination_col:
    distance = distance + destination_col - current_position[1]
  elif current_position[0] > destination_row:
    distance = distance + current_position[0] - destination_row

if source_row > destination_row  and source_col >= destination_col:
  while(current_position[0] != destination_row and current_position[1] != destination_col):
    if board[current_position[0]-1][current_position[1]-1] != "X":
      distance += 1
      current_position = [current_position[0]-1, current_position[1]-1]
      board[current_position[0]][current_position[1]] = str(distance)
  if current_position[1] > destination_col:
    distance = distance + current_position[1] - destination_col
  elif current_position[0] > destination_row:
    distance = distance - destination_row + current_position[0]

if source_row < destination_row  and source_col <= destination_col:
  while(current_position[0] != destination_row and current_position[1] != destination_col):
    if board[current_position[0]+1][current_position[1]+1] != "X":
      distance += 1
      current_position = [current_position[0]+1, current_position[1]+1]
      board[current_position[0]][current_position[1]] = str(distance)
  if current_position[1] < destination_col:
    distance = distance + destination_col - current_position[1]
  elif current_position[0] < destination_row:
    distance = distance + destination_row - current_position[0]

if source_row <= destination_row  and source_col > destination_col:
  while(current_position[0] != destination_row and current_position[1] != destination_col):
    if board[current_position[0]+1][current_position[1]-1] != "X":
      distance += 1
      current_position = [current_position[0]+1, current_position[1]-1]
      board[current_position[0]][current_position[1]] = str(distance)
  if current_position[1] > destination_col:
    distance = distance + current_position[1] - destination_col
  elif current_position[0] < destination_row:
    distance = distance + destination_row - current_position[0]

print_board(board)
print distance