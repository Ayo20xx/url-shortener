from urllib.parse import urlparse, urlunparse
user=input("enter url")
rs=urlparse(user)

while True:
    if rs.scheme == "http"or "https" :
        print("this is a legit url")
         break
    else:  
