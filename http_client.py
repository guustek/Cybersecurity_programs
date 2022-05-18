import json
import subprocess
import sys

try:
    import requests
except ImportError:
    print('"requests" module is missing, it will be installed automatically')
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
finally:
    import requests


class Action:
    GET = "1"
    POST = "2"
    DELETE = "3"
    EXIT = "4"


base_url = "https://gorest.co.in/public/v2/users"
auth_token = "296a3b30551729c976338edf0221891b798ea5ffe152af45136b3d3154189480"
headers = {"Authorization": "Bearer " + auth_token}


def get_all():
    response = requests.get(base_url, headers=headers)
    status_code = response.status_code
    reason = response.reason
    body = response.json()
    print(f"Status {status_code} {reason}\n"
          f"{json.dumps(body, indent=4)}\n")


def get_by_id(user_id):
    response = requests.get(f"{base_url}/{user_id}", headers=headers)
    status_code = response.status_code
    reason = response.reason
    body = response.json()
    print(f"Status {status_code} {reason}\n"
          f"{json.dumps(body, indent=4)}\n")


def add(user_name, user_email, user_gender, user_status):
    data = {
        "name": user_name,
        "email": user_email,
        "gender": user_gender,
        "status": user_status
    }
    response = requests.post(base_url, headers=headers, json=data)
    status_code = response.status_code
    reason = response.reason
    body = response.json()
    print("")
    print(f"Status {status_code} {reason}\n"
          f"{json.dumps(body, indent=4)}\n")


def delete(user_id):
    response = requests.delete(f"{base_url}/{user_id}", headers=headers)
    status_code = response.status_code
    reason = response.reason
    try:
        body = response.json()
    except requests.exceptions.JSONDecodeError:
        body = response.text
    print(f"Status {status_code} {reason}\n"
          f"{json.dumps(body, indent=4)}\n")


def get_posts(user_id):
    response = requests.get(f"{base_url}/{user_id}/posts", headers=headers)
    status_code = response.status_code
    reason = response.reason
    body = response.json()
    print(f"Status {status_code} {reason}\n"
          f"{json.dumps(body, indent=4)}\n")


if __name__ == "__main__":
    while True:
        print("1 - GET")
        print("2 - POST")
        print("3 - DELETE")
        print("")
        print("4 - EXIT")
        print("")
        method = input("Choose request method: ")
        match method:
            case Action.GET:
                print("")
                print("1 - All users")
                print("2 - By ID")
                print("3 - Posts by user ID")
                print("")
                request = input("Choose get request type: ")
                match request:
                    case "1":
                        print("")
                        get_all()
                    case "2":
                        print("")
                        ID = input("ID: ")
                        print("")
                        get_by_id(ID)
                    case "3":
                        print("")
                        ID = input("ID: ")
                        print("")
                        get_posts(ID)
                    case _:
                        print("\nInvalid value!\n")
            case Action.POST:
                print("")
                name = input("Name: ")
                email = input("Email: ")
                gender = input("Gender: ")
                status = input("Status: ")
                add(name, email, gender, status)
            case Action.DELETE:
                print("")
                ID = input("ID to delete: ")
                print("")
                delete(ID)
            case Action.EXIT:
                print("")
                print("Exiting...")
                print("")
                sys.exit()
            case _:
                print("\nInvalid value!\n")
