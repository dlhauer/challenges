package main

import "fmt"

func generate(numRows int) [][]int {
	var rows [][]int
	rows = append(rows, []int{1})
	for i := 1; i < numRows; i++ {
		var row []int
		prev := 0
		for _, num := range rows[i-1] {
			row = append(row, prev+num)
			prev = num
		}
		row = append(row, prev)
		rows = append(rows, row)
	}
	return rows
}

func main() {
	pascal := generate(5)
	for _, row := range pascal {
		fmt.Println(row)
	}
}
