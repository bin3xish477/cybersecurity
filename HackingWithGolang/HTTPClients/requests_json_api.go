package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

// ExampleJsonResponse defines a struct to the rest api @/todos/1
type ExampleJsonResponse struct {
	UserId    int
	Id        int
	Title     string
	Completed bool
}

func main() {
	// Rest API for testing
	resp, err := http.Get("https://jsonplaceholder.typicode.com/todos/1")
	defer resp.Body.Close()
	if err != nil {
		panic(resp)
	}

	var jsonResponse ExampleJsonResponse

	// Using ```json.NewDecoder``` to invokde ```Decode method```
	// for parsing JSON response into the ExampleJsonResponse struct variable
	if err := json.NewDecoder(resp.Body).Decode(&jsonResponse); err != nil {
		panic(err)
	}

	fmt.Printf("UserId : %d\n", jsonResponse.UserId)
	fmt.Printf("Id : %d\n", jsonResponse.Id)
	fmt.Printf("Title : %s\n", jsonResponse.Title)
	fmt.Printf("Completed : %t\n", jsonResponse.Completed)
}
