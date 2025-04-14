README
This project is my attempt to solve a Python test task. 
It is based on a Caesar cipher with a custom shifting pattern. 
I explored different ideas, tested variations, and included helpful comments
in the code.

📂 File Descriptions
python_test.py
This is the original test file I received. I tried to:

Understand the logic behind the encryption (custom Caesar cipher).

Follow hidden hints in the comments.

Create a process_data() function that transforms the input using shift values.

Add a decode_message() function to try to decode messages.

Test everything using a sample string.

There are also many useful comments and test cases that show my thinking process.

BF_Check.py
This file does a brute-force check. It:

Tries many different shift patterns.

Uses the pyenchant library to check if the output contains real English words.

Prints the results when it finds possible correct messages.

This helped me test and explore different solutions.

There are 3 different versions, because I was trying to run all 3 of them during night/day

final_jersov.py
This is a cleaned-up version of my solution. It:

Combines encoding and decoding into one function.

Handles user input or uses a default test sentence.

Validates if the decoded message matches the original.

Handles errors and keeps the code readable.

