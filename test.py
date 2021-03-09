import requests
BASE="http://127.0.0.1:5000/"
response  = requests.get(BASE + "video/0")
print(response.json())

data = [
    {"name":"test","likes":10,"views":100},
    {"name":"test","likes":10,"views":10},
    {"name":"test","likes":10,"views":10}
]
for i in range(len(data)):
    response  = requests.patch(BASE+"video/"+str(i) ,data[i])
    # print(response.json())
response  = requests.get(BASE + "video/0")
print(response.json())
