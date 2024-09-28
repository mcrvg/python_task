import json
#Create a new file servers.json

servers= {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

with open('servers.json', 'w') as f:
    json.dump(servers, f, indent=4)

#Use 'with' to open the file created above

with open('servers.json', 'r') as f:
  data = json.load(f)

#Parse contents the JSON file into a Python dictionary named "servers"
with open('servers.json', 'r') as f:
    servers = json.load(f)

#type
print(type(servers)) #class<dict>

#Print out the dictionary record with the key "server1"
print(servers['server1'])
#Print out the dictionary record with the key "server2"
print(servers['server2'])
#print  all keys and values
for server_name, server_data in servers.items():
        print(f"Server Name: {server_name}")
        for key, value in server_data.items():
            print(f"  {key}: {value}")






