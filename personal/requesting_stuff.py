import requests

valid_urls = []

for i in range(6357632, 6400000):
    response = requests.head(f"https://blackboard.staffs.ac.uk/ultra/courses/_88138_1/outline/file/_{i}_1")
    print(response.text)
    print(response.status_code)
    if response != 404:
        valid_urls.append(f"https://blackboard.staffs.ac.uk/ultra/courses/_88138_1/outline/file/_{i}_1")
