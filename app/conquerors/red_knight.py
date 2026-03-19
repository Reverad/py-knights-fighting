from app.conquerors.conquerors import calculate_stats


def red_knight_stats(stats: dict) -> dict:
    red_knight = stats["red_knight"]

    return calculate_stats(red_knight)
