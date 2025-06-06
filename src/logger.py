import logging
import os
from datetime import datetime

# Create logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Create unique log file name with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='a',  # Append mode
    format='[%(asctime)s] [Line %(lineno)d] [%(name)s] - %(levelname)s - %(message)s',
    level=logging.INFO
)

# # Test logging
# if __name__ == "__main__":
#     logging.info("Logging has started successfully.")
