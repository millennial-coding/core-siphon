"""
Core-Siphon: Among the Dead Stars
Universe Module. Contains star system data and navigation logic.

Author: Kyle Hebenheimer
Version: 0.1.0
"""

star_systems = {
    "the_corridor": {
        "name": "The Corridor",
        "description":  (
            "A liminal waypoint carved from 700-year-old infrastructure. "
            "Cold, clinical passage to more interesting or lucrative systems. "
            "The IF processes 10,000+ license applicants here a month. Only spot to both merc and military IDs. "
            "Nobody stays by choice."

        ),
        "danger_level": 1,
        "connected_systems": ["the_sump", "voss_expanse"],
        "available_actions": ["refuel", "check_bounties", "warp"]
    }
}
def get_system(system_key):
    """Return a star system dictionary by its key, or none if not found."""
    return star_systems.get(system_key, None)

def describe_system(system_key):
    """Print a formatted description of the star system."""
    system = get_system(system_key)

    if system is None:
        print("Unknown system. IF charts have no record of this location.")
        return

    print(f"\n[ {system['name']} ]")
    print(f"Danger Level: {system['danger_level']}/10")
    print(f"\n{system['description']}")
    print(f"\nAvailable actions: {', '.join(system['available_actions'])}")
