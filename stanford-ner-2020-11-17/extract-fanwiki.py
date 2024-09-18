import fandom

# Set the wiki to "Jojo"
fandom.set_wiki("jojo")

# Search for the character by name (Jonathan Joestar, based on your student ID)
search_result = fandom.search("Jonathan Joestar", results=1)
print(f"Search Results: {search_result}")

# Fetch the page of the character
page = fandom.page(title="Jonathan Joestar")

# Extract the "Personality" section
personality_section = page.section("Personality")

# Check if the section is available
if personality_section:
    content = f"Title: {page.title}\nURL: {page.url}\n\nPersonality:\n{personality_section}"
else:
    content = f"Title: {page.title}\nURL: {page.url}\n\nPersonality section not found."

# Write the content to fanwiki.txt
with open("fanwiki.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("Personality section has been written to fanwiki.txt")
