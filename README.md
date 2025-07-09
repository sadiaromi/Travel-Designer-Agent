# 🧳 AI Travel Designer Agent

An AI-powered travel planning assistant that helps users design a personalized travel experience — from destination recommendations to hotel, flight, food, and attraction suggestions — using a multi-agent system built with the OpenAI-compatible SDK and Chainlit interface.

---

## ✨ Features

- 🧠 **DestinationAgent**: Recommends the best destination based on user mood, interests, budget, and season.
- ✈️ **BookingAgent**: Provides mock flights and hotels using internal travel tools.
- 🎯 **ExploreAgent**: Suggests local attractions and food spots customized to the user's trip.
- 🤝 **Agent Handoff**: Agents coordinate using a central `TravelCoordinator` and the custom `AgentRunner` class.
- 💬 **Chainlit Interface**: Provides an interactive chat UI to ask for travel planning in natural language.
- 🔧 **Tools Used**: `get_flights()`, `suggest_hotels()`, `get_restaurants()`, `get_attractions()`

---

## 🧩 Tech Stack

- `Python 3.10+`
- `Chainlit`
- `OpenRouter` (free model via `deepseek/deepseek-r1:free`)
- `OpenAI-compatible SDK syntax`
- `Asyncio`, `random`, `dotenv` for environment configuration
- Local `tools/` and `agents/` for modularity

---

## 📁 Folder Structure

```
Travel-Agent/
        ├── agents/
│ ├── destination_agent.py
│ ├── booking_agent.py
│ └── explore_agent.py
├── tools/
│ └── travel_tools.py
├── lib/
│ └── agent_runner.py
├── travel_coordinator.py
├── chainlit_app.py
├── .env
└── README.md

```


---

## 🤖 How It Works

### 1. `DestinationAgent`
- Calls the model (`deepseek/deepseek-r1:free`) via OpenRouter.
- Sends user input (like "romantic beach vacation in summer").
- Returns city, country, description, and highlights as JSON.

### 2. `BookingAgent`
- Uses tools: `get_flights()` and `suggest_hotels()` with mocked data.
- Simulates bookings for the selected destination.

### 3. `ExploreAgent`
- Fetches local restaurants and attractions using tools.
- Personalizes based on user interest (like “I love food and museums”).

### 4. `AgentRunner`
- Simulates OpenAI Agent SDK behavior.
- Passes tasks between agents using `.handoff()`.

---

# 🛠 Setup & Run the App

## 🔹 Step 1: Create & Activate Virtual Environment

uv venv
# For Windows
.\venv\Scripts\activate

### ✅ Step 2: Install dependencies
```bash

uv  add -r requirements.txt

```

### ✅ Step 3: Create .env file

OPENRouter_API_KEY=your-api-key-here

### ✅ Step 4: Run the Chainlit App

chainlit run chainlit_app.py

---

## 💬 Sample Prompts You Can Try

Looking for a food and culture focused trip in Asia.
Suggest a peaceful destination with museums and relaxing vibes.
Where should I go in winter for snow and fun?
I want a short weekend adventure with hiking and local food.

