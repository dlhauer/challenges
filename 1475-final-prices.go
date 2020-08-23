package main

import "fmt"

func finalPrices(prices []int) []int {
	tmp := make([]int, len(prices))
	copy(tmp, prices)
	for i := range tmp {
		for j := i + 1; j < len(tmp); j++ {
			if tmp[j] <= tmp[i] {
				tmp[i] = tmp[i] - tmp[j]
				break
			}
		}
	}
	return tmp
}

func main() {
	prices := []int{10, 1, 1, 6}
	fmt.Println(finalPrices(prices))
}
