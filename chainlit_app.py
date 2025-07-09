from dotenv import load_dotenv
import chainlit as cl
from travel_coordinator import TravelCoordinator

load_dotenv()

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("coordinator", TravelCoordinator())
    await cl.Message(content="🌍 Dreaming of the perfect escape? Just tell me your travel vibe — and I'll whip up a custom-made adventure with destinations, flights, food, and fun! ✈️🍜🏞️").send()

@cl.on_message
async def handle_message(message: cl.Message):
    coordinator = cl.user_session.get("coordinator") 
    user_input = message.content

    try:
        await cl.Message(content="✈️ Planning your trip...").send()
        plan = await coordinator.plan_travel(user_input)

        # Format and send the response
        msg = f"""📍 **Destination:** {plan['destination']['city']}, {plan['destination']['country']}
{plan['destination']['description']}
Highlights: {", ".join(plan['destination']['highlights'])}

✈️ **Flights**:
"""
        for flight in plan['booking']['flights'][:2]:
            msg += f"- {flight['airline']} {flight['flight_number']}, ${flight['price']}, {flight['departure']} → {flight['arrival']}\n"

        msg += f"\n🏨 **Hotels**:\n"
        for hotel in plan['booking']['hotels'][:2]:
            msg += f"- {hotel['name']} (${hotel['price_per_night']}/night, ⭐ {hotel['rating']}) at {hotel['location']}\n"

        msg += f"\n🎯 **Attractions**:\n"
        for attraction in plan['exploration']['attractions']:
            msg += f"- {attraction['name']}: {attraction['description']}\n"

        msg += f"\n🍽️ **Restaurants**:\n"
        for rest in plan['exploration']['restaurants']:
            msg += f"- {rest['name']} ({rest['cuisine']}): {rest['specialty']}\n"

        await cl.Message(content=msg).send()

    except Exception as e:
        await cl.Message(content=f"❌ Something went wrong: {e}").send()
