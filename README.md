
#OpenRizz API Documentation
==========================

## Overview
OpenRizz is a simple API that provides pickup lines and flirt lines. It allows you to generate a response based on the input provided.

## Usage

### HTTP Request

*   **Method:** `POST`
*   **URL:** `http://localhost:8000/rizz/invoke`
*   **Headers:** `Content-Type: application/json`
*   **Body:** A JSON object with the following structure:
```json
{
    "input": {
        "description": "Your pickup line or flirt line",
        "response_type": "Funny, Flirty, Seductive"
    }
}
```
### Examples

#### curl
```bash
curl --location --request POST 'http://localhost:8000/rizz/invoke' \
     --header 'Content-Type: application/json' \
     --data-raw '{
        "input" : {
          "description":"Her name is Shreya. She looks cute and has a Heart of Gold (metaphor)!",
          "response_type":"Funny, Flirty, Seductive"
     }'
```
#### Python
```python
import requests

url = "http://localhost:8000/rizz/invoke"

payload = "{\"input\": {\"description\": \"Her name is Shreya. She looks cute and has a Heart of Gold (metaphor)!\",\"response_type\": \"Funny, Flirty, Seductive\"}}"
headers = { 'Content-Type': 'application/json' }
response = requests.request("POST", url, headers=headers, data=payload)
```
#### Go
```go
package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"strings"
)

func main() {
	client := &http.Client{}
	var data = strings.NewReader(`{
        "input" : {
          "description":"Her name is Shreya. She looks cute and has a Heart of Gold (metaphor)!",
          "response_type":"Funny, Flirty, Seductive"}
     }`)
	req, err := http.NewRequest("POST", "http://localhost:8000/rizz/invoke", data)
	if err != nil {
		log.Fatal(err)
	}
	req.Header.Set("Content-Type", "application/json")
	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	bodyText, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s\n", bodyText)
}
```
#### JavaScript
```javascript
fetch('http://localhost:8000/rizz/invoke', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    'input': {
      'description': 'Her name is Shreya. She looks cute and has a Heart of Gold (metaphor)!',
      'response_type': 'Funny, Flirty, Seductive'
    }
  })
});
```
### Response
The API will return a response based on the input provided. The response will be in the same format as the input.
