import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "difficulty": "medium",
    "category": 18,
}
response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]