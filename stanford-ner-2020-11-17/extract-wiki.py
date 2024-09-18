import wikipediaapi

# Set up a custom User-Agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; AsirBot/1.0; +http://www.example.com/bot)'
}

# Initialize Wikipedia API without passing 'user_agent' directly
wiki = wikipediaapi.Wikipedia('en', headers=headers)

# Define the page name for the actor Tom Holland
page_name = 'Tom_Holland'

# Extract the page for Tom Holland
page = wiki.page(page_name)

# Check if the page exists and write the main text to a file
if page.exists():
    with open('wikipedia.txt', 'w') as f:
        f.write(page.text)
    print(f"Extracted main text from the Wikipedia page for {page_name} successfully!")
else:
    print(f"Wikipedia page for {page_name} not found.")
