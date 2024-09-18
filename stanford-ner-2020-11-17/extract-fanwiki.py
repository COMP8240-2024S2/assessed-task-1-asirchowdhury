import fandom

# Set the wiki to JoJo's Bizarre Adventure
fandom.set_wiki("jojo")

# Search for Jonathan Joestar (your character based on the last digit of your student ID)
search_results = fandom.search("Jonathan Joestar", results=1)
print(f"Search Results: {search_results}")

# Extract the page for Jonathan Joestar
page = fandom.page(title="Jonathan Joestar")

# Open fanwiki.txt and write the content
with open("fanwiki.txt", "w", encoding="utf-8") as f:
    f.write(f"Title: {page.title}\n")
    f.write(f"URL: {page.url}\n\n")
    f.write(f"Summary:\n{page.summary}\n\n")

    # Writing sections to the file
    f.write("Sections:\n")
    for section in page.sections:
        f.write(f"{section}\n")

print("Data has been written to fanwiki.txt")
