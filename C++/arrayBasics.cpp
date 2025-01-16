// C++ program to display "Hello World"

// Header file for input output functions
#include <iostream>
using namespace std;

// Main() function: where the execution of
// program begins
int main(void)
{
    // Prints hello world
    cout << "Hello World" << endl;
    
    cout << "Size of char: " << sizeof(char) << endl;
    cout << "Size of int: " << sizeof(int) << endl;
    cout << "Size of float: " << sizeof(float) << endl;

    cout << "Size of long: " << sizeof(long) << endl;
    cout << "Size of double: " << sizeof(double) << endl;

    char aiden[] = "escamilla";
    char* pointer = aiden;
    cout << *(aiden + 9) << endl;

    int five[] = {0, 1, 3, 5, 7};
    int* point = five;
    
    cout << &five << endl;
    cout << *&(five[2]) << endl;
    cout << point[2] << endl;

    return 0;
}