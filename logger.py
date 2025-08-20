import logging

def get_logger(name:str):
    """
        Returns a logger instance with both console and file handler
    """
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    
    if not logger.handlers:
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        file_handler = logging.FileHandler("data_preprocessing.log")
        file_handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        
    return logger