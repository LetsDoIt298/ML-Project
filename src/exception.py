import sys
from src.logger import logging

# Function how our message looks in case of error
def error_message_detail(error, error_detail:sys):
    _,_,exe_tb = error_detail.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    error_message='''Error occured occured in python script named 
                  [{0}] line number [{1}] error message [{2}]'''.format(
                      file_name,
                      exe_tb.tb_lineno,
                      str(error)
                                                                              )
    return error_message

# Whenever error arrised call error_message_detail Exception
class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        # error_details is provided by sys
        self.error_message = error_message_detail(error_message,error_detail=error_details)

    def __str__(self):
        return self.error_message

###################################################


# ## Checking if logging is working or not
# if __name__ == "__main__":
#     try:
#         a =1/0
#     except Exception as e:
#         print('Hi',e)
#         logging.info(e,sys,"Divide by Zero")
#         raise CustomException(e,sys)
