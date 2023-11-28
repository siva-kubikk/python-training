package main

import "fmt"

func check_even_odd(number int)  {
	if number % 2 == 0 {
		// fmt.Printf("%d is Even\n", number)
		fmt.Println(number, "is Even.")
	} else {
		// fmt.Printf("%d is Odd\n", number)
		fmt.Println(number, "is Odd.")
	}
}