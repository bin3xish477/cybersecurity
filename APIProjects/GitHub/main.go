package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"

	"./github"
	"github.com/akamensky/argparse"
)

func createSearchURL(params []string) string {
	return github.SearchReposURL + strings.Join(params, "+")
}

func parseJSON(resp []byte, results *github.RepositoriesSearch) error {
	return json.Unmarshal(resp, results)
}

func main() {
	parser := argparse.NewParser("gitsearch", "Search GitHub for repositories")
	searchStr := parser.String("s", "search", &argparse.Options{Required: true, Help: "String to search repositories for"})
	language := parser.String("l", "language", &argparse.Options{Required: false, Help: "Language the repositories must contain, ex. Python"})
	err := parser.Parse(os.Args)
	if err != nil {
		fmt.Print(parser.Usage(err))
	}
	fmt.Println(*searchStr)

	var results github.RepositoriesSearch
    	params := []string{*searchStr, "language:"+*language}
	url := createSearchURL(params)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		panic(err)
	}

	personalAccessToken := os.Getenv("GITHUB_TOKEN")
	req.SetBasicAuth("binexisHATT", personalAccessToken)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	
	parseJSON(body, &results)
	fmt.Println(results.TotalCount)
	for _, repo := range results.Items {
		fmt.Println(repo.Owner.Login)
	}
}
