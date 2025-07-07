# STEP 1: Define the Chatbot Personality
def greet():
    print("🤖 Hello! I'm CryptoBuddy — your friendly crypto analyst!")
    print("Ask me about trending, sustainable, or profitable coins!")
    print("Type 'exit' to end the chat.\n")

# STEP 2: Predefined Crypto Dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# STEP 3: Chatbot Core Logic
def analyze_query(user_query):
    user_query = user_query.lower()

    # Most sustainable coin
    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 I recommend {recommend}! It’s eco-friendly and has long-term potential."

    # Trending up coin
    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 These coins are trending up: {', '.join(trending)}."

    # Profitable investment
    elif "profit" in user_query or "long-term" in user_query or "invest" in user_query:
        profitable = [coin for coin, data in crypto_db.items()
                      if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if profitable:
            return f"💰 For long-term growth, consider: {', '.join(profitable)}."
        else:
            return "🤔 No coin meets all profitability conditions right now."

    # Specific coin info
    else:
        for coin in crypto_db:
            if coin.lower() in user_query:
                data = crypto_db[coin]
                return (f"{coin} info:\n"
                        f"📊 Trend: {data['price_trend'].capitalize()}\n"
                        f"💼 Market Cap: {data['market_cap'].capitalize()}\n"
                        f"⚡ Energy Use: {data['energy_use'].capitalize()}\n"
                        f"🌿 Sustainability: {data['sustainability_score']*10}/10")
    
        return "😕 Sorry, I couldn't understand that. Try asking about trends, sustainability, or specific coins."

# STEP 4: Run the Chatbot
def run_bot():
    greet()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("👋 Bye! Remember: crypto is risky—do your own research!")
            break
        response = analyze_query(user_input)
        print("CryptoBuddy:", response)
        print()

# Start the bot
run_bot()
