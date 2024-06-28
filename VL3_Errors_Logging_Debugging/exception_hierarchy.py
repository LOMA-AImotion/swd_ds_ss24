import sys
import os
# first file does not exist
file1 = os.path.join(os.path.dirname(__file__), 'myfile.txt')
# second file has a string "SWD"
file2 = os.path.join(os.path.dirname(__file__), 'swd.txt')
# third file contains 42, should be fine
file3 = os.path.join(os.path.dirname(__file__), 'valid.txt')

for file in [file1, file2, file3]:
    try: 
        f = open(file)
        first_line = f.readline()
        i = int(first_line.strip())
        print("The number I found:", i)
    except OSError as err:
        print("OS error:", err)
    except ValueError as ve:
        print(f"Could not convert data '{first_line.strip()}' to an integer.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise