package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"

	"./github"
)

func createSearchURL(params []string) string {
	return github.SearchReposURL + strings.Join(params, "+")
}

func parseJSON(resp []byte, results *github.RepositoriesSearch) error {
	return json.Unmarshal(resp, results)
}

func main() {
	queryArgs := []string{"MS17-010", "language:python"}
	var results github.RepositoriesSearch
	url := createSearchURL(queryArgs)

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
