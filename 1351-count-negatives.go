package main

import "fmt"

func countnegatives(grid [][]int) int {
	iMax := len(grid)
	jMax := len(grid[0])
	count := 0
	for i := 0; i < iMax; i++ {
		j := 0
		if grid[i][j] < 0 {
			count += (iMax - i) * (jMax - j)
			break
		}
		for j := 0; j < jMax; j++ {
			if grid[i][j] < 0 {
				count += (jMax - j) * (iMax - i)
				jMax = j
			}
		}
	}
	return count
}

func main() {
	grid := [][]int{
		{4, 3, 2, -1},
		{3, 2, 1, -1},
		{1, 1, -1, -2},
		{-1, -1, -2, -3},
	}
	thing := countnegatives(grid)
	fmt.Printf("\n%d\n", thing)
}
