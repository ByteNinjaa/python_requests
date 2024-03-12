import requests

print("Hello")

response = requests.get('https://jsonplaceholder.typicode.com/users')

if response.status_code == 200:
    users = response.json()
    user_names = []
    for u in users:
        user_names.append(u['username'])

    print("Unsorted: ", user_names, "\n")
    print("Sorted: ", sorted(user_names))

    print('Success!')

else:
    print('An error occured')
