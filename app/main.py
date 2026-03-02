from app.conquerors.conquerors import conquerors
from app.conquerors.lancelot import lancelot_stats
from app.conquerors.mordred import mordred_stats
from app.conquerors.arthur import arthur_stats
from app.conquerors.red_knight import red_knight_stats
from app.battles.first_battle import first_battle
from app.battles.second_battle import second_battle


def battle(stats: dict) -> dict:
    lancelot = lancelot_stats(stats)
    mordred = mordred_stats(stats)
    arthur = arthur_stats(stats)
    red_knight = red_knight_stats(stats)

    result = first_battle(lancelot, mordred)
    result.update(second_battle(arthur, red_knight))

    return result


print(battle(conquerors))
