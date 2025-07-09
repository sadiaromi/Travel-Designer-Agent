from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent
from lib.agent_runner import AgentRunner

class TravelCoordinator:
    def __init__(self):
        self.runner = AgentRunner()
        self.destination_agent = DestinationAgent()
        self.booking_agent = BookingAgent()
        self.explore_agent = ExploreAgent()
        
        # Register agents with runner
        self.runner.register_agent("destination", self.destination_agent)
        self.runner.register_agent("booking", self.booking_agent)
        self.runner.register_agent("explore", self.explore_agent)
    
    async def plan_travel(self, user_input: str):
        """Coordinate between agents to create complete travel plan"""
        
        # Step 1: Destination Agent - Find perfect destination
        print("🔍 DestinationAgent: Finding your perfect destination...")
        destination = await self.runner.handoff("destination", {
            "method": "find_destination",
            "args": [user_input]
        })
        
        # Step 2: Booking Agent - Handle flights and hotels  
        print("✈️  BookingAgent: Getting flights and hotels...")
        booking = await self.runner.handoff("booking", {
            "method": "handle_booking", 
            "args": [destination, user_input]
        })
        
        # Step 3: Explore Agent - Suggest activities and food
        print("🎯 ExploreAgent: Finding attractions and restaurants...")
        exploration = await self.runner.handoff("explore", {
            "method": "suggest_activities",
            "args": [destination, user_input]
        })
        
        return {
            "destination": destination,
            "booking": booking, 
            "exploration": exploration
        }
