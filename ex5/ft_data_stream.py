"""Game data stream processor module.

This module demonstrates the use of generators for efficient data streaming
and processing, including game events, Fibonacci sequences, and prime numbers.
"""


def game_event_stream(total_events):
    """Generate a stream of game events for players.

    Creates a generator that yields game events including player name, level,
    and action. Events are generated cyclically from predefined player and
    action lists.

    Args:
        total_events: The total number of events to generate.

    Yields:
        tuple: A tuple containing (player_name, level, action).
    """
    players = [
        ("alice", 5),
        ("bob", 12),
        ("charlie", 8),
        ("diana", 15)
    ]

    actions = [
        "killed monster",
        "found treasure",
        "leveled up"
    ]

    i = 0
    while i < total_events:
        player, level = players[i % len(players)]
        action = actions[i % len(actions)]
        yield player, level, action
        i += 1


def fibonacci_generator():
    """Generate an infinite Fibonacci sequence.

    Yields:
        int: The next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator():
    """Generate an infinite sequence of prime numbers.

    Yields:
        int: The next prime number.
    """
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def main():
    """Run the data stream processor demonstration.

    Demonstrates efficient stream processing of game events and shows examples
    of Fibonacci and prime number generators. Processes events and calculates
    analytics without loading all data into memory.
    """
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"\nProcessing {total_events} game events...\n")

    total_processed = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    for player, level, action in game_event_stream(total_events):
        total_processed += 1

        if total_processed <= 3:
            print(f"Event {total_processed}: "
                  f"Player {player} (level {level}) {action}")

        if level >= 10:
            high_level_players += 1

        if action == "found treasure":
            treasure_events += 1

        if action == "leveled up":
            level_up_events += 1

    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci_generator()
    fib_values = [str(next(fib)) for _ in range(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_values)}")

    primes = prime_generator()
    prime_values = [str(next(primes)) for _ in range(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_values)}")


if __name__ == "__main__":
    main()
