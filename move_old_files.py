import os 
import shutil 
import time 
import logging 
from datetime import datetime 
from dotenv import load_dotenv

def setup_logging(log_dir): 
    # Create the log directory if it doesn't exist
    if not os.path.exists(log_dir): 
        os.makedirs(log_dir) 
     
    # Create a log file name with the current date and time 
    log_file = os.path.join(log_dir, f"move_old_files_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log") 
     
    # Configure logging 
    logging.basicConfig( 
        filename=log_file, 
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s' 
    ) 
    logging.info("Logger configurado") 
    return log_file 

def delete_old_log_files(log_dir, max_log_days):
    # Delete log files older than max_log_days in the log_dir directory.
    current_time = time.time()
    for file_name in os.listdir(log_dir):
        file_path = os.path.join(log_dir, file_name)
        # Check if it is a file
        if os.path.isfile(file_path):
            # Get the last modification date of the file
            file_mod_time = os.path.getmtime(file_path)
            file_days_to_move = (current_time - file_mod_time) / (60 * 60 * 24)
            # Check if the file is older than max_log_days
            if file_days_to_move > max_log_days:
                os.remove(file_path)
                logging.info(f'Arquivo de log apagado: {file_path}')


def find_and_move_old_files(src_dir, dest_dir, days_to_move): 
    current_time = time.time() 

    for root, _, files in os.walk(src_dir): 
        for file_name in files: 
            file_path = os.path.join(root, file_name) 
             
            # Get the last modification date of the file 
            file_mod_time = os.path.getmtime(file_path) 
            file_days_to_move = (current_time - file_mod_time) / (60 * 60 * 24) 
             
            # Check if the file is older than "days_to_move" 
            if file_days_to_move > days_to_move: 
                relative_path = os.path.relpath(root, src_dir) 
                dest_path = os.path.join(dest_dir, relative_path) 
                 
                # Create the destination directory if it doesn't exist 
                if not os.path.exists(dest_path): 
                    os.makedirs(dest_path) 
                 
                # Move the file to the new directory  
                shutil.move(file_path, os.path.join(dest_path, file_name)) 
                logging.info(f'Movido: {file_path} para {os.path.join(dest_path, file_name)}') 

def main(): 
    load_dotenv()  # Load the variables from the .env file
    src_dir = os.getenv('SRC_DIR')
    dest_dir = os.getenv('DEST_DIR')
    log_dir = os.getenv('LOG_DIR')
    days_to_move = int(os.getenv('DAYS_TO_MOVE'))
    max_log_days = int(os.getenv('MAX_LOG_DAYS')) 
 
    # Delete old log files
    delete_old_log_files(log_dir, max_log_days)

    # Configure logging 
    log_file = setup_logging(log_dir) 
    # print(f"Log sendo salvo em: {log_file}") 

    # Execute the function to find and move old files 
    find_and_move_old_files(src_dir, dest_dir, days_to_move) 

if __name__ == "__main__": 
    main()