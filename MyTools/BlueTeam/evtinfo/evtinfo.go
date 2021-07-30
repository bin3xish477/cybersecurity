package main

import (
	"encoding/csv"
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("usage: eventinfo [event_id] [event_id] ...")
		return
	}
	eventIdArgs := os.Args[1:]
	csvFile, err := os.Open("events.csv")
	if err != nil {
		fmt.Printf("there was an error opening file: %s", err)
		return
	}
	defer csvFile.Close()
	reader, err := csv.NewReader(csvFile).ReadAll()
	if err != nil {
		fmt.Printf("an error occured: %s", err)
	}
	for _, line := range reader {
		eventId, description := line[0], line[1]
		for _, arg := range eventIdArgs {
			if eventId == arg {
				fmt.Printf("\u001b[31mEvent ID\u001b[0m: %s\n\u001b[32mDescription\u001b[0m: '%s'\n", eventId, description)
				fmt.Println("******************************************************")
			}
		}
	}
}
