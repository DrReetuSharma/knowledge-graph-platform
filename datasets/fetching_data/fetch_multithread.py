import threading
import requests

# Function to fetch multiple URLs concurrently
def fetch_urls_concurrently(urls):
    def fetch_url(url):
        try:
            response = requests.get(url)
            print(f"URL: {url}, Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# List of URLs to fetch
urls = [
    ' ',
    ' ',
    ' '
]

# Fetch the URLs concurrently
fetch_urls_concurrently(urls)
