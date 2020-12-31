#include <iostream>
#include <vector>

/*
Write a function which calculates the average of the numbers in a given list.
*/

using namespace std;

double calcAverage(const std::vector<int>& values){
    double average = 0;
    for(int i = 0; i < values.size(); i++) {
        average += values[i];
    }
    return average / values.size();
}