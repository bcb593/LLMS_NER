import json
import pickle
import os

with open("./data/rft_clauses_final.json", "r") as file:
    rft_clauses_final = json.load(file)

"""
JSON SCHEMA
rft_clauses:
    document_index:
        doc_filename:
        clauses:
            clause_type1: clause_list
            clause_type2: clause_list
                .
                .
                .
            clause_type41: clause_list
        locations:
            clause_type1: clause_Loc_dict
            clause_type2: clause_Loc_dict
                .
                .
                .
            clause_type41: clause_Loc_dict
"""

N = len(rft_clauses_final)
dataset_filepath = 'C:\\Users\\john\\LLM_NER_DATA\\CUAD_v1'
text_doc_folder = 'full_contract_txt'
text_doc_filepath = os.path.join(dataset_filepath, text_doc_folder)

docs_in_str = []

# Files that could not be found or read correctly with the error type
# Contains tuple -> (filename, error_type)
file_error_type = []

for i in range(N):
    # File Retrieval Section:
    index = str(i)
    filename = rft_clauses_final[index]["doc_filename"]
    
    # Handles file not found & read file errors
    try:
        # Attempts to open file at specified location
        with open(os.path.join(text_doc_filepath,filename), 'r') as file:
                # Attempts to read file into string removing & replacing '\n' with ' '
                doc_text = file.read().replace('\n', ' ')
                docs_in_str.append(doc_text)
    except Exception as e:
        docs_in_str.append("ERROR")
        file_error_type.append((filename,type(e)))
        continue
        
with open("./data/docs_in_str.ob", 'wb') as fp:
    pickle.dump(docs_in_str, fp)