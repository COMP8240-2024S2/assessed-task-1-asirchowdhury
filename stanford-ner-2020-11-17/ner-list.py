import re

# Function to extract and list NERs from the input file, keeping multi-word entities together
def extract_ner(input_file, output_file):
    # Pattern to match NER tags (e.g., Timothy/PERSON)
    pattern = re.compile(r'(\w+)/(\w+)')

    # List to store named entities (in order of appearance)
    entities = []
    current_entity = []  # To accumulate multi-word entities
    current_tag = None

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            matches = pattern.findall(line)
            for match in matches:
                word, ner_tag = match
                # Only keep words with valid NER tags (PERSON, ORGANIZATION, LOCATION)
                if ner_tag in ["PERSON", "ORGANIZATION", "LOCATION"]:
                    if current_tag == ner_tag:
                        # If the current tag is the same as the previous one, keep adding to the current entity
                        current_entity.append(word)
                    else:
                        # If it's a new entity, store the previous one and reset
                        if current_entity:
                            entities.append(" ".join(current_entity))
                        current_entity = [word]
                        current_tag = ner_tag
                else:
                    # If the word doesn't have a valid NER tag, store the current entity and reset
                    if current_entity:
                        entities.append(" ".join(current_entity))
                    current_entity = []
                    current_tag = None

    # Add any remaining entity
    if current_entity:
        entities.append(" ".join(current_entity))

    # Write the unique entities to the output file, one per line (in order of appearance)
    with open(output_file, 'w', encoding='utf-8') as file:
        for entity in entities:
            file.write(entity + '\n')

# Extract NERs for stanford-wikipedia.txt
extract_ner("stanford-wikipedia.txt", "ner-list-wikipedia.txt")

# Extract NERs for stanford-fanwiki.txt
extract_ner("stanford-fanwiki.txt", "ner-list-fanwiki.txt")

print("NER list been written to ner-list-wikipedia.txt and ner-list-fanwiki.txt")
