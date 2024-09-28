#Import JSON
import json

#create dictionary
servers_dict = {
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
# Convert dictionary to JSON string
json_string = json.dumps(servers_dict)
print(json_string)

#Convert this Python dictionary to a JSON file

with open("data.json", "w") as f:
    f.write(json_string)

print("JSON data written to data.json")
