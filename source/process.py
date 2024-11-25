import pandas as pd
import os
import logging
logger = logging.getLogger("Main")

def process_csv(input_path, output_path):
    """
    Reads a CSV, performs a dummy operation, and saves the result.
    """
    # Read the CSV
    df = pd.read_csv(input_path)
    # Dummy operation: Add a new column
    df['processed'] = 'Processed'
    # Save the processed CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    logger.info(f"Processed file saved at: {output_path}")