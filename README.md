# cid_mapping_tools
We'll use this repo to share tools for mapping Connect for Cancer Prevention Concept IDs to human readable variable labels.

### dceg_connect_cid2txt.py 

Converts the deidentified_recruitment "SITE_deidentified_recruitment_data.csv" file to an excell file with the Concept IDs swapped out for human-readable text using the Data Dictionary. Written by Martin Ferguson.

#### Usage:

```python3 dceg_connect_cid2txt.py SITE_deidentified_recruitment_data.csv```

Remember that both the .py file and the .csv file should be in the same folder.
