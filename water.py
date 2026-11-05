def get_state(temp: float | int) -> str:
    if type(temp) not in (int, float):
        return "invalid temperature"

    if not (-273.15 <= temp < float("inf")):
        return "invalid temperature"

    if temp < 0:
        return "solid"
    if temp < 100:
        return "liquid"
    return "gaseous"
