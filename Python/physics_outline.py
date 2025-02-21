# Physics Graphs

## INSTALL THE FOLLOWING IN THE TERMINAL BEFORE RUNNING YOUR CODE: ##
# sudo apt-get install python3-venv
# python3 -m venv .venv
# source .venv/bin/activate
# pip3 install matplotlib
# pip install PyQt5


## To RUN THE CODE: ##
# 1. Take the file out of the python folder
# 2. You need to run the code manually with "python3 Physics_Graphs.py" so it runs in the same terminal as the installations
#--------------------------------------------------------------------------------------------------------------------
## FUNCTIONS, LISTS, AND USER INPUT ##

# Importations
import matplotlib.pyplot as plt 

# This function takes 3 arrays of 10 elements each, and plots them
def make_plots(position_array, velo_array, accel_array):
 time =  [0,  1,  2,  3,  4,  5,   6,   7,   8,   9  ]

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

# This function takes a user input and checks if it is a negative or positive number
def is_digit(digit_string):
 try:
   float(digit_string)
   return True
 except ValueError:
   return False

given_info = input("Do you know the acceleration, a list of velocities, or a list of positions? (Please enter: a, vs, ps): ").lower()

while given_info not in ["a", "vs", "ps"]:  # Input validation, loop until a valid answer is given
 print("Incorrect answer. Please only type: a, vs, or ps")
 print()
 given_info = input("Do you know the acceleration, list of velocities, or a list of positions? (Please enter: a, vs, ps): ").lower()

# Define the lists for later use
acceleration = []
velocity = []
position = []
#--------------------------------------------------------------------------------------------------------------------
## MAIN CODE ##

# ACCELERATION IS GIVEN
if given_info == "a": # If you're given an acceleration
  # Get accel. from the user
   acceleration_input = input("Please enter the acceleration: ")

  # Input validation, make sure a number is given ( assuming all acceleration is positive ) 
   while not is_digit(acceleration_input):
    print("Incorrect answer. Please only type a number")
    print()
    acceleration_input = input("Please enter the acceleration: ")
   
   else:
    acceleration_input = float(acceleration_input)

  # Make an array of constant acceleration
   for _ in range(10):
      if acceleration_input.is_integer():
        acceleration.append(int(acceleration_input))
      else:
        acceleration.append(acceleration_input)
 
  # Make the resulting velocity array
   for i in range(10):
      velocity.append(acceleration_input * i)
  
  # Make the resulting position array
   if acceleration_input == 0:
      for m in range(10):
         position.append(velocity[m] * m)
   else:
      for m in range(10):
           position.append(velocity[m] * m / 2)
  
   # Print out the lists
   print()
   print(f"Your constant acceleration is: {acceleration}")
   print("****************************************************")
   print(f"Your velocities are : {velocity}")
   print("****************************************************")
   print(f"Your positions are: {position}")
   print("****************************************************")


# VELOCITIES ARE GIVEN
elif given_info == 'vs':  # If you're given a list of 10 velocities
  # Loop 10 times to get velocities
  velocity.append(0)
  v = 1
  print()
  print("The first element of the velocity array is the starting velocity: 0")

  for _ in range(9):
    velocity_element = input(f"Enter element {v + 1}: ")

 # Validate the input for the velocity inputs
    while not is_digit(velocity_element):
      print("Incorrect answer. Please only type a number")
      print()
      velocity_element = input(f"Enter element {v + 1} again: ")
 
 # Turn velocity into digits and add inputs to an array
    else:
      velocity_element = float(velocity_element)

      if velocity_element.is_integer():
        velocity.append(int(velocity_element))
      else:
        velocity.append(round(velocity_element, 2))
      v += 1
 
 # Create the resulting acceleration array
  for d in range(1, len(velocity)):
    accel_difference = velocity[d] - velocity[d - 1]
    acceleration.append(round(accel_difference, 2))
  acceleration.append(round(accel_difference, 2)) # Add the last difference again because if there are 10 velocity elements then there are only 9 differences. This stops and error from popping up

 # Create the resulting position array
  if accel_difference == 0:
      for t in range(10):
         position.append(velocity[t] * t)
  else:
      for t in range(10):
           position.append(velocity[t] * t / 2)

 # Print out the lists
  print()
  print(f"Your accelerations are: {acceleration}")
  print("****************************************************")
  print(f"Your velocities are : {velocity}")
  print("****************************************************")
  print(f"Your positions are: {position}")
  print("****************************************************")


# EXTRA SPICY / impossible (my code is broken because this is AlMOST impossible)
# POSITIONS ARE GIVEN
elif given_info == "ps": # If you're given a list of 10 positions
 # Loop 10 times to get positions
  position.append(0)
  p = 1
  print()
  print("The first element of the postion array is the starting position: 0")

  for _ in range(9):
    position_element = input(f"Enter element {p + 1}: ")

 # Validate the input for the position inputs
    while not is_digit(position_element):
      print("Incorrect answer. Please only type a number")
      print()
      position_element = input(f"Enter element {p + 1} again: ")

 # Add valid position input to an array
    else:
      position_element = float(position_element)

      if position_element.is_integer():
        position.append(int(position_element))
      else:
        position.append(round(position_element, 2))
      p += 1

 # Create the resulting velocities
  pos_difference = None
  for x in range(1, len(velocity)):
    pos_difference = position[x] - position[x - 1]
    velocity.append(round(pos_difference, 2))
  velocity.append(round(pos_difference, 2))

 # Create the resulting acceleration
  for y in range(1, len(velocity)):
    velo_difference = velocity[y] - velocity[y - 1]
    acceleration.append(round(velo_difference, 2))
  acceleration.append(round(velo_difference, 2))

 # Print out the lists
  print()
  print(f"Your accelerations are: {acceleration}")
  print("****************************************************")
  print(f"Your velocities are : {velocity}")
  print("****************************************************")
  print(f"Your positions are: {position}")
  print("****************************************************")

else:
 print("Error: The code should never have made it here. User entered: ", given_info)

# Make the graphs
make_plots(position, velocity, acceleration)