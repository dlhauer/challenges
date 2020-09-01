package main

import (
	"fmt"
	"strconv"
)

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}
	prev := countAndSay(n - 1)
	var say string
	count := 0
	for i := range prev {
		count++
		if i == len(prev)-1 || prev[i] != prev[i+1] {
			say += strconv.Itoa(count) + prev[i:i+1]
			count = 0
		}
	}
	return say
}

func main() {
	ns := [...]int{1, 2, 3, 4, 5, 6}
	for _, n := range ns {
		fmt.Println(countAndSay(n))
	}
}
