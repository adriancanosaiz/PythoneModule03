"""Player inventory system module.

This module provides a complete inventory management system for game players,
including inventory display,
item transfers between players,
and value calculations.
"""


def print_inventory(player, inventory):
    """Print detailed inventory information for a player.

    Displays each item with its category, rarity, quantity, and value.
    Also shows total inventory value, item count, and category breakdown.

    Args:
        player: The name of the player.
        inventory: A dictionary where keys are item names and values
        are dictionaries containing
        'category', 'rarity', 'quantity', and 'value' keys.
    """
    print(f"\n=== {player}'s Inventory ===")
    total_value = 0
    total_items = 0
    categories = {}

    for item, data in inventory.items():
        item_total = data["quantity"] * data["value"]
        total_value += item_total
        total_items += data["quantity"]

        category = data["category"]
        categories[category] = categories.get(category, 0) + data["quantity"]

        print(
            f"{item} ({data['category']}, {data['rarity']}): "
            f"{data['quantity']}x @ {data['value']} gold each = "
            f"{item_total} gold"
        )

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    category_str = ", ".join(
        f"{cat}({qty})" for cat, qty in categories.items()
    )
    print(f"Categories: {category_str}")


def transfer_item(giver, receiver, item, quantity):
    """Transfer items from one player's inventory to another.

    Transfers a specified quantity of an item from the giver's inventory to the
    receiver's inventory.
    If the receiver doesn't have the item, it will be added.

    Args:
        giver: The inventory dictionary of the player giving the item.
        receiver: The inventory dictionary of the player receiving the item.
        item: The name of the item to transfer.
        quantity: The number of items to transfer.

    Returns:
        bool: True if the transfer was successful, False otherwise.
    """
    if item not in giver or giver[item]["quantity"] < quantity:
        print("Transaction failed!")
        return False

    giver[item]["quantity"] -= quantity

    if item not in receiver:
        receiver[item] = giver[item].copy()
        receiver[item]["quantity"] = 0

    receiver[item]["quantity"] += quantity
    print("Transaction successful!")
    return True


def inventory_value(inventory):
    """Calculate the total value of an inventory.

    Args:
        inventory: A dictionary where keys are item names and values
                    are dictionaries containing 'quantity' and 'value' keys.

    Returns:
        int: The total value of all items in the inventory.
    """
    return sum(
        data["quantity"] * data["value"]
        for data in inventory.values()
    )


def main():
    """Run the inventory system demonstration.

    Creates sample inventories for two players, demonstrates item transfers,
    and displays analytics about inventory values and item counts.
    """
    print("=== Player Inventory System ===")

    alice_inventory = {
        "sword": {
            "category": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500
        },
        "potion": {
            "category": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 50
        },
        "shield": {
            "category": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 200
        }
    }

    bob_inventory = {
        "magic_ring": {
            "category": "accessory",
            "rarity": "rare",
            "quantity": 1,
            "value": 300
        }
    }

    print_inventory("Alice", alice_inventory)

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    transfer_item(alice_inventory, bob_inventory, "potion", 2)

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice_inventory['potion']['quantity']}")
    print(f"Bob potions: {bob_inventory['potion']['quantity']}")

    print("\n=== Inventory Analytics ===")

    alice_value = inventory_value(alice_inventory)
    bob_value = inventory_value(bob_inventory)

    most_valuable = "Alice" if alice_value > bob_value else "Bob"
    print(f"Most valuable player: "
          f"{most_valuable} ({max(alice_value, bob_value)} gold)")

    alice_items = sum(data["quantity"] for data in alice_inventory.values())
    bob_items = sum(data["quantity"] for data in bob_inventory.values())

    most_items_player = "Alice" if alice_items > bob_items else "Bob"
    most_items_count = max(alice_items, bob_items)
    print(f"Most items: {most_items_player} ({most_items_count} items)")

    rarest = []

    for item, data in alice_inventory.items():
        if data["rarity"] == "rare":
            rarest.append(item)

    for item, data in bob_inventory.items():
        if data["rarity"] == "rare":
            rarest.append(item)

    print(f"Rarest items: {', '.join(rarest)}")


if __name__ == "__main__":
    main()
