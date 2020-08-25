package main

import "fmt"

func moveZeroes(nums []int) {
	z := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[i], nums[z] = nums[z], nums[i]
			z++
		}
	}
}

func main() {
	nums := []int{0, 1, 0, 3, 12, 0}
	moveZeroes(nums)
	fmt.Println(nums)
}
