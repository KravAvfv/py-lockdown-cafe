from app.cafe import Cafe
from app.errors import NotVaccinatedError, NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: str) -> str:
    cafe_obj = Cafe(cafe)
    masks_to_buy = 0
    try:
        for friend in friends:
            cafe_obj.visit_cafe(friend)
    except VaccineError:
        return f"All friends should be vaccinated"
    except NotWearingMaskError:
        masks_to_buy += 1
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe_obj.name}"
