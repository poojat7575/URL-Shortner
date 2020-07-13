# URL-Shortner
A simple URL Shortner implementation in Python

Two REST APIs (built with Python-Flask):
1. /short_url

  	Method: PUT

  	Request body: {"url": "https://mydomain.com/pleasehelpmebyshorteningmylongurl"}

  	Response: "https://mydomain.com/random-string-with-ten-chars"
  
2. /long_url

  	Method: PUT

  	Request body: {"url": "https://mydomain.com/myshorturl"}

  	Response: 
    	"https://mydomain.com/corresponding long url" (if exists)
   		"No record exists" (if not exist)

