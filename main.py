import os
import requests  # 1. Added to allow secure HTTP verification calls to Cloudflare
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from google import genai
from google.genai import types

app = FastAPI()

# Allow your Canva website to securely communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Updated schema to expect the incoming captcha token from your index.html
class ChatRequest(BaseModel):
    message: str
    captcha_token: str

# System Instructions with Guardrails & Local Alignment
SYSTEM_INSTRUCTION = """
You are the BridgeAIPH Social Media Planner, a helpful marketing concierge for Filipino MSMEs.
Your goal is to help local businesses create content to boost their direct sales on social media.

GUARDRAILS:
1. Before providing any content, you MUST gather 3 pieces of information: Business Name, Precise Philippine Location, and Target Product/Service. If any are missing, politely ask for them.
2. If the user digresses or talks about something other than social media marketing, politely redirect them back to their mission as a social media concierge.

TONE & LANGUAGE:
Speak naturally in light, conversational Taglish (a blend of English and Tagalog) to match how local consumers interact online.

DELIVERABLE:
Once you have the 3 parameters, generate a 3-post weekly content plan formatted for immediate use:
Post 1: Educational (brand value/transparency)
Post 2: Engaging Hook (humor, puns, or local cultural references to drive comments)
Post 3: Promotional (direct call-to-action with local delivery/GCash context)
"""

# Initialize the Gemini Client securely
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is missing!")

client = genai.Client(api_key=api_key)

# 3. Secure your Cloudflare validation point
# PASTE YOUR PRIVATE SECRET KEY FROM CLOUDFLARE INSIDE THE QUOTES BELOW:
CLOUDFLARE_SECRET_KEY = "0x4AAAAAADuoyNVLmJGy7cueGPTKkC47VD8"

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # A. Intercept the request and verify the captcha token with Cloudflare
    try:
        verify_response = requests.post(
            "https://challenges.cloudflare.com/turnstile/v0/siteverify",
            data={
                "secret": CLOUDFLARE_SECRET_KEY,
                "response": request.captcha_token
            },
            timeout=5 # Safe timeout to ensure performance doesn't hang
        )
        captcha_result = verify_response.json()
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Security service verification failed: {str(err)}")
        
    # B. If Cloudflare determines it's an automated bot request, slam the door shut instantly
    if not captcha_result.get("success"):
        raise HTTPException(status_code=401, detail="Access Denied. Invalid security token.")

    # C. If a verified human passes, proceed normally to calculate your Gemini model logic
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=request.message,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.7,
                )
            )
        return {"reply": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# This serves your beautiful new index.html layout automatically when someone loads the link!
@app.get("/index.html", response_class=HTMLResponse)
def serve_interface():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"<h3>Error loading interface: {str(e)}</h3>"
