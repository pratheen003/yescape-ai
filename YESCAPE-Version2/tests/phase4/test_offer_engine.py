from signals.signal1_offer.offer_engine import OfferAnalysisEngine


engine = OfferAnalysisEngine()

sample = """

Congratulations.

Google Internship Program.

Website:

careers.google.com

Contact:

hr@google.com

Monthly stipend ₹25000

"""

result = engine.analyze(sample)

print()

print("Confidence :", result["confidence"])

print()

print(result["fields_found"])

print()

offer = result["offer_data"]

print("Company :", offer.company)

print("Website :", offer.website)

print("Email   :", offer.recruiter_email)

print("Salary  :", offer.salary)