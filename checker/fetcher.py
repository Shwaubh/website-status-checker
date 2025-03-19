# Read URLs

def fetch_urls(file_path):
    urls = []
    with open(file_path, 'r') as file:
        for url in file.readlines():
            urls.append(url.strip())
    return urls

# print(fetch_urls('../websites.txt'))