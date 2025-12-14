import sys

def main():
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