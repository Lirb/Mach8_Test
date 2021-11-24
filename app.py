import sys
from user import User

def main():
    if len(sys.argv) != 2:
       raise ValueError('Please provide a height in inches')
    else: 
        total_height = float(sys.argv[1])
        user = User(total_height)
        user.query()
        result_str = user.list_query_results()
        print(result_str)
        
if __name__ == "__main__":
    main()
    