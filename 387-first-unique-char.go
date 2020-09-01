package main

import "fmt"

func firstUniqChar(s string) int {
	count := make(map[rune]int)
	for _, char := range s {
		count[char]++
	}
	for i, char := range s {
		if count[char] == 1 {
			return i
		}
	}
	return -1
}

func main() {
	ss := []string{"leetcode", "danied", "risetovotesir", "hannah"}
	for _, s := range ss {
		fmt.Println(firstUniqChar(s))
	}
}
