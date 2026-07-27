from signals.signal1_offer.offer_parser import OfferParser


parser = OfferParser()

sample = """

Congratulations.

You have been selected for Google's Internship Program.

Visit:

careers.google.com

Monthly stipend ₹25000

Contact:

hr@google.com

"""

offer = parser.parse(sample)

print()

print("Company :", offer.company)

print("Email   :", offer.recruiter_email)

print("Website :", offer.website)

print("Salary  :", offer.salary)