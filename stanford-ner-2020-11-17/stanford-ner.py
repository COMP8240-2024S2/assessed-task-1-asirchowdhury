import os

# Define paths
stanford_ner_jar = "stanford-ner.jar"
classifier = "classifiers/english.all.3class.distsim.crf.ser.gz"
input_files = ["wikipedia.txt", "fanwiki.txt"]
output_files = ["stanford-wikipedia.txt", "stanford-fanwiki.txt"]

# Loop through both the Wikipedia and Fandom files
for i in range(2):
    input_file = input_files[i]
    output_file = output_files[i]
    
    command = f"java -mx600m -cp '{stanford_ner_jar}:classifiers' edu.stanford.nlp.ie.crf.CRFClassifier " \
              f"-loadClassifier {classifier} -textFile {input_file} > {output_file}"
    
    print(f"Running NER on {input_file}, outputting to {output_file}")
    os.system(command)

print("Stanford NER applied successfully!")
