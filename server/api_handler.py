# Send ip address to server
import socket
import fcntl
import struct
import requests as req
import socket as sock

BASE_URL = "https://boiling-reef-89836.herokuapp.com/lock_owners/"

AUTH_TOKEN = -1


def get_auth_token(username="smart-lock-admin", password="copyandpaste"):
    route = 'api/authenticate/'
    params = {"username": username, "password": password}
    token_str = req.post(BASE_URL + route, params).json()
    
    AUTH_TOKEN = token_str["token"]
    print(AUTH_TOKEN)

    return token_str["token"]

# Add endpoint and handler for the embedding


get_auth_token()



def get_user():
    route = 'api/owners/'
    params = {"Authorization": AUTH_TOKEN}
    res = req.get(BASE_URL + route, params).json()

    #id = res[0]["id"]
    #route = 'api/owners/' + str(id)
    #params = {"Authorization": AUTH_TOKEN}
    #res = req.get(BASE_URL + route, params).json()
    print (res)
    return res

user_info = get_user()[0]

def get_ip():
    s = sock.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_addr = s.getsockname()[0]
    print(ip_addr)
    s.close()
    return ip_addr

get_ip()


def get_public_ip():
    return req.get("https://api.ipify.org/?format=json").json()["ip"]

def get_lock(lock_owner=user_info["id"]):
    route = 'api/locks/'
    params = {"Authorization": AUTH_TOKEN, "lock_owner": lock_owner}
    res = req.post(BASE_URL + route, params).text
    print(res)
    return


lock_info = get_lock()

def create_lock(lock_owner=user_info["id"], address="54 Brett Rd., Piscataway, NJ", ip_address=get_ip()):
    route = 'api/locks/'
    params = {"Authorization": AUTH_TOKEN, "lock_owner": lock_owner, "address": address, "ip_address": ip_address}
    req.post(BASE_URL + route, params)
    return


def post_ip_address(lock_owner=user_info["id"], address="54 Brett Rd., Piscataway, NJ", ip_address=get_ip()):
    route = 'api/locks/'
    params = {"Authorization": AUTH_TOKEN, "lock_owner": lock_owner, "address": address, "ip_address": ip_address}
    req.patch(BASE_URL + route, params)
    return

post_ip_address()

lock_info = get_lock()


def post_srn(lat, longitude, date_str, lock_id):
    route = 'api/srn/'
    params = {"Authorization": AUTH_TOKEN, "latitude": lat, "longitude": longitude, "stranger_report_time": date_str, "lock": lock_id}

    req.post(BASE_URL + route, params)
    return


def send_sms(phone_number, message):
    route = "api/notify/"
    params = {"Authorization": AUTH_TOKEN, "dest": phone_number, "content": message}
    req.get(BASE_URL + route, params)
    return 