
import pandas as pd

# Import the official Hugging Face datasets library
from datasets import load_dataset 
print("Downloading and loading dataset directly from Hugging Face...")

# Load the dataset split straight from the cloud hub
hf_dataset = load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset", split="train")

# Convert the Hugging Face dataset object into a standard Pandas DataFrame
df = hf_dataset.to_pandas()

# 1. Dataset structure
print("DATASET STRUCTURE")
rows, columns = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")
print("\nData types per column:")
print(df.dtypes)

# 2. Missing values
print("\nMISSING VALUES")
missing_values = df.isnull().sum()
print(missing_values)
print(f"Total missing values: {missing_values.sum()}")

# Show rows containing missing values
print("\nROWS WITH MISSING VALUES")
print(df[df.isnull().any(axis=1)])

# 3. Duplicate records
print("\nDUPLICATE RECORDS")
duplicated_rows = df.duplicated().sum()
print(f"Number of fully duplicated rows: {duplicated_rows}")

# 4. Duplicate customer requests
print("\nDUPLICATE CUSTOMER REQUESTS")
duplicated_requests = df["instruction"].duplicated().sum()
print(f"Number of repeated instruction entries: {duplicated_requests}")

# Count unique instruction texts that appear more than once
repeated_text_counts = df["instruction"].value_counts()
unique_repeated_texts = (repeated_text_counts > 1).sum()

print("Number of unique instruction texts appearing more than once:",
      unique_repeated_texts)

# 5. Intent distribution
print("\nINTENT DISTRIBUTION")
intent_counts = df["intent"].value_counts(dropna=False)
print(intent_counts)

print(f"\nNumber of unique intents: {df['intent'].nunique()}")

# 6. Intent class percentages
print("\nINTENT CLASS PERCENTAGES")
intent_percentages = df["intent"].value_counts(normalize=True) * 100
print(intent_percentages.round(2))

# 7. Instruction length
print("\nINSTRUCTION LENGTH (WORDS)")
word_counts = (
    df["instruction"].dropna().astype(str).str.split().str.len()
)

print(f"Mean words: {word_counts.mean():.2f}")
print(f"Median words: {word_counts.median():.2f}")
print(f"Minimum words: {word_counts.min()}")
print(f"Maximum words: {word_counts.max()}")

# 8. Repeated instructions with different intents
print("\nREPEATED INSTRUCTIONS WITH DIFFERENT INTENTS")

valid_instructions = df.dropna(subset=["instruction", "intent"])

instruction_intent_counts = (
    valid_instructions.groupby("instruction")["intent"].nunique()
)

conflicting_instructions = instruction_intent_counts[
    instruction_intent_counts > 1
]

print("Number of instruction texts with multiple intents:",
      len(conflicting_instructions))

if not conflicting_instructions.empty:
    print("\nExamples of conflicting instructions:")
    print(conflicting_instructions.head(10))

# 9. Number of categories
print("\nCATEGORY DISTRIBUTION")
print("Number of categories:", df["category"].nunique())

print("\nRecords per category:")
print(df["category"].value_counts(dropna=False))

print("\nNumber of intents per category:")
print(df.groupby("category", dropna=False)["intent"].nunique())

# 10. Check unusual or rare category values
print("\nRARE CATEGORY VALUES")

category_counts = df["category"].value_counts(dropna=False)
rare_categories = category_counts[category_counts < 5]

print("Categories with fewer than 5 records:")
print(rare_categories)

if not rare_categories.empty:
    print("\nRecords belonging to rare categories:")
    print(df[df["category"].isin(rare_categories.index)])

# 11. Check blank instructions
print("\nBLANK INSTRUCTIONS")

blank_instructions = (
    df["instruction"].fillna("").astype(str).str.strip().eq("").sum()
)

print("Number of blank instructions:", blank_instructions)


