import json


def getWeightByAgeAndGender(ageInYear: int, gender: str) -> float:
    """
    Returns the weight in kilograms based on the age and gender of the person.

    Parameters:
    ageInYear (int): The age of the person in years.
    gender (str): The gender of the person. Can be either "male" or "female".

    Returns:
    float: The weight of the person in kilograms.
    """
    with open("data/weight.json", "r") as f:
        weightData = json.load(f)
    weightInKg = weightData[gender][str(ageInYear)]
    return weightInKg


def getHeigthByAgeAndGender(ageInYear: int, gender: str) -> int:
    """
    Returns the height in centimeters based on the age and gender provided.

    Parameters:
    ageInYear (int): The age in years of the person.
    gender (str): The gender of the person. Can be either "male" or "female".

    Returns:
    int: The height in centimeters of the person.
    """
    with open("data/heigth.json", "r") as f:
        heightData = json.load(f)

    heigthInCm = heightData[gender][str(ageInYear)]
    return heigthInCm


def energyByStJeorEquation(
    ageInYear: int, gender: str, activityFactor: float, heigthInCm: int, weightInKg: int
) -> float:
    """
    Calculates the energy expenditure of a person using the St. Jeor equation.

    Args:
        ageInYear (int): Age of the person in years.
        gender (str): Gender of the person. Either "male" or "female".
        activityFactor (float): Activity factor of the person.
        heigthInCm (int): Height of the person in centimeters.
        weightInKg (int): Weight of the person in kilograms.

    Returns:
        float: Energy expenditure of the person in kilojoules.
    """

    energyKj = 0
    energyKj += 10 * weightInKg
    energyKj += 6.25 * heigthInCm
    energyKj += -5 * ageInYear

    if gender == "male":
        energyKj += 5

    if gender == "female":
        energyKj += -161

    energyKj *= activityFactor
    energyKj *= 4.2  # convert kcal to kJ

    return energyKj


def main():
    """
    Calculates the daily energy need of a person based on their gender, age, height, weight, and activity factor.

    Parameters:
    gender (str): The gender of the person. Can be "male", "female", or "divers".
    ageInYear (int): The age of the person in years.
    activityFactor (float): The activity factor of the person. Can be 1.6 for normal activity, 1.4 for less activity, or 1.8 for more activity.

    Returns:
    energyKj (float): The daily energy need of the person in kilojoules.
    """

    # inputdata
    gender = "male"  # or female or divers
    ageInYear = 15
    activityFactor = (
        1.8  # 1.6 for normal activity, 1.4 for less activity, 1.8 for more activity
    )

    heigthInCm = getHeigthByAgeAndGender(ageInYear=ageInYear, gender=gender)
    weightInKg = getWeightByAgeAndGender(ageInYear=ageInYear, gender=gender)

    print(f"Your height is {heigthInCm} cm")
    print(f"Your weight is {weightInKg} kg")
    print(f"Your activity factor is {activityFactor}")
    print(f"Your age is {ageInYear} years")

    energyKj = energyByStJeorEquation(
        ageInYear=ageInYear,
        gender=gender,
        activityFactor=activityFactor,
        heigthInCm=heigthInCm,
        weightInKg=weightInKg,
    )
    print(f"Your daily energy need is {energyKj} kJ")

    return energyKj


if __name__ == "__main__":
    main()
