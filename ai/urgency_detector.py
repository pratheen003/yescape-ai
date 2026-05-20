URGENCY_WORDS={

"urgent":10,
"act now":10,
"only today":15,
"limited slots":15,
"hurry":10,
"immediate joining":15,
"last chance":15,
"join immediately":10,
"offer expires":15

}


def analyze_urgency(text):

    text=text.lower()

    score=0

    positives=[]

    negatives=[]


    for word,penalty in URGENCY_WORDS.items():

        if word in text:

            score-=penalty

            negatives.append(
            f"Pressure wording detected: {word}"
            )


    if len(negatives)==0:

        positives.append(
        "No pressure language detected"
        )


    return{

    "score":score,

    "positives":positives,

    "negatives":negatives

    }