#!/usr/bin/env python3

# Import the function from the subdirectory
from functions.get_files_info import get_files_info

def main():
    print("Testing get_files_info function...\n")
    
    # Test 1: List current directory (should work)
    print("Test 1: get_files_info('calculator', '.')")
    result1 = get_files_info("calculator", ".")
    print(result1)
    print("\n" + "="*50 + "\n")
    
    # Test 2: List 'pkg' directory (may or may not exist)
    print("Test 2: get_files_info('calculator', 'pkg')")
    result2 = get_files_info("calculator", "pkg")
    print(result2)
    print("\n" + "="*50 + "\n")
    
    # Test 3: Try to list /bin (should return error - outside working directory)
    print("Test 3: get_files_info('calculator', '/bin')")
    result3 = get_files_info("calculator", "/bin")
    print(result3)
    print("\n" + "="*50 + "\n")
    
    # Test 4: Try to list parent directory (should return error - outside working directory)
    print("Test 4: get_files_info('calculator', '../')")
    result4 = get_files_info("calculator", "../")
    print(result4)
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
