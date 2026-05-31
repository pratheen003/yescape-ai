def get_verdict(
    score,
    positives=[],
    negatives=[]
):

    positive_count=len(positives)
    negative_count=len(negatives)

    if score>=80:

        return{

        "status":"SAFE",

        "trust":"HIGH TRUST",

        "verdict":
        f"""
This internship opportunity appears legitimate.

The analysis detected {positive_count} positive trust indicators and only {negative_count} risk indicators.

The company information, structure, and communication style resemble genuine internship offers.

Applicants should still verify recruiter identity before sharing personal documents.
        """
        }


    elif score>=60:

        return{

        "status":"CAUTION",

        "trust":"MEDIUM TRUST",

        "verdict":
        f"""
This internship offer contains both positive and negative indicators.

The system found {positive_count} positive signals and {negative_count} potential concerns.

Additional verification of recruiter details and company authenticity is recommended.
        """
        }


    elif score>=40:

        return{

        "status":"RISKY",

        "trust":"LOW TRUST",

        "verdict":
        f"""
Several warning signs were detected.

The analysis found {negative_count} risk indicators that may affect the credibility of this opportunity.

Proceed carefully and independently verify all company information.
        """
        }


    else:

        return{

        "status":"SCAM ALERT",

        "trust":"VERY LOW TRUST",

        "verdict":
        f"""
This internship offer contains multiple characteristics commonly associated with scams.

The system identified {negative_count} significant risk indicators and limited trust signals.

Avoid making payments or sharing sensitive information until independent verification is completed.
        """
        }