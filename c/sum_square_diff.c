#include <stdio.h>
#include <math.h>

int sumSquare(int max){
    int total = 0;
    for (int i = 1; i <= max; i++){
        total += pow(i, 2);
    }
    return total;
}

int squareSum(int max){
    int total = 0;
    for (int i = 1; i <= max; i++){
        total += i;
    }
    return pow(total, 2);
}

int main() {
   printf("%d \n",
          squareSum(100) - sumSquare(100));
   return 0;
}
