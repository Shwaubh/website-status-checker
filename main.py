# Application and Business Logic
import requests
import csv
import time

WEBSITE_FILE = "websites.txt"
RESULT_FILE = "results.csv"

def read_websites():
    try:
        with open(WEBSITE_FILE, "r") as file:
            websitelist = []
            for line in file.readlines():
                websitelist.append(line.strip())
            return websitelist
    except FileNotFoundError:
        print("Websites.txt file is not found")
        return []

def check_website_status(website, retries = 3):
    for attempt in range(retries):
        try:
            response = requests.get(website, timeout = 5)
            return response.status_code # 200, 400, 404, etc
        except requests.ConnectionError:
            print("Connection Error to website : ", website)
        except requests.Timeout:
            print("Timeout Error to website : ", website)
        except requests.RequestException as e:
            print("Error : ", e)
        time.sleep(2)
    return "Failed"

def write_results(results):
    with open(RESULT_FILE, 'w') as file:
        writer = csv.writer(file)  
        writer.writerow(["Website", "Status Code"])
        writer.writerows(results)

def main():
    websites = read_websites()
    if not websites:
        print("No websites to check")
        return
    results = []
    print("Website Status check started")
    for website in websites:
        status = check_website_status(website)
        results.append([website, status])
        print(website, " - Status : " ,status)

    write_results(results)
    print("Results saved in 'results.csv'")

if __name__ == "__main__":
    main()