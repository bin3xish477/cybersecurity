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
    "github.com/fatih/color"
)

var (
    boldWhite   = color.New(color.FgWhite).Add(color.Bold)
    boldBlue    = color.New(color.FgBlue).Add(color.Bold)
    boldRed     = color.New(color.FgRed).Add(color.Bold)
    boldGreen   = color.New(color.FgGreen).Add(color.Bold)
    boldYellow  = color.New(color.FgYellow).Add(color.Bold)
    boldCyan    = color.New(color.FgCyan).Add(color.Bold)
    boldMagenta = color.New(color.FgHiMagenta).Add(color.Bold)
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
    sort := parser.String("r", "sort", &argparse.Options{Required: false, Help: "Sort based on the # of [stars, forks, or help-wanted-issues"})
    order := parser.String("o", "order", &argparse.Options{Required: false, Help: "Show results in descending or ascending order [desc | asc"})
    count := parser.Int("c", "count", &argparse.Options{Required: false, Help: "Number of repositories to return"})

	err := parser.Parse(os.Args)
	if err != nil {
		fmt.Print(parser.Usage(err))
        os.Exit(1)
	}

	var results github.RepositoriesSearch
    params := []string{*searchStr}

    if *language != ""{
        params = append(params, *language)
    }
    if *sort != ""{
        params = append(params, "&sort="+*sort)
    }
    if *order != ""{
        params = append(params, "&order="+*order)
    }

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

    if *count == 0 {
        *count = len(results.Items)
    }
	for _, repo := range results.Items[:*count] {
        fmt.Println()
		boldRed.Print("Repository: ")
        fmt.Print(repo.Name)
        boldWhite.Print("   [Stars: ")
        fmt.Print(repo.StargazersCount)
        fmt.Print(" | ")
        boldWhite.Print("Forks: ")
        fmt.Print(repo.Forks)
        boldWhite.Println("]")

        boldCyan.Println("☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳☳")
        if repo.Description != "" {
            boldWhite.Print("  • Description: ")
            fmt.Println(repo.Description)
        } else {
            boldWhite.Print("  • Description: ")
            fmt.Println("None")
        }
		boldBlue.Print("  • Username: ")
        fmt.Println(repo.Owner.Login)

        boldGreen.Print("  • Repo Url: ")
        fmt.Println(repo.HTMLURL)

        boldMagenta.Print("  • Clone Url: ")
        fmt.Println(repo.CloneURL)

        boldYellow.Print("  • SSH Url: ")
        fmt.Println(repo.SSHURL)

        boldRed.Print("  • Language: ")
        if repo.Language == "" {
            fmt.Println("Unknown")
        } else {
            fmt.Println(repo.Language)
        }
	}

    fmt.Println()
    boldWhite.Print(results.TotalCount)
    fmt.Println(" Results")
}
