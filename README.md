<<<<<<< HEAD
# Bitext Customer Support Dataset Analysis

## 1. Project Overview

This project performs exploratory data analysis (EDA) and data quality checks on the Bitext Customer Support LLM Chatbot Training Dataset. The dataset is loaded directly from Hugging Face and analyzed using Python and Pandas.

The main objective is to understand the dataset's structure, examine customer support intent and category distributions, identify missing and duplicate records, and assess the dataset's suitability for machine learning-based customer request classification.

## 2. Dataset Source

- **Dataset:** Bitext Customer Support LLM Chatbot Training Dataset
- **Platform:** Hugging Face
- **URL:** https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset
- **Split:** `train`

## 3. Project Structure

```text
project/
├── bittext_data_analysis.py
├── README.md
└── requirements.txt
```

## 4. Requirements

The project uses the following Python libraries:

- `pandas` — for data manipulation and analysis.
- `datasets` — for loading the dataset from Hugging Face.

Install the dependencies using:

```bash
pip install pandas datasets
```

Alternatively, create a `requirements.txt` file containing:

```text
pandas
datasets
```

Then run:

```bash
pip install -r requirements.txt
```

## 5. How to Run the Script

Make sure Python is installed and an internet connection is available to download the dataset.

Run the following command from the project directory:

```bash
python bittext_data_analysis.py
```

The script downloads the training split from Hugging Face, converts it into a Pandas DataFrame, and prints the analysis results to the terminal.

## 6. Analysis Performed

The script performs the following checks:

1. **Dataset structure:** Displays the number of rows, columns, and data types.
2. **Missing values:** Counts missing values in each column and displays affected records.
3. **Duplicate records:** Counts completely duplicated rows.
4. **Duplicate customer requests:** Identifies repeated `instruction` texts.
5. **Intent distribution:** Displays the frequency of each intent and the number of unique intents.
6. **Intent class percentages:** Calculates the percentage distribution of intent labels.
7. **Instruction length:** Calculates the mean, median, minimum, and maximum word counts.
8. **Conflicting intents:** Identifies identical instructions associated with multiple intent labels.
9. **Category distribution:** Examines category frequencies and the number of unique intents per category.
10. **Rare categories:** Identifies categories with fewer than five records.
11. **Blank instructions:** Counts instructions that are empty or contain only whitespace.

## 7. Expected Results

When executed, the script prints descriptive statistics and data quality information, including:

- Dataset dimensions and column data types.
- Missing-value and duplicate-record counts.
- Repeated customer requests.
- Intent and category distributions.
- Intent class percentages.
- Customer instruction length statistics.
- Instructions associated with multiple intents.
- Rare categories and blank instructions.

The exact results depend on the dataset version downloaded from Hugging Face.

## 8. Relevance to Machine Learning

The analysis helps determine whether the dataset is appropriate for supervised customer support text classification.

The findings can guide subsequent steps, including data cleaning, duplicate handling, class imbalance analysis, text preprocessing, feature extraction, and model selection.

The dataset can be used to investigate classification algorithms such as Naive Bayes, Logistic Regression, Support Vector Machines, Decision Trees, and Random Forest.

## 9. Limitations

This script focuses on exploratory analysis and data quality assessment. It does not perform text preprocessing, train machine learning models, or calculate classification performance metrics.

Repeated instructions are not automatically errors, and instructions associated with multiple intents require further investigation before any records are removed.

The rare-category threshold of fewer than five records is an exploratory choice and does not necessarily indicate that a category should be excluded.

Duplicate detection uses exact text matching and does not identify semantically similar requests with different wording.

## 10. Future Improvements

Possible extensions include:

- Visualizing intent and category distributions.
- Applying text cleaning and normalization.
- Investigating class imbalance and duplicate records.
- Splitting the dataset into training, validation, and test sets.
- Training and comparing classification algorithms.
- Evaluating models using accuracy, precision, recall, F1-score, and Matthews correlation coefficient (MCC).

## 11. Dataset Attribution

Bitext. *Bitext Customer Support LLM Chatbot Training Dataset*. Hugging Face.

https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset

Refer to the dataset card for licensing and usage conditions.
=======
# Customer-Request-Classification
>>>>>>> 6560a608457a39ccd412368b5fc511ca38211c88
