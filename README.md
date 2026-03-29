# 📡 MarketPulse India — Geopolitical Market Tracker

A real-time web application that tracks Indian stock markets and analyzes how global geopolitical events impact financial markets.

🔗 **Live App:** https://marketpulse-india-67zeoqqq6lwkjhrfpkgsrt.streamlit.app/

---

## 🚀 Features

- 📈 **Live Nifty 50 & Sensex** candlestick charts
- 💰 **Real-time price cards** for Nifty, Sensex, Gold & Oil
- 🌍 **Global Tension Map** — countries color coded by geopolitical tension level
- 📰 **Live news feed** with AI-powered sentiment analysis (Positive/Negative/Neutral)
- 🔴 **Global Tension Index (GTI)** — calculated from live news sentiment

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application framework |
| yfinance | Real-time stock market data |
| Plotly | Interactive charts & world map |
| TextBlob | NLP sentiment analysis |
| NewsAPI | Live geopolitical news feed |
| Pandas | Data manipulation |

---

## 📊 How It Works

1. **Stock Data** — fetched live from Yahoo Finance using yfinance
2. **News Feed** — pulled from NewsAPI with geopolitical keywords
3. **Sentiment Analysis** — each headline analyzed using TextBlob NLP
4. **GTI Score** — calculated as percentage of negative news headlines
5. **Tension Map** — countries colored from green (stable) to red (critical)

---

## 🔧 Installation & Setup
```bash
# Clone the repository
git clone https://github.com/prakharkashyap-20/MarketPulse-India.git

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run MarketPulse/app.py
```

---

## 📌 Project Insights

- Nifty 50 fell from 25,500 to 23,000 in March 2026 — directly correlated with foreign investor selloff triggered by Iran war tensions and global trade war fears
- Gold ▲ 3.4% and Oil ▲ 5.46% — classic safe-haven movement during geopolitical uncertainty
- App demonstrates real-world connection between global events and Indian financial markets

---

## 👨‍💻 Author

**Prakhar Kashyap**
BSc IT — AI & Data Science | IITG Online
- GitHub: [@prakharkashyap-20](https://github.com/prakharkashyap-20)

---

⭐ If you found this project interesting, please give it a star!
