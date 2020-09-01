package main

import "fmt"

func isValid(s string) bool {
	open := map[rune]rune{
		'(': ')',
		'[': ']',
		'{': '}',
	}
	stack := []rune{}
	for _, bracket := range s {
		if open[bracket] != '\x00' {
			stack = append(stack, bracket)
		} else if len(stack) > 0 {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if open[top] != bracket {
				return false
			}
		} else {
			return false
		}
	}
	return len(stack) == 0
}

func main() {
	ss := []string{"[](){}", "[({})]", "[[()", "{})", "[(])", "[", ")"}
	for _, s := range ss {
		fmt.Println(isValid(s))
	}
}
