# main.py
# Entry point for Core-Siphon: Among the Dead Stars

"""
Core-Siphon: Among the Dead Stars
Main entry point. Handles game initialization and the primary game loop.

Author: Kyle Hebenheimer
Version: 0.1.0
"""

def main():
    """Initialize and greet player."""
    print("=" * 40)
    print("   Core-Siphon: Among the Dead Stars")
    print("=" * 40)
    print()

    pilot_name = input("Enter your pilot name or SiphonID to continue: ")
    ship_name = input("Enter your ship name or IFIB number to continue: ")

    print()
    print(f"Welcome, {pilot_name}. Your ship, {ship_name}, awaits you. It will need you to run a diagnostics check.")
    print("You are facing the endless cold night and the void is indifferent. Get to work, soldier.")

main()
