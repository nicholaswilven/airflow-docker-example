input_path = "data/generated_menu_data.csv"
output_path = "data/generated_menu_data_processed.csv"

import argparse
import os
from datetime import datetime
import logging
from source.api import test_apis
from source.process import process_csv

os.makedirs('logs', exist_ok = True)
logging.basicConfig(
    level = logging.INFO,
    format = '[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%d %B %Y %H:%M:%S',
    handlers = [
        logging.StreamHandler(),
        logging.FileHandler(
            filename ='./logs/DummyLogs.log',
            mode = 'a' 
        )
    ],
)
logger = logging.getLogger("Main")

def main(process_csv = False, test_apis = False):
    try:
        logger.info('*'*45 + ' START ' + '*'*45)
        start_main = datetime.now()
        exit_statuss = 0
        if process_csv:
            process_csv(input_path, output_path)
        if test_apis:
            if not os.path.exists(output_path):
                raise FileNotFoundError("Processed file not found. Run 'process_csv' mode first.")
            test_apis(output_path)
    except Exception as e:
        exit_status = 1
        logger.exception(e)
    finally:
        end_main = datetime.now()
        logger.info(f'Exited after {end_main - start_main} with status {exit_status}')
        logger.info('*'*45 + ' FINISH ' + '*'*45)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dummy Airflow pipeline")
    parser.add_argument(
        "--process_csv", 
        action="store_true", 
        help="Process the input CSV and save the result locally."
    )
    parser.add_argument(
        "--test_apis", 
        action="store_true", 
        help="Send the processed CSV via API."
    )
    args = parser.parse_args()
    
    args = parser.parse_args()

    # Convert args to a dictionary
    args_dict = vars(args)
    main(**args_dict)
