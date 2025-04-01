import re
 
class FormatCheck:
   
    @staticmethod
    def email(email:str) -> bool:
        """_summary_
        Args:
            email (str): _description_
        Returns:
            bool: _description_
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]+$"
        return bool(re.match(pattern, email))
    
    @staticmethod 
    def minimumLength(input_string: str , min_length:int)->bool:
        """
            _summery__
        Args:
            input_string (str): string to check if length is bigger than expected minimum length
            min_length (int): this value define minimum allowed length of string
        Returns:
            bool
        """
        if len(input_string) < min_length:
            return False
        return True