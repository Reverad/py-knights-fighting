def first_battle(lancelot: dict, mordred: dict) -> dict:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    return {
        lancelot["name"]: lancelot["hp"],
        mordred["name"]: mordred["hp"]
    }
