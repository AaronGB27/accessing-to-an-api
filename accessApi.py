import requests
def get_summary(book, chapter):
    base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'
    # TODO: Create a URL string that will access the API for the given book and chapter
    # HINT: The URL should be in the format f"{base_url}{book.lower()}/{chapter}"
    url_spec = f"{base_url}{book.lower()}/{chapter}"
    # HINT: Use the requests.get() method to access the API and return the JSON data
    data = requests.get(url_spec)
    # HINT: Extract the summary from the JSON data and return it
    print(data.json()["chapter"]["summary"])