from openai import OpenAI
import json
import os
import random
from typing import Dict

class DestinationAgent:
    """Analyzes user preferences and recommends a travel destination."""

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    async def find_destination(self, user_input: str) -> Dict[str, str]:
        prompt = f"""Based on this travel request: "{user_input}"

Analyze the user's preferences and suggest a destination.
Consider:
- Mood, interests, season, food, weather, budget, adventure
Return JSON in format:
{{
    "city": "destination city name",
    "country": "country name", 
    "description": "why it's ideal",
    "highlights": ["one", "two", "three"]
}}"""

        try:
            response = self.client.chat.completions.create(
                model="deepseek/deepseek-r1:free",
                messages=[
                    {"role": "system", "content": "You are a travel expert. Respond in valid JSON only."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            content = response.choices[0].message.content.strip()

        
            if content.startswith("```"):
                content = content.replace("```json", "").replace("```", "").strip()

            print("🧠 MODEL RESPONSE (Cleaned Destination):", content)
            return json.loads(content)

        except Exception as e:
            print(f"DestinationAgent fallback: {e}")
            return random.choice([
                {
                    "city": "Kyoto",
                    "country": "Japan",
                    "description": "Peaceful temples, vibrant food scene, and cherry blossoms in season.",
                    "highlights": ["Fushimi Inari Shrine", "Gion District", "Kaiseki Cuisine"]
                },
                {
                    "city": "Rome",
                    "country": "Italy",
                    "description": "Perfect for history, art, and Italian cuisine lovers.",
                    "highlights": ["Colosseum", "Vatican", "Pasta and Pizza"]
                },
                {
                    "city": "Barcelona",
                    "country": "Spain",
                    "description": "Great mix of beach, architecture, and tapas.",
                    "highlights": ["Sagrada Familia", "La Rambla", "Tapas Bars"]
                },
                {
                    "city": "Istanbul",
                    "country": "Turkey",
                    "description": "Fusion of East and West with historical charm.",
                    "highlights": ["Blue Mosque", "Grand Bazaar", "Turkish Cuisine"]
                }
            ])
