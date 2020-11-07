package main

import (
    "fmt"
    "encoding/json"
    "net/http"
    "io/ioutil"
    "os"
    "strings"
    "./github"
)

func createSearchURL(params []string) string {
    return github.SearchReposUrl + strings.Join(params, "+")
}

func parseJSON(resp []byte, results *github.RepositoriesSearch) error {
    return json.Unmarshal(resp, results)
}

func main() {
    query_args := []string{"MS17-010", "language:python"}
    var results github.RepositoriesSearch
    url := createSearchURL(query_args)

    req, err := http.NewRequest("GET", url, nil)
    if err != nil {
        panic(err)
    }

    personal_access_token := os.Getenv("GITHUB_TOKEN")
    req.SetBasicAuth("binexisHATT", personal_access_token)

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
        fmt.Println(repo.Owner_.Login)
    }
}

