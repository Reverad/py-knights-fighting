from app.conquerors.conquerors import calculate_stats


def arthur_stats(stats: dict) -> dict:
    arthur = stats["arthur"]

    return calculate_stats(arthur)
