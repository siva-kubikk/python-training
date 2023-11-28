package main
func factorial(n int){
	var f int = 1;
	for i := 1; i < n+1; i++ {
		f = f * i
	}
	println(f)
}