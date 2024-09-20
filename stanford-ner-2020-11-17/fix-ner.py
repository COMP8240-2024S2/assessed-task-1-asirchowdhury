import string

def fix_ner(filename):
    punctuation = set(string.punctuation)

    # Read the original file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Open the same file to overwrite it with updates
    with open(filename, 'w') as file:
        for line in lines:
            parts = line.strip().split('\t')

            # Ensure that the line has exactly two parts: word and NER tag
            if len(parts) == 2:
                word, ner_tag = parts

                # Check for punctuation or mis-tagged punctuation
                if word in punctuation or ner_tag in punctuation:
                    ner_tag = 'O'  # Set the tag to 'O' instead of '/O'

                # Write the modified or unchanged line back to the file
                file.write(f"{word}\t{ner_tag}\n")
            else:
                # If the line doesn't conform, keep it unchanged
                file.write(line)

# Fix both files in place
fix_ner("wikipedia-gold.txt")
fix_ner("fanwiki-gold.txt")
