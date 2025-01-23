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
  given_info = input("Do you know the acceleration, list of velocities, or a list of positions? (Please enter: a, vs, ps): ").lower()

# Define the lists for later use
acceleration = []
velocity = []
position = []

# IN CLASS
if given_info == "a": # If you're given an acceleration
  # GET ACCEL. FROM THE USER
  accel_user_input = input("Please enter the acceleration: ")
  # Input validation, make sure a number is given ( assuming all acceleration is positive )
  while not is_digit(accel_user_input):  # Input validation, loop until a valid answer is given
    print("Invalid input. Please only type a number for accel.")
    accel_user_input = input("Please enter the acceleration: ").lower()

  # Turn acceleration into an float
  accel_number = float(accel_user_input)
  # Make an array of constant acceleration
  acceleration = [accel_number] * 10
  print(acceleration)
  # Make the resulting velocity array
  
  # Make the resulting position array
  print("The code is working")

# Uncomment the line below if to start working on this
#elif given_info == 'vs':  # If you're given a list of 10 velocities
  

  # Loop 10 times to get velocities
  # Validate the input for the velocity inputs
  

  # Turn velocity into digits and add inputs to an array


  #Create the resulting acceleration array

  #Create the resulting position

# EXTRA SPICY / impossible (my code is broken because this is AlMOST impossible)
# Uncomment the line below if to start working on this
#elif given_info == "ps": # If you're given a list of 10 positions

  # Loop 10 times to get positions
  # Validate the input for the position inputs

  # add valid position input to an array

  #Create the resulting velocities

  #Create the resulting acceleration
else:
  print("Error: The code should never have made it here. User entered: ", given_info)

test_positions = [0, 5, 20, 45, 80, 125, 180, 245, 320, 405]
test_velocity = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
test_acceleration = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

make_plots(test_positions, test_velocity, test_acceleration)