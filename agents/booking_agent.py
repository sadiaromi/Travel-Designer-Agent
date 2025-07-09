from tools.travel_tools import get_flights, suggest_hotels
from typing import Dict 

class BookingAgent:
    """Handles booking-related tasks using travel tools"""
    
    async def handle_booking(self, destination: Dict[str, str], user_input: str) -> Dict[str, list]:
        """Fetch flight and hotel suggestions for a destination"""
        city = destination.get('city', 'Paris')
        
        flights = await get_flights(city)
        hotels = await suggest_hotels(city)
        
        return {
            "flights": flights,
            "hotels": hotels
        }
