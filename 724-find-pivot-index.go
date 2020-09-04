package main

import "fmt"

func pivotIndex(nums []int) int {
	prefix, suffix := 0, 0
	for _, num := range nums {
		suffix += num
	}
	for i, num := range nums {
		suffix -= num
		if prefix == suffix {
			return i
		}
		prefix += num
	}
	return -1
}

func main() {
	nums := []int{49, 7, 23, 6, 6, 14}
	fmt.Println(pivotIndex(nums))
}
