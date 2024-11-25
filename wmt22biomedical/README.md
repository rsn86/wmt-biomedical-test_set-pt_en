# [WMT 2022 Biomedical](https://www.statmt.org/wmt22/biomedical-translation-task.html)

For the test set of Medline abstracts, the format will be plain text files. The format will be the following:

DOC_ID	SENT_ID	SENTENCE_TEXT

The three values are separated by a TAB character:

    DOC_ID: sequential one, e.g. doc1, doc8, not the original PMID in Medline
    SENT_ID: a sequential number from 1 to n
    SENTENCE_TEXT: the sentence text to be translated by the participants

```
doc1	1	sentence_1
doc2	2	sentence_2
doc2	3	sentence_3
doc2	4	sentence_4
doc2	5	sentence_5
...
doc2	n	sentence_n
doc4	1	sentence_1
doc4	2	sentence_2
...
```

The Medline test files are available in the WMT'22 biomedical task [Google Drive Folder](https://drive.google.com/drive/folders/1W_zVbS5yb921bpSZW-Ca9nKoWXmim1xU?usp=sharing).

