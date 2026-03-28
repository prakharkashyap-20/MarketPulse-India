import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import requests
from textblob import TextBlob

st.set_page_config(page_title="MarketPulse India", layout="wide", page_icon="📈")

st.markdown("""
<style>
    .stApp { background-color: #0a0e1a; color: #00ff88; }
    .block-container { padding: 1rem 2rem; }
    h1, h2, h3 { color: #00ff88; font-family: 'Courier New'; }
    .metric-card {
        background: #111827;
        border: 1px solid #00ff8844;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("## 📡 MarketPulse India — Geopolitical Market Tracker")
st.markdown("---")

# --- PRICE CARDS ---
def get_price(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="2d", interval="1d")
    if data.empty:
        return None, None
    close = data['Close'].iloc[-1]
    prev = data['Close'].iloc[-2]
    change = ((close - prev) / prev) * 100
    return round(close, 2), round(change, 2)

nifty_price, nifty_change = get_price("^NSEI")
sensex_price, sensex_change = get_price("^BSESN")
gold_price, gold_change = get_price("GC=F")
oil_price, oil_change = get_price("CL=F")

col1, col2, col3, col4 = st.columns(4)

def show_card(col, name, price, change):
    arrow = "▲" if change >= 0 else "▼"
    color = "#00ff88" if change >= 0 else "#ff4444"
    col.markdown(f"""
    <div class='metric-card'>
        <h3>{name}</h3>
        <h2 style='color:{color}'>{price}</h2>
        <p style='color:{color}'>{arrow} {change}%</p>
    </div>
    """, unsafe_allow_html=True)

show_card(col1, "NIFTY 50", nifty_price, nifty_change)
show_card(col2, "SENSEX", sensex_price, sensex_change)
show_card(col3, "GOLD", gold_price, gold_change)
show_card(col4, "OIL", oil_price, oil_change)

st.markdown("---")

# --- MAP + NEWS SIDE BY SIDE ---
col_map, col_news = st.columns([1.5, 1])

with col_map:
    st.markdown("### 🌍 Global Tension Map")
    tension_data = {
        "country": ["Russia", "Iran", "United States", "China", "India",
                     "Pakistan", "Israel", "Ukraine", "Germany", "France",
                     "United Kingdom", "Saudi Arabia", "Turkey", "Brazil", "Japan"],
        "tension": [90, 85, 60, 70, 45, 75, 88, 92, 30, 25, 35, 65, 60, 20, 15],
        "status": ["CRITICAL", "CRITICAL", "HIGH", "HIGH", "MEDIUM",
                    "HIGH", "CRITICAL", "CRITICAL", "LOW", "LOW", "LOW", "HIGH", "HIGH", "LOW", "LOW"]
    }
    df = pd.DataFrame(tension_data)
    fig_map = px.choropleth(
        df,
        locations="country",
        locationmode="country names",
        color="tension",
        hover_name="country",
        hover_data=["status"],
        color_continuous_scale=["#00ff88", "#ffd700", "#ff4444"],
        range_color=[0, 100],
    )
    fig_map.update_layout(
        paper_bgcolor='#0a0e1a',
        font_color='#00ff88',
        geo=dict(
            bgcolor='#0a0e1a',
            showframe=False,
            showcoastlines=True,
            coastlinecolor="#333333",
            showland=True,
            landcolor="#1a1a2e",
            showocean=True,
            oceancolor="#0a0e1a",
        ),
        coloraxis_colorbar=dict(
            title="Tension",
            tickfont=dict(color="#00ff88"),
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        height=500
    )
    st.plotly_chart(fig_map, use_container_width=True)

with col_news:
    st.markdown("### 📰 Live Geopolitical News")
    NEWS_API_KEY = "bd3af160cb3d4533bc3386e578169ee4"
    url = f"https://newsapi.org/v2/everything?q=india+economy+geopolitics&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()

    if news_data["status"] == "ok":
        articles = news_data["articles"][:8]
        for article in articles:
            title = article["title"]
            source = article["source"]["name"]
            score = TextBlob(title).sentiment.polarity
            if score > 0.1:
                sentiment = "🟢 POSITIVE"
                color = "#00ff88"
            elif score < -0.1:
                sentiment = "🔴 NEGATIVE"
                color = "#ff4444"
            else:
                sentiment = "🟡 NEUTRAL"
                color = "#ffd700"

            st.markdown(f"""
            <div style='background:#111827; border-left: 4px solid {color};
            padding: 0.6rem; margin: 0.4rem 0; border-radius: 5px;'>
                <span style='color:{color}; font-weight:bold; font-size:0.8rem'>{sentiment}</span>
                &nbsp;|&nbsp; <span style='color:#aaa; font-size:0.8rem'>{source}</span><br>
                <span style='color:white; font-size:0.85rem'>{title}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Could not fetch news.")

st.markdown("---")

# --- CANDLESTICK CHARTS ---
def draw_chart(symbol, title):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1mo", interval="1d")
    if data.empty:
        st.error(f"Could not fetch {title} data.")
        return
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        increasing_line_color='#00ff88',
        decreasing_line_color='#ff4444'
    )])
    fig.update_layout(
        paper_bgcolor='#0a0e1a',
        plot_bgcolor='#111827',
        font_color='#00ff88',
        title=title,
        xaxis_rangeslider_visible=False,
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

col_left, col_right = st.columns(2)
with col_left:
    draw_chart("^NSEI", "NIFTY 50 — 1 Month")
with col_right:
    draw_chart("^BSESN", "SENSEX — 1 Month")

st.success("✅ Live market data loaded!")