from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_ai_explanation(
    internship_text,
    score,
    reasons
):

    try:

        prompt = f"""
        You are YESCAPE AI.

        Internship:
        {internship_text}

        YEScore:
        {score}/100

        Detection reasons:
        {reasons}

        Explain:
        - why safe/risky
        - warning signs
        - trust summary

        Keep concise.
        """

        response = client.chat.completions.create(
            model="google/gemma-3-12b-it:free",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"AI analysis unavailable: {str(e)}"