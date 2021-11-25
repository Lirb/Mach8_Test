import sys
from user import User

def main():
    if len(sys.argv) != 2:
       print('Please provide a valid height in inches (postive Integer)')
    else: 
        try:
            total_height = float(sys.argv[1])
            if total_height < 0:
                raise ValueError('Please provide a valid height in inches (postive Integer)')
            user = User(total_height)
            user.query()
            result_str = user.list_query_results()
            print(result_str)
        except ValueError as error:
            print(error)      
        
if __name__ == "__main__":
    main()
    