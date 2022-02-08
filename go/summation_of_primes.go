package main

import (
	"fmt"
)

func SieveOfEratosthenes(n int) []int {
	// create a boolean array, and initialize all as true
	integers := make([]bool, n+1)
	for i := 2; i < n+1; i++ {
		integers[i] = true
	}

	for p := 2; p*p <= n; p++ {
		if integers[p] == true {
			for i := p * 2; i <= n; i = p + i {
				integers[i] = false
			}
		}
	}
	var primes []int
	for p := 2; p <= n; p++ {
		if integers[p] == true {
			primes = append(primes, p)
		}
	}
	return primes
}

func eulerProblem10() {
	pr := SieveOfEratosthenes(2000000)
	sum := 0
	for _, p := range pr {
		sum += p
	}
	fmt.Println(sum)
}
