README.md

Project Overview

This Assesment task used Stanford NER (Named Entity Recognizer) to tag entities in two types of texts: Wikipedia and Fanwiki. The objective of this task was to evaluate how well the pre-trained model recognizes entities such as persons, organizations, and locations and to further improve the model’s performance by fixing issues related to the tagging of punctuation as entities.


1. Extraction of Data
Wikipedia: Used a script (extract-wiki.py and extract-fanwiki.py) to download and extract the Wikipedia entry for Tom Holland as the task mentioned to choose any actor.

Fanwiki: Extracted information using fandom-py to gather details on Jonathan Joestar from JoJo’s Bizarre Adventure. I extracted information on his personality and since my id ended with 0 so i got him as my character.
Then I Saved extracted content to wikipedia.txt and fanwiki.txt.

2. Initial NER Tagging
Ran Stanford NER using the stanford-ner.py script to tag named entities (e.g., PERSON, ORGANIZATION, LOCATION) on the Wikipedia and Fanwiki texts.
Saved the initial tagging results to stanford-wikipedia.txt and stanford-fanwiki.txt.

3. Manual Correction
Manually checked the initial tagging and created gold standard files: wikipedia-gold.txt and fanwiki-gold.txt by correcting any errors.

4. Evaluation

Evaluated the performance of the NER model using the eval.sh script.
This evaluation generated the precision, recall, and F1-scores for entities in both texts.
The results showed 100% precision, recall, and F1-scores for both the Wikipedia and Fanwiki datasets, even before applying fixes.

5. Fixing Punctuation Issues

Wrote a script (fix-ner.py) that scans the gold standard files and ensures that any punctuation is tagged as /O.
Re-ran the evaluation using the eval.sh script after the fix.
Testing the Fix: After applying the fix-ner.py script to wikipedia-gold.txt and fanwiki-gold.txt, the NER evaluation was run again. The results remained unchanged, which suggests that punctuation was already handled correctly. However, I verified the script by manually changing a punctuation mark to a name, and the script correctly fixed the error when re-run.

Final Outputs

The final evaluation results showed that the model achieved:

Precision, Recall, and F1 Scores:
Wikipedia: Precision = 1.0000, Recall = 1.0000, F1 = 1.0000
Fandom: Precision = 1.0000, Recall = 1.0000, F1 = 1.0000
These results remained consistent before and after applying the fix-ner.py script.


6. Use of AI Tools

AI tools were used at several points during the project to assist in debugging issues, refining the code, and gaining a better understanding of the evaluation process.

Reproducibility

To reproduce the results:

Data Extraction: Run extract-wiki.py and the Fandom extraction script to gather the text files.
Run Stanford NER: Use the provided NER script to generate initial entity-tagged files.
Manual Gold Standard Creation: Correct the initial tagging results manually to generate wikipedia-gold.txt and fanwiki-gold.txt.
Evaluation: Run eval.sh to evaluate the Stanford NER model’s performance.
Fix NER: Apply the fix-ner.py script to handle punctuation tagging and rerun the evaluation.