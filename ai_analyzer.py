import json
from groq import Groq

# Replace with your Groq API key
client = Groq(
    api_key="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"
)

def analyze_resume(resume_text, job_description):
    prompt = f"""
    You are an expert ATS Resume Analyzer.

    Compare the resume with the job description.

    Return ONLY valid JSON.

    Use this format exactly:

    {{
        "ats_score":85,
        "match_percentage":80,
        "technical_skills":["Python"],
        "missing_skills":["SQLite"],
        "strengths":"...",
        "weaknesses":"...",
        "suggestions":"...",
        "resume_summary":"...",
        "candidate_level":"Fresher"
    }}

    Resume:

    {resume_text}

    Job Description:

    {job_description}
    """



    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    text = response.choices[0].message.content.strip()

    # Remove markdown if AI returns ```json ... ```
    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    try:
        result = json.loads(text)
        return result

    except json.JSONDecodeError:
        return {
            "ats_score": 0,
            "match_percentage": 0,
            "technical_skills": [],
            "missing_skills": [],
            "strengths": "",
            "weaknesses": "",
            "suggestions": text,
            "resume_summary": "",
            "candidate_level": ""
        }