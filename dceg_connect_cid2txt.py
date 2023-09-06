#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import requests
import re
import sys
import os
import certifi  # Import the certifi package

## Files and uris
# Get csv filename from command line arg. ToDo: sloppy, no error checking.
csv_file = sys.argv[-1]
filename = os.path.splitext(csv_file)[0]

# Get the data dictionary json file from github
c4cp_dictionary_url = 'https://raw.githubusercontent.com/episphere/conceptGithubActions/master/aggregateCopy.json'
c4cp_req = requests.get(c4cp_dictionary_url, verify=False)
c4cp_req.close()
c4cp_dict = c4cp_req.json()

# "No" and some other values following are messed up in the json dictionary. Fix them.
c4cp_dict['104430631']['Variable Name'] = 'No'
c4cp_dict['181769837']['Variable Name'] = 'Other'
c4cp_dict['178420302']['Variable Name'] = 'Unknown/Unavailable'

## Read CSV file into dataframe. This will be a df using concept IDs (i.e. the numerical codes) as column headers and values. Hence cid_df.
cid_df = pd.read_csv(csv_file, dtype=str, keep_default_na=False)
cid_df = cid_df.reindex(sorted(cid_df.columns), axis=1)

# Display
#cid_df.info()

## Concatenated column header patterns seen are:
#   Connect_ID
#   token
#   d_<concept_id>
#   d_<concept_id>_d_<concept_id>
#   d_<concept_id>_d_<concept_id>_d_<concept_id>
#   state_d_<concept_id>
#   state_d_<concept_id>_d_<concept_id>
#   state_state_d_<concept_id>
#   state_state_d_<concept_id>_d_<concept_id>

## Get the column headers as index object
headers_idx = cid_df.columns

## Split the concatenated concept_ids found in a single column header into an array; turn the array into a multi-index for a new dataframe using multi-row column headers
cid_headers_orig = cid_df.columns.values.tolist()
# Get column headers as a list of lists of concept IDs
cid_headers_list = [(re.findall(r'(?:state|\d{9})', header)) if re.search(r'd_\d{9}', header) else [header, ] for header in cid_headers_orig]
# Front-pad lists with null to length of longest list - needed to create multi-index
max_depth = max([len(header) for header in cid_headers_list])
cid_headers_list = [np.pad(header, (4 - len(header), 0), 'constant', constant_values=('',)).tolist() for header in cid_headers_list]
cid_headers_list = [tuple(header) for header in cid_headers_list]

# Create a multi-index, then use it as the new headers for the dataframe.
cid_headers_midx = pd.MultiIndex.from_tuples(cid_headers_list)

# Create a NEW dataframe: copy the original, keeping the original concept ID dataframe for other possible use.
# midx_cid_df = cid_df.copy()
# Replace the column headers index with the multi-index. Dataframe now has 4 rows of column headers vs the original 1 row.
# midx_cid_df.columns = cid_headers_midx

## Convert CID-based headers to text-based headers. Use 'Variable Name' value from data dictionary. (Why is it an array in the JSON?)
def func1(x):
    y = [(c4cp_dict.get(i, {}).get('Variable Name') if re.match(r'\d{9}', i) else i) for i in x]
    z = [i[0] if isinstance(i, list) else i for i in y]
    return tuple(z)
txt_headers_midx = cid_headers_midx.map(func1)

## Create a copy of the dataframe that uses text (Variable Name) instead of concept IDs as the column headers.
midx_txt_df = cid_df.copy()
midx_txt_df.columns = txt_headers_midx

## Transform every cell in dataframe using concept ID to text 'Variable Name' map
def func2(x):
    j = c4cp_dict.get(str(x), {}).get('Variable Name', None) if re.match(r'^\d{9}$', str(x)) else x
    return j
midx_txt_df = midx_txt_df.applymap(func2, na_action='ignore')

## Export the dataframe as multirow header column Excel spreadsheet and CSV
midx_txt_df.to_excel(filename + '.xlsx', sheet_name='cid_2_txt')
