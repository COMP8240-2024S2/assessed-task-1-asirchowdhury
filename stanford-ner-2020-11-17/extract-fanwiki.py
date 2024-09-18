import fandom

# Set the wiki to "Jojo"
fandom.set_wiki("jojo")

# Search for the character by name (Jonathan Joestar, based on your student ID)
search_result = fandom.search("Jonathan Joestar", results=1)
print(f"Search Results: {search_result}")

# Fetch the page of the character
page = fandom.page(title="Jonathan Joestar")

# Prepare the content to write to fanwiki.txt
content = f"Title: {page.title}\nURL: {page.url}\n\nSummary:\n{page.summary}\n\nSections:\n"
sections = "\n".join(page.sections)
content += sections

# Write the content to fanwiki.txt, making sure newlines are included
with open("fanwiki.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("Data has been written to fanwiki.txt")
