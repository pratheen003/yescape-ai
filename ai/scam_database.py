import json


def check_scam_database(text):

    text = text.lower()

    matches = []

    score_penalty = 0

    with open(
        "data/scam_patterns.json",
        "r",
        encoding="utf-8"
    ) as f:

        scam_db = json.load(f)

    for category, patterns in scam_db.items():

        for pattern in patterns:

            if pattern.lower() in text:

                matches.append(category)

                score_penalty += 8

                break

    return {

        "matches": matches,

        "score_penalty": score_penalty

    }