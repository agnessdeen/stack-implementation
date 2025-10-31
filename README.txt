Project Title: Expression Evaluator using Stack

Language: Python 3.10+

Author: agness deen kabia

Description:
This program reads infix mathematical expressions from an input file, converts each expression to postfix notation using a stack-based algorithm, evaluates the result, and writes the output to a file. It demonstrates the use of data structures (stacks), operator precedence, and file handling in Python.

Folder Structure:
├── main.py         # Python source code
├── input.txt       # Contains infix expressions (one per line)
├── output.txt      # Contains evaluated results (formatted to 2 decimal places)
└── README.txt      # Project documentation

Features:
- Converts infix expressions to postfix notation
- Evaluates postfix expressions using stack logic
- Handles +, -, *, / operators and parentheses
- Reads from input.txt and writes to output.txt
- Formats results to 2 decimal places

How to Run:
1. Ensure Python is installed (version 3.10 or higher)
2. Place `main.py`, `input.txt`, and `README.txt` in the same folder
3. Open the folder in PyCharm or any Python IDE
4. Run `main.py`
5. Check `output.txt` for results

Sample input.txt:
3 + 4 * (2 - 1)
(5 + 6) * 2
10 / (3 + 2)
8 - 3 + 2

Expected output.txt:
7.00
22.00
2.00
7.00

References:
- Python Documentation: https://docs.python.org/3/
- GeeksforGeeks: Infix to Postfix Conversion
- Stack Overflow: Stack-based expression evaluation

