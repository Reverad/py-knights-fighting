from app.conquerors.conquerors import calculate_stats


def mordred_stats(stats: dict) -> dict:
    mordred = stats["mordred"]

    return calculate_stats(mordred)
