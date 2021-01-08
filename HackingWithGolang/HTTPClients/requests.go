package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"strings"
)

func main() {
	// Get requests
	resp, err := http.Get("https://www.google.com/robots.txt")
	defer resp.Body.Close()
	if err != nil {
		panic(err)
	}
	fmt.Println(resp.Status)

	// POST requests
	form := url.Values{}
	form.Add("Name", "Binexis")
	resp, err = http.Post(
		"https://www.google.com/robots.txt",
		"application/x-www-form-urlencoded",
		strings.NewReader(form.Encode()),
	)
	if err != nil {
		panic(err)
	}

	fmt.Println(resp.Status)

	// Get requests using ```http.NewRequest``` and ```http.Client```
	// for more customization
	req, err := http.NewRequest("GET", "https://www.google.com/robots.txt", nil)
	client := http.Client{}
	resp, err = client.Do(req)
	if err != nil {
		panic(err)
	}
	fmt.Println(resp.Status)

	// Reading response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(body))
}
