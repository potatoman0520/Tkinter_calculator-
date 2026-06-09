# Tkinter Calculator

## Description

A simple GUI calculator built with Python's `tkinter` library. It supports basic arithmetic operations — addition, subtraction, multiplication, and division — through a clickable button interface.

## Features

- Digit buttons (0–9) to build numbers
- Operators: `+`, `-`, `*`, `/`
- `=` button to evaluate the expression
- `CLEAR` button to reset the entry field

## Requirements

- Python 3.x
- `tkinter` (included in the Python standard library)

## How to Run

```bash
python Assignment_6.py
```

## Usage

1. Click digit buttons to enter the first number.
2. Click an operator button (`+`, `-`, `*`, `/`) — this stores the first number and clears the display.
3. Enter the second number using the digit buttons.
4. Click `=` to display the result.
5. Click `CLEAR` to reset and start a new calculation.

## File Structure

```
Assignment_6.zip
└── Assignment_6.py   # Main application file
```

## Notes

- The calculator handles **integer inputs only**; decimal input is not supported.
- Division by zero is not handled and will raise a `ZeroDivisionError`.
- The window size is fixed at **300 × 400 pixels**.

