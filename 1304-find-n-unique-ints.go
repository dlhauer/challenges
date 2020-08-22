package main

import "fmt"

func sumZero(n int) []int {
	arr := make([]int, 0)
	for i := 1; i <= n/2; i++ {
		arr = append(arr, i, -i)
	}
	if n%2 != 0 {
		arr = append(arr, 0)
	}
	return arr
}

func main() {
	fmt.Println(sumZero(9))
}
