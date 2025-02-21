#include <iostream>
using namespace std;

// C++ program begins
int main() {
    float acceleration; // Number?


    cout << "Enter an integer: ";
    while (!(cin >> acceleration)) {
        cout << "Invalid input. Please enter an integer: ";
        cin.clear(); 
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    cout << acceleration << endl;

  //Calcualte velocity

    //  START      STOP    INCREASE
    for(int i = 0; i < 10; i = i + 2){
      cout << i << endl;
    }


    return 0;
}