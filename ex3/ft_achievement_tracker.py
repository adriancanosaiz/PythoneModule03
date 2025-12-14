from typing import Any


def show_player_achievements(player, achivements) -> None:
    print(f"Player {player} achievements: {achivements}")

def get_all_achievements(players) -> None:
    all_achievements = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    return all_achievements

def get_common_achievements(players) -> None:
    common = None
    for achievements in players.values():
        if common is None:
            common = achievements
        else:
            common = common.intersection(achievements)
    return common

def get_rare_achievements(players, all_achievements) -> Any:
    achievements_count = {}
    for achievement in all_achievements:
        count = 0
        for player_achievements in players.values():
            if achievement in player_achievements:
                count += 1
        achievements_count[achievement] = count

    return {
        achievement
        for achievement, count in achievements_count.items()
        if count == 1
    }

def compare_players(player1, player2) -> Any:
    common = player1.intersection(player2)
    unique_player1 = player1.difference(player2)
    unique_player2 = player2.difference(player1)

    return common, unique_player1, unique_player2

def main() -> None:
    print("=== Achievement Tracker System ===\n")

    players = {
        "alice": {
            "first_kill",
            "level_10",
            "treasure_hunter",
            "speed_demon"
        },
        "bob": {
            "first_kill",
            "level_10",
            "boss_slayer",
            "collector"
        },
        "charlie": {
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist"
        }
    }

    for player, achievements in players.items():
        show_player_achievements(player, achievements)

    print("\n=== Achievement Analytics ===")

    all_achievements = get_all_achievements(players)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_achievements = get_common_achievements(players)
    print(f"\nCommon to all players: {common_achievements}")

    rare_achievements = get_rare_achievements(players, all_achievements)
    print(f"Rare achievements (1 player): {rare_achievements}")

    alice_vs_bob = compare_players(players["alice"], players["bob"])
    print(f"\nAlice vs Bob common: {alice_vs_bob[0]}")
    print(f"Alice unique: {alice_vs_bob[1]}")
    print(f"Bob unique: {alice_vs_bob[2]}")

if __name__ == "__main__":
    main()