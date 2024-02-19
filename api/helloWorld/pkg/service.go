package pkg

import "fmt"

func Hello(content string) Letter {
	return Letter{
		Recipient: "Buntelrus",
		Content:   fmt.Sprintf("Very important!\n%s", content),
	}
}
