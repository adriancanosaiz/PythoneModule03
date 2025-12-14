"""Command Quest module for processing command-line arguments.

This module demonstrates how to access and manipulate command-line arguments
using sys.argv in Python.
"""
import sys


def main():
    """Process and display command-line arguments received.

    Displays the program name,
    number of arguments received,
    and each argument individually.
    If no arguments are provided, displays a message indicating so.
    """
    print("=== Command Quest ===")

    args = sys.argv
    total_args = len(args)
    program_name = args[0]

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")
        return

    print(f"Program name: {program_name}")
    print(f"Arguments received: {total_args - 1}")

    i = 1
    while i < total_args:
        print(f"Argument {i}: {args[i]}")
        i += 1

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
