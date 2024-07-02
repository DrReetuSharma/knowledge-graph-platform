import requests


def fetch_url(url):
  """
  Defining a function to fetch a URL and print the result
  Moodify as required.

  Return: first 500 characters
  """

try:
        response = requests.get(url)
       # print(f"URL: {url}, Status Code: {response.status_code}")
        print(f"Content: {response.text[:500]}")  # Print the first 500 characters of the response content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

# URL to fetch
url = ' '

# Fetch the URL
