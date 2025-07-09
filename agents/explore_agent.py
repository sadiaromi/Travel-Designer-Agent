from openai import OpenAI
import json
import os
from tools.travel_tools import get_attractions, get_restaurants
from typing import Dict

class ExploreAgent:
    """Suggests personalized attractions and restaurants based on destination and user preferences."""

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    async def suggest_activities(self, destination: Dict[str, str], user_input: str) -> Dict[str, list]:
        city = destination.get('city', 'Rome')
        country = destination.get('country', '')

        attractions = await get_attractions(city)
        restaurants = await get_restaurants(city)

        prompt = f"""Customize these travel recommendations for {city}, {country}.
User said: "{user_input}"

Attractions: {json.dumps(attractions)}
Restaurants: {json.dumps(restaurants)}

Make the suggestions personal and relevant.
Respond in this exact JSON format:
{{
  "attractions": [{{"name": "...", "description": "..."}}],
  "restaurants": [{{"name": "...", "cuisine": "...", "specialty": "..."}}]
}}"""

        try:
            response = self.client.chat.completions.create(
                model="deepseek/deepseek-r1:free",
                messages=[
                    {"role": "system", "content": "You are a helpful travel planner. Respond in valid JSON only."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            content = response.choices[0].message.content.strip()
            if content.startswith("```"):
                content = content.replace("```json", "").replace("```", "").strip()

            print("🧠 MODEL RESPONSE (Cleaned Explore):", content)
            return json.loads(content)

        except Exception as e:
            print(f"ExploreAgent fallback: {e}")
            return {
                "attractions": attractions,
                "restaurants": restaurants
            }
