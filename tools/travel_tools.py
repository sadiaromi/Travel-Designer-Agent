import asyncio
import random

async def get_flights(destination: str, origin: str = "New York"):
    await asyncio.sleep(0.5)
    airlines = ["Delta", "American", "United", "Emirates", "Lufthansa", "British Airways"]
    return [{
        "airline": airline,
        "flight_number": f"{airline[:2].upper()}{random.randint(1000, 9999)}",
        "departure": f"{origin} {10+i}:00AM",
        "arrival": f"{destination} {3+i}:30PM",
        "price": random.randint(400, 1200),
        "duration": f"{6+i}h {10+i*5}m"
    } for i, airline in enumerate(random.sample(airlines, 3))]

async def suggest_hotels(destination: str):
    await asyncio.sleep(0.5)
    hotel_types = ["Grand Hotel", "Boutique Inn", "Luxury Resort", "Historic Palace", "Modern Suites"]
    return [{
        "name": f"{random.choice(hotel_types)} {destination}",
        "rating": round(4 + random.random(), 1),
        "location": f"{destination} City Center",
        "price_per_night": random.randint(100, 400),
        "amenities": random.sample(["WiFi", "Pool", "Spa", "Restaurant", "Gym"], 2)
    } for _ in range(3)]

async def get_attractions(destination: str):
    templates = [
        f"{destination} Museum",
        f"Historic {destination} Cathedral",
        f"{destination} Central Park",
        f"{destination} Market Square",
        f"{destination} Old Town",
        f"{destination} Cultural Center",
        f"{destination} Art Walk"
    ]
    descriptions = [
        "Famous for its architecture and exhibits.",
        "Beautiful blend of tradition and culture.",
        "Great for relaxation and family walks.",
        "Offers vibrant food and local experiences.",
        "A must-visit for first-timers."
    ]
    return [{"name": name, "description": random.choice(descriptions)} for name in random.sample(templates, 3)]

async def get_restaurants(destination: str):
    names = [
        f"Le {destination}",
        f"{destination} Bistro",
        f"Café {destination}",
        f"{destination} Grill",
        f"Mama {destination}",
        f"{destination} Street Eats"
    ]
    cuisines = ["Italian", "Turkish", "Mediterranean", "French", "Japanese", "Thai"]
    specialties = ["Seafood platters", "Home-style classics", "Modern fusion", "Spiced rice bowls", "Tapas and wine"]
    return [{
        "name": name,
        "cuisine": random.choice(cuisines),
        "specialty": random.choice(specialties)
    } for name in random.sample(names, 3)]
