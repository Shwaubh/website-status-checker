from .utils import get_session
import concurrent.futures

def check_website(url, session, logger):
    try:
        response = session.get(url)
        if response.status_code == 200:
            logger.info(f"{url} is up and running")
        else:
            logger.warning(f"{url} is down - {response.status_code}")
    except Exception as e:
        logger.error(f"{url} is not reachable/available - Reason : {e}")

def check_all_website(urls, logger):
    session = get_session()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in urls:
            futures.append(executor.submit(check_website, url, session, logger))        
        concurrent.futures.wait(futures)
        