package main

import "fmt"

var numbers = map[int]string{
	1:  "one",
	2:  "two",
	3:  "three",
	4:  "four",
	5:  "five",
	6:  "six",
	7:  "seven",
	8:  "eight",
	9:  "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
}

func spelledNumber(n int) string {
	s := ""
	if n == 1000 {
		return "onethousand"
	}
	if n/100 >= 1 {
		s += numbers[n/100] + "hundred"
	}
	n = n % 100
	if n == 0 {
		return s
	}
	if s != "" {
		s += "and"
	}
	if n > 20 {
		dec := n - (n % 10)
		s += numbers[dec]
		n = n % 10
	}
	s += numbers[n]
	return s
}

func main() {
	total := 0
	for i := 1; i <= 1000; i++ {
		total += len(spelledNumber(i))
	}
	fmt.Println(total)
}
