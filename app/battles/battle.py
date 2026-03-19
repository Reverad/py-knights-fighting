def battle(conq1: dict, conq2: dict) -> dict:
    conq1["hp"] -= conq2["power"] - conq1["protection"]
    conq2["hp"] -= conq1["power"] - conq2["protection"]

    if conq1["hp"] <= 0:
        conq1["hp"] = 0

    if conq2["hp"] <= 0:
        conq2["hp"] = 0

    return {
        conq1["name"]: conq1["hp"],
        conq2["name"]: conq2["hp"]
    }
