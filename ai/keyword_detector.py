SCAM_WORDS = [

"registration fee",
"training fee",
"processing fee",
"pay before joining",
"security deposit",
"advance payment",
"limited slots",
"urgent joining",
"immediate onboarding",
"act now",
"click immediately",
"whatsapp only",
"earn instantly"

]


def detect_keywords(text):

    text=text.lower()

    found=[]

    for word in SCAM_WORDS:

        if word in text:

            found.append(word)

    return found