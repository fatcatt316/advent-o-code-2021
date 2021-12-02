package main

import (
    "bufio"
    "fmt"
    "strconv"
    "os"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
	increases_for_groups_of(3)
}

func array_sum(array []int) int {
 result := 0
 for _, v := range array {
  result += v
 }
 return result
}

func increases_for_groups_of(array_size int) {
	// os.Open() opens specific file in
  // read-only mode and this returns
  // a pointer of type os.
  file, err := os.Open("./input.txt")
  check(err)

  // The bufio.NewScanner() function is called in which the
  // object os.File is passed as its parameter and this returns an
  // object bufio.Scanner which is later used with the
  // bufio.Scanner.Split() method.
  scanner := bufio.NewScanner(file)

  var depths []int
  var total_increases int = 0

  for scanner.Scan() {
  	current_depth, err := strconv.Atoi(scanner.Text())
  	check(err)

  	depths = append(depths, current_depth)

  	if len(depths) == array_size + 1 {
  		if array_sum(depths[1:array_size+1]) > array_sum(depths[0:array_size]) {
  			total_increases++
  		}
  		depths = depths[1:]
  	}
  }

  // The method os.File.Close() is called
  // on the os.File object to close the file
  file.Close()

  fmt.Println("-----------------")
	fmt.Println(total_increases)
  fmt.Println("-----------------")
}