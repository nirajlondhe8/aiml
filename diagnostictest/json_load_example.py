import json


def main():
    sample_data = {
        "username": "niraj",
        "followers": 120,
    }

    with open("twitter.json", "w") as file:
        json.dump(sample_data, file)

    with open("twitter.json") as file:
        data = json.load(file)

    print(data)
    print(data["username"])


if __name__ == "__main__":
    main()
