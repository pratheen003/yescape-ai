def get_verdict(score):


    if score>=80:

        return{

        "status":"SAFE",

        "trust":"HIGH TRUST",

        "verdict":
        "AI found strong legitimacy indicators."
        }


    elif score>=50:

        return{

        "status":"MODERATE",

        "trust":"MEDIUM TRUST",

        "verdict":
        "Some suspicious patterns detected."
        }


    else:

        return{

        "status":"RISK",

        "trust":"LOW TRUST",

        "verdict":
        "Multiple scam indicators found."
        }