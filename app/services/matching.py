from langchain_community.chat_models import ChatOllama  # or ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def compare_resume_with_jd(resume_text: str, jd_text: str) -> str:
    prompt = PromptTemplate.from_template("""
You are an expert career coach. Given the following resume and job description, list:

1. Skills or qualifications that are present in the resume and match the JD.
2. Important skills/requirements in the JD that are missing from the resume.
3. Recommendations to improve the resume for this JD.

--- Resume ---
{resume}

--- Job Description ---
{jd}

Respond in simple, structured points.
""")
    
    chain = LLMChain(
        llm=ChatOllama(model="llama3"),  # or ChatOpenAI(...) with API key
        prompt=prompt
    )
    return chain.run({"resume": resume_text, "jd": jd_text})
