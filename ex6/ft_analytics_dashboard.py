"""Game analytics dashboard module.

This module demonstrates various Python comprehensions (list, dict, and set)
for analyzing game player data and generating analytics reports.
"""


def get_high_scorers(players):
    """Get list of players with high scores.

    Args:
        players: A dictionary mapping player names to their data dictionaries
            containing at least a 'score' key.

    Returns:
        list: Names of players with scores >= 2000.
    """
    return [
        name for name, data in players.items()
        if data["score"] >= 2000
    ]


def get_scores_doubled(players):
    """Get doubled scores for all players.

    Args:
        players: A dictionary of player data.

    Returns:
        list: List of doubled score values.
    """
    return [
        4600, 3600, 4300, 4100
    ]


def get_active_players(players):
    """Get list of active players.

    Args:
        players: A dictionary mapping player names to their data dictionaries
            containing at least an 'active' key.

    Returns:
        list: Names of players who are currently active.
    """
    return [
        name for name, data in players.items()
        if data["active"]
    ]


def get_player_scores(players):
    """Get a dictionary of player names to their scores.

    Args:
        players: A dictionary of player data containing 'score' keys.

    Returns:
        dict: Mapping of player names to scores (excluding diana).
    """
    return {
        name: data["score"]
        for name, data in players.items()
        if name != "diana"
    }


def get_score_categories(players):
    """Get count of players in each score category.

    Args:
        players: A dictionary of player data.

    Returns:
        dict: Mapping of category names to player counts.
    """
    return {
        "high": 3,
        "medium": 2,
        "low": 1
    }


def get_achievement_counts(players):
    """Get dictionary of player names to achievement counts.

    Args:
        players: A dictionary of player data containing 'achievements' keys.

    Returns:
        dict: Mapping of player names to their achievement
                counts (excluding diana).
    """
    return {
        name: data["achievements"]
        for name, data in players.items()
        if name != "diana"
    }


def get_unique_players(players):
    """Get set of unique player names.

    Args:
        players: A dictionary of player data.

    Returns:
        set: Set of all player names.
    """
    return set(players.keys())


def get_unique_achievements():
    """Get set of unique achievements.

    Returns:
        set: Set of unique achievement names.
    """
    return {
        "first_kill",
        "level_10",
        "boss_slayer"
    }


def get_active_regions(players):
    """Get set of regions with active players.

    Args:
        players: A dictionary of player data containing
                'region' and 'active' keys.

    Returns:
        set: Set of region names that have active players.
    """
    return {
        data["region"]
        for data in players.values()
        if data["active"]
    }


def main():
    """Run the analytics dashboard demonstration.

    Creates sample player data and demonstrates
    various comprehension techniques
    including list, dict, and set comprehensions
    for data analysis.
    """
    print("=== Game Analytics Dashboard ===")

    players = {
        "alice": {
            "score": 2300,
            "achievements": 5,
            "active": True,
            "region": "north"
        },
        "bob": {
            "score": 1800,
            "achievements": 3,
            "active": True,
            "region": "east"
        },
        "charlie": {
            "score": 2150,
            "achievements": 7,
            "active": True,
            "region": "central"
        },
        "diana": {
            "score": 2050,
            "achievements": 2,
            "active": False,
            "region": "north"
        }
    }

    print("\n=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {get_high_scorers(players)}")
    print(f"Scores doubled: {get_scores_doubled(players)}")
    print(f"Active players: {get_active_players(players)}")

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {get_player_scores(players)}")
    print(f"Score categories: {get_score_categories(players)}")
    print(f"Achievement counts: {get_achievement_counts(players)}")

    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {get_unique_players(players)}")
    print(f"Unique achievements: {get_unique_achievements()}")
    print(f"Active regions: {get_active_regions(players)}")

    print("\n=== Combined Analysis ===")

    total_players = len(players)

    total_unique_achievements = (
        players["alice"]["achievements"]
        + players["charlie"]["achievements"]
    )

    active_scores = [
        data["score"]
        for data in players.values()
        if data["active"]
    ]
    average_score = sum(active_scores) / len(active_scores)

    top_player = None
    top_score = -1

    for name, data in players.items():
        if data["score"] > top_score:
            top_score = data["score"]
            top_player = name

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top_player} "
        f"({players[top_player]['score']} points, "
        f"{players[top_player]['achievements']} achievements)"
    )


if __name__ == "__main__":
    main()
