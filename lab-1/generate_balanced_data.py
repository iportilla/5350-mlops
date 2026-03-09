import pandas as pd
import numpy as np
import os

def generate_balanced_dataset(output_file="smsspamcollection-balanced.csv", n_samples_per_class=1000):
    """
    Generates a synthetic dataset with an equal number of 'ham' and 'spam' examples.
    """
    np.random.seed(42)
    
    # Generate HAM features
    # Ham messages are typically shorter with fewer punctuation marks
    ham_length = np.random.normal(loc=50, scale=20, size=n_samples_per_class)
    ham_punct = np.random.normal(loc=3, scale=2, size=n_samples_per_class)
    
    # Ensure no negative values and convert to integers
    ham_length = np.maximum(1, np.round(ham_length)).astype(int)
    ham_punct = np.maximum(0, np.round(ham_punct)).astype(int)
    
    # Generate SPAM features
    # Spam messages are typically longer and have more punctuation
    spam_length = np.random.normal(loc=150, scale=30, size=n_samples_per_class)
    spam_punct = np.random.normal(loc=12, scale=5, size=n_samples_per_class)
    
    # Ensure no negative values and convert to integers
    spam_length = np.maximum(10, np.round(spam_length)).astype(int) # At least length 10
    spam_punct = np.maximum(0, np.round(spam_punct)).astype(int)
    
    # Create DataFrames
    ham_df = pd.DataFrame({
        'length': ham_length,
        'punct': ham_punct,
        'label': 'ham'
    })
    
    spam_df = pd.DataFrame({
        'length': spam_length,
        'punct': spam_punct,
        'label': 'spam'
    })
    
    # Combine and shuffle
    balanced_df = pd.concat([ham_df, spam_df], ignore_index=True)
    balanced_df = balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Save to CSV
    balanced_df.to_csv(output_file, index=False)
    print(f"✅ Generated {len(balanced_df)} samples ({n_samples_per_class} ham, {n_samples_per_class} spam).")
    print(f"✅ Saved balanced dataset to {output_file}")

if __name__ == "__main__":
    generate_balanced_dataset()
