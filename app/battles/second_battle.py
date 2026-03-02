def second_battle(arthur: dict, red_knight: dict) -> dict:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0

    return {
        arthur["name"]: arthur["hp"],
        red_knight["name"]: red_knight["hp"]
    }
