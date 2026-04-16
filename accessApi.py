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

def run_summary_tool():
    # Print a welcome message as shown in the example. "Welcome to the Book of Mormon Summary Tool!"
    print("Welcome to the Book of Mormon Summary Tool!")
    # Use a while loop to allow the user to input a book and chapter
    while True:
    # Ask the user for the book and chapter they would like to view a summary of
        #books_menu = {"_id":"bookofmormon","books":[{"_id":"1nephi","title":"1 Nephi"},{"_id":"2nephi","title":"2 Nephi"},{"_id":"jacob","title":"Jacob"},{"_id":"enos","title":"Enos"},{"_id":"jarom","title":"Jarom"},{"_id":"omni","title":"Omni"},{"_id":"wordsofmormon","title":"Words of Mormon"},{"_id":"mosiah","title":"Mosiah"},{"_id":"alma","title":"Alma"},{"_id":"helaman","title":"Helaman"},{"_id":"3nephi","title":"3 Nephi"},{"_id":"4nephi","title":"4 Nephi"},{"_id":"mormon","title":"Mormon"},{"_id":"ether","title":"Ether"},{"_id":"moroni","title":"Moroni"}],"title":"Book of Mormon","titleOfficial":"The Book of Mormon","titleShort":"BoM"}
    #Reduced the code instead of bring the entire json object that is extensive , Had better get the url of the api has the object , then convert it to a item readable for python in order to iterate to it and finally printing the books , needed to display to the terminal and user can look up and choose a books
        url_books = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon'
        get_books = requests.get(url_books)
        convert_to_json = get_books.json()
        print("List of the books\n")
        for i in range(len(convert_to_json["books"])):
            print(f"({i}) {convert_to_json["books"][i]["title"]}")
        print()
        try:
            book = input("Choose a Book: ").capitalize()
            chapter = int(input("Choose a chapter: "))
    # Use the get_summary() function to retrieve the summary and print it
            get_summary(book,chapter)
    # If the book or chapter is invalid, catch the KeyError and print an error message
        except KeyError:
            print("Please enter a exist book")
    # Ask the user if they would like to view another summary
        ask = input("Would do you like another summary?(y/n): ")
    # If the user does not want to view another summary, print "Thank you for using Book of Mormon Summary Tool!"
        if ask == "n":
            print("\"Thank you for using Book for Mormon Summary Tool!\"")
    # do not forget to finish or break the loop
            break

if __name__ == "__main__":
    run_summary_tool()