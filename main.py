import json

def getWeightByAgeAndGender(ageInYear: int, gender: str):
    with open("data/weight.json", "r") as f:
        weightData = json.load(f)
    weightInKg = weightData[gender][str(ageInYear)]
    return weightInKg


def getHeigthByAgeAndGender(ageInYear: int, gender: str):
    with open("data/heigth.json", "r") as f:
        heightData = json.load(f)

    heigthInCm = heightData[gender][str(ageInYear)]
    return heigthInCm


def energyByStJeorEquation(
    ageInYear: int, gender: str, activityFactor: float, heigthInCm: int, weightInKg: int
):
    energyKj = 0
    energyKj += 10 * weightInKg
    energyKj += 6.25 * heigthInCm
    energyKj += -5 * ageInYear

    if gender == "male":
        energyKj += 5

    if gender == "female":
        energyKj += -161

    energyKj *= activityFactor
    energyKj *= 4.2

    return energyKj


def main():
    # input
    gender = "male" # or female or divers
    ageInYear = 30
    activityFactor = 1.2

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
