"""Player score analytics module.

This module provides functionality to analyze player score statistics,
including total, average, maximum, minimum, and score range.
"""
import sys


def main():
    """Analyze player scores from command-line arguments.

    Reads scores from command-line arguments,
    validates they are numeric values,
    and calculates statistics such as total,
    average, maximum, minimum, and range
    of the scores.

    Note:
        Scores must be provided as command-line arguments.
        Example: python3 ft_score_analytics.py 1500 2300 1800
    """

    print("=== Player Score Analytics ===")
    args = sys.argv[1:]
    total_args = len(args)

    if total_args == 0:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []
    for value in args:
        try:
            scores.append(int(value))
        except ValueError:
            print(f"Invalid score detected: {value}")
            print("Please enter only numeric values.")
            print("Example: python3 ft_score_analytics.py "
                  "1500 2300 1800 2100 1950")
            return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    highest_score = max(scores)
    lowest_score = min(scores)
    score_range = highest_score - lowest_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
