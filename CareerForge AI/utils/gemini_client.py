from groq import Groq

client = Groq(
    api_key="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"
)

def ask_gemini(prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content