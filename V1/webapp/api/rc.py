import requests
import json
import requests

def rc():
    return requests.get("http://localhost:8090/api/objects/info?name=sun&format=json")

def post_rc(request):
    if request == "right":

        url = "http://localhost:8090/api/main/move"

        headers = {
            "Accept": "*/*",
            "Accept-Language": "fr-FR,fr;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://localhost:8090",
            "Referer": "http://localhost:8090/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }

        cookies = {
            "PHPSESSID": "a8d6icao0cl84p0ect424oiniv",
            "username-localhost-8888": "2|1:0|10:1742320309|23:username-localhost-8888|204:eyJ1c2VybmFtZSI6ICJmZDZjYTdlMmNlNzQ0ODBlYTAzYzhmNjY2YTUxNjEzNCIsICJuYW1lIjogIkFub255bW91cyBDYWxsaXJyaG9lIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgQ2FsbGlycmhvZSIsICJpbml0aWFscyI6ICJBQyIsICJjb2xvciI6IG51bGx9|cfa169e5bdc76d58f45a0b65997be28d8d874f9343c782d38b28215fc53de18d",
            "_xsrf": "2|829786cb|3a6ff780e4268a76b44c8f31db745582|1742320309",
        }

        data = {
            "x": "1",
            "y": "0",
        }

        response = requests.post(url, headers=headers, cookies=cookies, data=data)

        return response.status_code
    
    if request == "top":

        url = "http://localhost:8090/api/main/move"

        headers = {
            "Accept": "*/*",
            "Accept-Language": "fr-FR,fr;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://localhost:8090",
            "Referer": "http://localhost:8090/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }

        cookies = {
            "PHPSESSID": "a8d6icao0cl84p0ect424oiniv",
            "username-localhost-8888": "2|1:0|10:1742320309|23:username-localhost-8888|204:eyJ1c2VybmFtZSI6ICJmZDZjYTdlMmNlNzQ0ODBlYTAzYzhmNjY2YTUxNjEzNCIsICJuYW1lIjogIkFub255bW91cyBDYWxsaXJyaG9lIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgQ2FsbGlycmhvZSIsICJpbml0aWFscyI6ICJBQyIsICJjb2xvciI6IG51bGx9|cfa169e5bdc76d58f45a0b65997be28d8d874f9343c782d38b28215fc53de18d",
            "_xsrf": "2|829786cb|3a6ff780e4268a76b44c8f31db745582|1742320309",
        }

        data = {
            "x": "0",
            "y": "1",
        }

        response = requests.post(url, headers=headers, cookies=cookies, data=data)

        return response.status_code
    
    if request == "bottom":
        url = "http://localhost:8090/api/main/move"

        headers = {
            "Accept": "*/*",
            "Accept-Language": "fr-FR,fr;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://localhost:8090",
            "Referer": "http://localhost:8090/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }

        cookies = {
            "PHPSESSID": "a8d6icao0cl84p0ect424oiniv",
            "username-localhost-8888": "2|1:0|10:1742320309|23:username-localhost-8888|204:eyJ1c2VybmFtZSI6ICJmZDZjYTdlMmNlNzQ0ODBlYTAzYzhmNjY2YTUxNjEzNCIsICJuYW1lIjogIkFub255bW91cyBDYWxsaXJyaG9lIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgQ2FsbGlycmhvZSIsICJpbml0aWFscyI6ICJBQyIsICJjb2xvciI6IG51bGx9|cfa169e5bdc76d58f45a0b65997be28d8d874f9343c782d38b28215fc53de18d",
            "_xsrf": "2|829786cb|3a6ff780e4268a76b44c8f31db745582|1742320309",
        }

        data = {
            "x": "0",
            "y": "-1",
        }

        response = requests.post(url, headers=headers, cookies=cookies, data=data)

        return response.status_code
    
    if request == "left":
        url = "http://localhost:8090/api/main/move"

        headers = {
            "Accept": "*/*",
            "Accept-Language": "fr-FR,fr;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://localhost:8090",
            "Referer": "http://localhost:8090/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
        }

        cookies = {
            "PHPSESSID": "a8d6icao0cl84p0ect424oiniv",
            "username-localhost-8888": "2|1:0|10:1742320309|23:username-localhost-8888|204:eyJ1c2VybmFtZSI6ICJmZDZjYTdlMmNlNzQ0ODBlYTAzYzhmNjY2YTUxNjEzNCIsICJuYW1lIjogIkFub255bW91cyBDYWxsaXJyaG9lIiwgImRpc3BsYXlfbmFtZSI6ICJBbm9ueW1vdXMgQ2FsbGlycmhvZSIsICJpbml0aWFscyI6ICJBQyIsICJjb2xvciI6IG51bGx9|cfa169e5bdc76d58f45a0b65997be28d8d874f9343c782d38b28215fc53de18d",
            "_xsrf": "2|829786cb|3a6ff780e4268a76b44c8f31db745582|1742320309",
        }

        data = {
            "x": "-1",
            "y": "0",
        }

        response = requests.post(url, headers=headers, cookies=cookies, data=data)

        return response.status_code
    
def get_object():
    return ['sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    
    
