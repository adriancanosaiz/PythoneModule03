"""Game coordinate system module.

This module provides utilities for working with 3D coordinates in a game,
including distance calculation and coordinate parsing.
"""
import math


def distance_3d(point1, point2):
    """Calculate the Euclidean distance between two 3D points.

    Args:
        point1: A tuple of three numeric values
                (x, y, z) representing the first point.
        point2: A tuple of three numeric values
                (x, y, z) representing the second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2 +
        (point2[2] - point1[2]) ** 2
    )


def parse_coordinates(coord_str):
    """Parse a comma-separated string into a tuple of integer coordinates.

    Args:
        coord_str: A string containing three comma-separated integer values.
            Example: "3,4,0"

    Returns:
        tuple: A tuple of three integers (x, y, z).

    Raises:
        ValueError: If the string cannot be parsed into integers.
    """
    parts = coord_str.split(",")
    return tuple(int(value) for value in parts)


def main():
    """Demonstrate coordinate system functionality.

    Shows examples of distance calculation,
    coordinate parsing, and error handling
    for invalid coordinate strings.
    """
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)
    position = (10, 20, 5)

    print(f"\nPosition created: {position}")
    print(f"Distance between {origin} and {position}: "
          f"{distance_3d(origin, position):.2f}")

    coord_str = "3,4,0"
    print(f'\nParsing coordinates: "{coord_str}"')

    try:
        parsed_position = parse_coordinates(coord_str)
        print(f"Parsed position: {parsed_position}")
        print(f"Distance between {origin} and {parsed_position}: "
              f"{distance_3d(origin, parsed_position):.2f}")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")

    invalid_coord = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid_coord}"')

    try:
        parse_coordinates(invalid_coord)
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: "
              f"{type(error).__name__}, Args: {error.args}")

    print("\nUnpacking demonstration:")
    x, y, z = (3, 4, 0)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
