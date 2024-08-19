import pandas as pd
from fuzzywuzzy import fuzz, process

# Load the datasets containing customer information and transaction records
customers = pd.read_csv("data/customers.csv")
transactions = pd.read_csv("data/transactions.csv")

# Function to perform fuzzy matching on customer names
def match_name(name, list_names, min_score=0):
    max_score = -1
    max_name = ""
    for name2 in list_names:
        # Calculate the similarity score between the transaction name and each customer name
        score = fuzz.ratio(name, name2)
        # Update max_name and max_score if the score exceeds both the minimum score and the current max_score
        if (score > min_score) & (score > max_score):
            max_name = name2
            max_score = score

    return (max_name, max_score)


customers_names = customers["customer_name"].to_list()


dict_list = []

# Iterate over each transaction record
for i, transaction_row in transactions.iterrows():
    name = transaction_row["customer_name"]  
    match = match_name(name, customers_names, 75)  # Perform fuzzy matching with a minimum score of 75

    # Create a dictionary to store the transaction and matching results
    dict_ = {}
    dict_["transaction_id"] = transaction_row["transaction_id"]  
    dict_["customer_name"] = name  
    dict_["match_name"] = match[0]  

    dict_["amount"] = transaction_row["amount"]  
    dict_["transaction_date"] = transaction_row["transaction_date"]  

    # If a match was found, retrieve the corresponding email from the customers dataset
    if match[0]:
        customer_row = customers[customers["customer_name"] == match[0]]
        dict_["email"] = customer_row["email"].values[0] if not customer_row.empty else None
    else:
        dict_["email"] = None  

    
    dict_list.append(dict_)

merged_table = pd.DataFrame(dict_list)

merged_table.to_csv('data/merged_table.csv', index=False)
