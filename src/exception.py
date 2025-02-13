from src.logger import logging
import sys

def error_message_detail(error,error_details:sys):
    '''
    This function returns the line no. and file_name where the error occurred.
    '''
    # Extracting error details from the sys module
    _,_,exec_tb=error_details.exc_info()

    # Extracting file_name and line_no from the traceback object
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_no = exec_tb.tb_lineno

    #Formating the error message
    error_message=f"Error [{str(error)}] occurred on line number [{line_no}] in file [{file_name}]"

    logging.info(error_message)

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message