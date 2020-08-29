#include <stdio.h>

int divisibleByRange(int min, int max){
    int  divisible = 0;
    int num = max;
    int i;
    while (!divisible){
        for (i = min; i <= max; i ++){
            if (num % i != 0){
                break;
            }
        }
        if (i == max + 1){
           divisible = 1;
        } else {
            num ++;
        }
    }
    return num;

}

int main() {
   int num = divisibleByRange(1, 20);
   printf("%d \n", num);
   return 0;
}
