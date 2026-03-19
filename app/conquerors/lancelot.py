from app.conquerors.conquerors import calculate_stats


def lancelot_stats(stats: dict) -> dict:
    lancelot = stats["lancelot"]
    return calculate_stats(lancelot)
