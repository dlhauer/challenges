package main

import "fmt"

func containsNearbyDuplicate(nums []int, k int) bool {
	prev := make(map[int]int)
	for i, num := range nums {
		if j, ok := prev[num]; ok && i-j <= k {
			return true
		}
		prev[num] = i
	}
	return false
}

func main() {
	nums := []int{-1, 0, 3, 6, 1, 2, 3}
	k := 3
	fmt.Println(containsNearbyDuplicate(nums, k))
}
