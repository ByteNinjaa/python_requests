import requests

print("Hello")

response = requests.get('https://jsonplaceholder.typicode.com/users')

if response.status_code == 200:
    users = response.json()
    for u in users:
        if u['company']['bs'] == "harness real-time e-markets":
            print(f"ID: {u['id']}\nName: {u['name']}\nBS: {u['company']['bs']}\n")

    print('Success!')

else:
    print('An error occured')
