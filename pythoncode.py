# special_greeting.py
from datetime import datetime

def print_ascii_name():
    print(r"""
     _               _      _     _       _     _           _     
    | |             | |    | |   (_)     | |   (_)         | |    
    | |     __ _  __| | ___| |    _ _ __ | |__  _ _ __   __| |___ 
    | |    / _` |/ _` |/ _ \ |   | | '_ \| '_ \| | '_ \ / _` / __|
    | |___| (_| | (_| |  __/ |___| | | | | | | | | | | | (_| \__ \
    |______\__,_|\__,_|\___|_____|_|_| |_|_| |_|_|_| |_|\__,_|___/
    """)

def main():
    print_ascii_name()
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nHello, Lakshmikanth! The current date and time is: {formatted_time}")

if __name__ == "__main__":
    main()
