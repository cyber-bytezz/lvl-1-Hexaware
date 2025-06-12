from google import genai
from stt_transcriber import transcribe_audio
 
# -- Configuration --
AUDIO_FILE = "audio_clips/input.wav"
GEMINI_API_KEY = "AIzaSyA9mR-a6u8GYYnai5VaFTpXdcAh5c-59TM"
MODEL_NAME = "gemini-2.0-flash"  # or use "gemini-1.5-pro" for long context
 
def generate_ticket(transcript: str):
    # Initialize Gemini client
    client = genai.Client(api_key=GEMINI_API_KEY)
 
    # Construct prompt
    prompt = f"""
You are an AI support assistant. Read the transcript below and generate a structured ticket in JSON.
 
Respond only in this format:
 
{{
  "issue_summary": "<short summary>",
  "category": "<login, billing, crash, etc.>",
  "priority": "<low | medium | high>",
  "follow_up_question": "<ask the user one relevant question>"
}}
 
Transcript:
\"\"\"{transcript}\"\"\"
"""
 
    # Gemini API call
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
 
    print("\n--- AI Generated Ticket ---\n")
    print(response.text)
 
if __name__ == "__main__":
    print("[🎙️] Transcribing audio...")
    transcript = transcribe_audio(AUDIO_FILE)
    print("[📝] Transcript:", transcript)
    generate_ticket(transcript)