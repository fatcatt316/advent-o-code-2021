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

  var text []string
  // var current_depth int
  var previous_depth int
  var total_increases int = 0

  for scanner.Scan() {
  	row_text := scanner.Text()
  	current_depth, err := strconv.Atoi(row_text)
  	check(err)

  	if previous_depth != 0 {
  		fmt.Println(previous_depth)
  		if previous_depth < current_depth {
  			total_increases++
  		}
  	}

    text = append(text, row_text)
    previous_depth = current_depth
  }

  // The method os.File.Close() is called
  // on the os.File object to close the file
  file.Close()

  fmt.Println("-----------------")
	fmt.Println(total_increases)

  fmt.Println("-----------------")

  // and then a loop iterates through
  // and prints each of the slice values.
  // for _, each_ln := range text {
  //     fmt.Println(each_ln)
  // }
}