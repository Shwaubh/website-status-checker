from checker.logger import setup_logger
from checker.fetcher import fetch_urls
from checker.status_checker import check_all_website

def main():
    logger = setup_logger()
    urls = fetch_urls("websites.txt")
    check_all_website(urls, logger)

if __name__ == "__main__":
    main()