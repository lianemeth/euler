#include <stdio.h>
#include <math.h>

void sieve(int max){
    unsigned int i, j;
    int primes[max];
    int count = 0;
    for (i = 0; i < max; i++) primes[i] = 1;
    for (i = 2; i < max; i++){
        // prime numbers were skipped, since they didnt had a multiple
        if (primes[i]){
            // p starts at 2, 2*1, 2*2, 2*3, 2*4 get marked. 
            // next prime number, 3, 3*1, 3*2, ...
            for (j = i; i * j < max; j ++)
                primes[i * j] = 0;
        }
    }
    for (i=2; i< max; i++){
        if(primes[i]) {
            count ++;
            printf("%d , %d\n", count, i);
        }
    }
}

int main() {
    sieve(110000);
}
