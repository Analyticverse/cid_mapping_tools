# cid_mapping_tools
We'll use this repo to share tools for mapping Connect for Cancer Prevention Concept IDs to human readable variable labels.

## Concept ID Converter written by Martin Ferguson

This Python script (`dceg_connect_cid2txt.py`) is designed to convert Concept IDs (CIDs) in a given CSV file (`SITE_deidentified_recruitment_data.csv`) into their corresponding textual representations using a predefined data dictionary. The script processes the CSV file and creates an Excel spreadsheet with a multirow header column and a corresponding CSV file containing the converted data.

A Excel version of our data dictionary can be found here: https://github.com/Analyticsphere/ConnectMasterAndSurveyCombinedDataDictionary

### Prerequisites

- Python 3.x
- Required Python libraries: pandas, numpy, requests, openpyxl

Install the required libraries using the following command:

```bash
pip install pandas numpy requests openpyxl
```

Note: If you are on a Windows machine, this might work better:

```bash
py -m pip install pandas numpy requests openpyxl
```

### Usage

1. Save the provided Python script (`dceg_connect_cid2txt.py`) in your desired directory.

2. Download or create a CSV file (`deidentified_recruitment_data.csv`) that you want to process.

3. Open a terminal or command prompt.

4. Navigate to the directory where you saved the script using the `cd` command:

   ```bash
   cd /path/to/script/
   ```

5. Run the script using the following command, providing the name of your CSV file as an argument:

   ```bash
   python dceg_connect_cid2txt.py deidentified_recruitment_data.csv
   ```

   Replace `deidentified_recruitment_data.csv` with the actual name of your CSV file.

6. The script will process the CSV file, convert concept IDs to textual representations, and create an Excel spreadsheet (`deidentified_recruitment_data.xlsx`) with a multirow header column. 

### Notes

Please note that an active internet connection is required to run the script since it fetches data from a remote URL using the `requests` library.

Make sure to replace `/path/to/script/` with the actual path where you save the `dceg_connect_cid2txt.py` script and `deidentified_recruitment_data.csv` file.
