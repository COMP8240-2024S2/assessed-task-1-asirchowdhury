#!/bin/bash

# Run evaluation on Fixed Wikipedia NER and save to file
echo "Evaluating Fixed Wikipedia NER"
java -mx1g -cp /workspaces/assessed-task-1-asirchowdhury/stanford-ner-2020-11-17/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier \
-loadClassifier /workspaces/assessed-task-1-asirchowdhury/stanford-ner-2020-11-17/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz \
-testFile wikipedia-gold.txt -outputFormat slashTags > wikipedia-eval.txt

# Run evaluation on Fixed Fanwiki NER and save to file
echo "Evaluating Fixed Fanwiki NER"
java -mx1g -cp /workspaces/assessed-task-1-asirchowdhury/stanford-ner-2020-11-17/stanford-ner-2020-11-17/stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier \
-loadClassifier /workspaces/assessed-task-1-asirchowdhury/stanford-ner-2020-11-17/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz \
-testFile fanwiki-gold.txt -outputFormat slashTags > fanwiki-eval.txt
