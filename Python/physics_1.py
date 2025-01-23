import matplotlib.pyplot as plt


def make_plots(position_array, velo_array, accel_array):
  time =        [0,  1,  2,  3,  4,  5,   6,   7,   8,   9  ]

  figure, axies = plt.subplots(1, 3)
  figure.suptitle("Physics Plots")
  axies[0].plot(time,position_array)
  axies[0].set_title("Position")
  axies[0].set_xlabel("Time (s)")
  axies[0].set_ylabel("Position (m)")

  axies[1].plot(time,velo_array)
  axies[1].set_title("Velocity")
  axies[1].set_xlabel("Time (s)")
  axies[1].set_ylabel("Velo. (m/s)")

  axies[2].plot(time,accel_array)
  axies[2].set_title("Acceleration")
  axies[2].set_xlabel("Time (s)")
  axies[2].set_ylabel("Accel. (m/s/s)")

  plt.show()

def is_digit(digit_string):
  try:
    float(digit_string)
    return True
  except ValueError:
    return False

given_info = input("Do you know the acceleration, a list of velocities, or a list of positions? (Please enter: a, vs, ps): ").lower()
while given_info not in ["a", "vs", "ps"]:
  print("Incorret answer. Please only type: a, vs, or ps")
  given_info = input("Do you know the acceleration, list of velocities, or a list of positions? (Please enter: a, vs, ps): ").lower()

acceleration = []
velocity = []
position = []

if given_info == "a": # IN CLASS
  acceleration = input("What's the acceleration?: ")

  while not is_digit(acceleration): # Input validation, make sure a number is given ( assuming all acceleration is positive)
    print("Error. Please enter a valid numerical acceleration")
    acceleration = input("What's the acceleration?: ")

  acceleration = float(acceleration)  # Turn it into an integer
  acceleration = [acceleration] * 10 # make array of constant acceleration

  # Make the resulting velocity array
  velocity.append(0)
  for i in range(1, 10):
    velocity.append(velocity[-1] + acceleration[i])

  print(velocity) # check the velocity
  # Make the resulting position array
  for i in range(10):
    position.append(.5 * i * velocity[i])
  print(position) # check the position

elif given_info == 'vs':  # SPICY Challenge
  velocity_list = []
  counter = 0

  print("Please enter the velocities from begining to end (time 0 -> time 9)")
  while counter < 10: 
    user_answer = input("Enter the next velocity: ")
    while not is_digit(user_answer):  # Input validation for the velocity inputs
      print("Error. Please enter a valid number")
      user_answer = input("Enter the next velocity: ")

    velocity_list.append(float(user_answer))  # add valid velocity input to list
    counter += 1  # Increment counter to keep track of the number of velocities inputed

    # print(velocity_list)  # Check the velocity
  velocity = velocity_list

  #Create the resulting acceleration
  for i in range(9):  # Don't go to the last value
    acceleration.append(velocity[i + 1] - velocity[i]) # acc = change in velocity
  acceleration.append(acceleration[-1]) # 10th acc. value = 9th acc. value because we're assuming constant acc.
  print(acceleration)
    #Create the resulting position
  for i in range(10):
    position.append(.5 * i * velocity[i]) # acc = change in velocity
  print(position)
elif given_info == "ps":  # EXTRA SPICY / impossible (my code is broken because this is AlMOST impossible)
  position_list = []
  counter = 0

  print("Please enter the positions from begining to end (time 0 -> time 9)")
  while counter < 10: 
    user_answer = input("Enter the next position: ")
    while not is_digit(user_answer):  # Input validation for the position inputs
      print("Error. Please enter a valid number")
      user_answer = input("Enter the next position: ")

    position_list.append(float(user_answer))  # add valid position input to list
    counter += 1  # Increment counter to keep track of the number of positions inputed

    # print(position_list)  # Check the positions
  position = position_list

  #Create the resulting velocities
  velocity.append(0)  # Start at 0
  for i in range(1, 10):  # Don't go to the last value
    velocity.append(position[i] - position[i - 1]) # velocity = change in position over a second
  print(velocity)   # check velocity

    #Create the resulting acceleration
  for i in range(9):
    acceleration.append(velocity[i + 1] - velocity[i]) # acc = change in velocity
  acceleration.append(acceleration[-1])  # copy paste last accel. assuming constant acceleration
  print(acceleration)   # check acceleration
else:
  print("Error: The code should never have made it here. User entered: ", given_info)

make_plots(position, velocity, acceleration)