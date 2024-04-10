import requests

def bestUniversityByCountry(country):
    base_url = "https://jsonmock.hackerrank.com/api/universities"
    page_num = 1
    best_uni = None
    highest_rank = float(0)

    while True:
        url = f"{base_url}?page={page_num}"
        response = requests.get(url)
        data = response.json()

        if not data["data"]:
            break

        for university in data["data"]:
            if university.get("location").get("country") == country:
                if university.get("score") > highest_rank:
                    best_uni = university["university"]
                    highest_rank = university["score"]

        page_num += 1

    return best_uni

if __name__ == '__main__':
    country = input("Enter country: ")
    result = bestUniversityByCountry(country)
    print(result)
