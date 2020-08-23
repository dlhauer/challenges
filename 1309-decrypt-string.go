package main

import (
	"fmt"
	"strconv"
)

func freqAlphabets(s string) string {
	var res string
	for i := 0; i < len(s); {
		inc := 0
		var j int
		if i < len(s)-2 && string(s[i+2]) == "#" {
			j = i + 2
			inc = 3
		} else {
			j = i + 1
			inc = 1
		}
		num, _ := strconv.Atoi(s[i:j])
		num += 96
		res = res + string(num)
		i += inc
	}
	return res
}

func main() {
	s := "10#11#912#"
	fmt.Println(freqAlphabets(s))
}
