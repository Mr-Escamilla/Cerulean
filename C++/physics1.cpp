#include <iostream>
using namespace std;

// Main() function: where the execution of
// program begins
int main(void)
{
  float acceleration;

  cout << "Enter the constant acceleration: ";  // Get acceleration from the user
  while (!(cin >> acceleration)){ // Validate the input
    cout << "Invalid input, please type the constant acceleration: ";
    cin.clear(); 
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
  }
  cout << "Your acceleration is " << acceleration << endl;
  cout << "**************************************" << endl;

  // Create the velocity for 10 seconds
  float velocity[10];
  velocity[0] = 0;  // Set inital Velocity to 0
  int length_v = sizeof(velocity)/sizeof(velocity[0]);  // (40 / 4) = 10 

  cout << "Your velocities are: " << endl;
  cout << velocity[0] << " ";   // Print out initial velocity
  for(int i = 1; i < length_v; i++){
    velocity[i] = velocity[i - 1] + acceleration; // Velocity = previous + change in velocity (accl.)
    cout << velocity[i] << " ";
  }
  cout << endl << "**************************************" << endl; // Make output readable

  // Create the distance for 10 seconds
  float distance[10];
  int length_d = sizeof(distance)/sizeof(distance[0]);  // (40 / 4) = 10 
  cout << "Your distances are: " << endl;
  for(int i = 0; i < length_d; i++){
    distance[i] = (.5 * i * velocity[i]); // distance = .5 * t * velocity
    cout << distance[i] << " ";
  }
  cout << endl << "**************************************" << endl; // Make output readable

  return 0;
}