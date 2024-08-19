# Transaction Analysis Project - LendingOne

This project provides a detailed analysis of transaction data for LendingOne. The analysis is conducted using Python for data processing and Tableau for visualization. The project includes data cleaning, merging, and visualization to identify key insights into customer spending behavior.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Install Dependencies](#2-install-dependencies)
  - [3. Running the Python Scripts](#3-running-the-python-scripts)
  - [4. Running the Jupyter Notebook](#4-configure-snowflake)
  - [5. Tableau Visualization](#5-tableau-visualization)
- [Tableau Dashboard](#tableau-dashboard)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The project includes the following components:
- **Data Processing**: Python scripts for merging customer and transaction data, and uploading the processed data to Snowflake.
- **Visualization**: A Jupyter Notebook and a Tableau dashboard for visualizing transaction amounts, spending trends over time, and top customers.

## Setup Instructions

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/guilhermecarvalho18/LendingOne_Transaction_Analysis.git 
```
### 2. Install Dependencies

Ensure you have Python installed on your system. You can install the necessary Python packages using pip:

```bash
pip install -r requirements.txt
```

### 2\. Running the Python Scripts

#### Data Merging

Run the `data_merge.py` script to merge customer and transaction data:

```bash
python src/data_merge.py
```

This script performs the following tasks:

-   Reads customer and transaction data from CSV files.
-   Uses fuzzy matching to match customer names in the transaction data with those in the customer data.
-   Outputs a merged dataset to a CSV file in the `data/` directory.

#### Snowflake Ingestion

Run the `snowflake_ingestion.py` script to upload the merged data to Snowflake:

```bash
python src/snowflake_ingestion.py
```

This script performs the following tasks:

-   Connects to your Snowflake database.
-   Creates a table for the merged data if it does not already exist.
-   Uploads the data from the merged CSV file to Snowflake.

### 3\. Configure Snowflake

Before running the Snowflake ingestion script, you need to configure your Snowflake credentials. The script uses the `python-dotenv` library to load environment variables from a `.env` file.

Create a `.env` file in the root directory of the project with the following content:

```bash
SNOWFLAKE_USER=<your_snowflake_username>
SNOWFLAKE_PASSWORD=<your_snowflake_password>
SNOWFLAKE_ACCOUNT=<your_snowflake_account>
SNOWFLAKE_WAREHOUSE=<your_snowflake_warehouse>
SNOWFLAKE_DATABASE=<your_snowflake_database>
SNOWFLAKE_SCHEMA=<your_snowflake_schema>
```

Make sure to replace the placeholders with your actual Snowflake credentials.

### 4\. Running the Jupyter Notebook

If you wish to perform exploratory data analysis or further customize the analysis, you can use the provided Jupyter Notebook:

1.  Launch the Jupyter Notebook:

    ```bash
    jupyter notebook notebooks/EDA.ipynb
    ```

2.  The notebook includes steps for:

    -   Loading and exploring the customer and transaction data.
    -   Visualizing data distributions and trends.
    -   Experimenting with different data processing techniques.

### 5\. Tableau Visualization

The data analysis results are visualized using Tableau. The Tableau dashboard provides interactive insights into transaction amounts, spending trends over time, and customer spending.

You can view the Tableau dashboard here: [Transaction Analysis Dashboard](https://public.tableau.com/views/TransactionAnalysis-LendingOne/Dashboard1?:language=pt-BR&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

The dashboard includes:

-   **Distribution of Transaction Amounts**: A histogram showing the distribution of transaction amounts.
-   **Spending Over Time**: A line chart showing total spending over time.
-   **Top 10 Customers by Total Spending**: A bar chart showing the top 10 customers by their total spending.
