#!/usr/bin/env python3

import requests

url = "https://api.github.com/user"

r = requests.get(url, auth=("user", "password"))

print("Response status code: ", r.status_code)

print("Response headers[content-type]: ", r.headers["content-type"])

print("Respone encoding: ", r.encoding)

print("Response text: ", r.text)

print("Response in JSON format: ", r.json)