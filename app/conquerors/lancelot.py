def lancelot_stats(stats: dict) -> dict:
    lancelot = stats["lancelot"]

    lancelot["protection"] = 0
    for armour in lancelot["armour"]:
        lancelot["protection"] += armour["protection"]

    lancelot["power"] += lancelot["weapon"]["power"]

    if lancelot["potion"] is not None:
        if "power" in lancelot["potion"]["effect"]:
            lancelot["power"] += lancelot["potion"]["effect"]["power"]

        if "protection" in lancelot["potion"]["effect"]:
            lancelot["protection"] += (
                lancelot)["potion"]["effect"]["protection"]

        if "hp" in lancelot["potion"]["effect"]:
            lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

    return lancelot
