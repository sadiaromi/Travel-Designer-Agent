from typing import Dict, Any
import asyncio

class AgentRunner:
    """Custom Agent Runner for coordinating handoffs between agents"""
    
    def __init__(self):
        self.agents: Dict[str, Any] = {}
        self.current_agent: str = None
        self.execution_history = []
    
    def register_agent(self, name: str, agent: Any):
        """Register an agent with the runner"""
        self.agents[name] = agent
        print(f"✅ Registered {name} agent")
    
    async def handoff(self, to_agent: str, context: Dict[str, Any]):
        """Hand off execution to specified agent"""
        if to_agent not in self.agents:
            raise ValueError(f"Agent {to_agent} not found. Available agents: {list(self.agents.keys())}")
        
        # Update current agent
        previous_agent = self.current_agent
        self.current_agent = to_agent
        
        # Log handoff
        self.execution_history.append({
            "from": previous_agent,
            "to": to_agent,
            "context": context
        })
        
        agent = self.agents[to_agent]
        
        # Execute the agent method with provided context
        method_name = context.get("method")
        args = context.get("args", [])
        
        if not hasattr(agent, method_name):
            raise ValueError(f"Agent {to_agent} does not have method {method_name}")
        
        method = getattr(agent, method_name)
        
        # Execute method (handle both sync and async)
        if asyncio.iscoroutinefunction(method):
            result = await method(*args)
        else:
            result = method(*args)
        
        return result
    
    def get_current_agent(self) -> str:
        """Get currently active agent"""
        return self.current_agent
    
    def get_execution_history(self):
        """Get history of agent handoffs"""
        return self.execution_history
    
    async def execute_workflow(self, workflow: list):
        """Execute a series of agent operations"""
        results = []
        
        for step in workflow:
            agent_name = step.get("agent")
            result = await self.handoff(agent_name, step)
            results.append(result)
        
        return results
    
    def reset(self):
        """Reset runner state"""
        self.current_agent = None
        self.execution_history = []
