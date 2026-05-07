# ◈ Profit Calculator Pro — v3.0

> **Forex · Indices · Metals · Crypto** — Advanced pip & profit calculator with live crypto prices, multi-currency support, and a dark terminal-style UI.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.x-1F6FEB?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-3FB950?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-58A6FF?style=flat-square)

---

## 📸 Overview

**Profit Calculator Pro** is a desktop application built with Python and CustomTkinter that helps forex and crypto traders instantly calculate pips, profit/loss, risk-to-reward ratios, and multi-lot breakdowns — all in a sleek dark terminal aesthetic.

```
╔══════════════════════════════════════════════════════════════════╗
║     FOREX + CRYPTO PIP & PROFIT CALCULATOR — Advanced UI v3.0   ║
║     Built with CustomTkinter | Dark Terminal Style               ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## ✨ Features

### 📈 Forex / Indices / Metals Tab
- **15+ instruments** — EUR/USD, GBP/USD, USD/JPY, XAU/USD, NAS100, US30, UK100, and more
- **Pip & point calculation** with per-pair pip sizes and values
- **BUY / SELL direction** toggle with visual color feedback
- **Entry, Exit, Stop Loss, and Take Profit** price inputs
- **Lot size presets** — Standard, Mini, Micro, Nano — plus manual entry
- **Multi-lot breakdown table** — P&L for all lot sizes at a glance
- **Risk/Reward ratio** calculated automatically from SL/TP
- **Custom pair support** — define your own pip size and pip value

### ₿ Crypto Calculator Tab
- **15+ crypto pairs** — BTC/USDT, ETH/USDT, SOL/USDT, DOGE/USDT, and more
- **Live price feed** via Binance API (fetched in background thread)
- **Leverage slider** from 1× (spot) up to 100× with liquidation price estimate
- **Margin used** display for leveraged positions
- **Multi-amount breakdown** — P&L across 7 position sizes simultaneously
- **PKR column** always shown in the breakdown for Pakistani traders
- **Custom coin support** with manual name input

### 🌐 Shared Features
- **Multi-currency accounts** — USD, PKR, EUR, GBP
- **Real-time calculation** — results update on every keystroke
- **Dark terminal UI** built with CustomTkinter
- Fully responsive window with scrollable panels

---

## 🖥️ Screenshots

> The application uses a dark `#0D1117` background with a blue accent (`#58A6FF`), green/red P&L indicators, and monospaced Courier font throughout for a professional trading terminal feel.

| Panel | Description |
|---|---|
| **Trade Parameters** | Left panel — inputs for pair, direction, prices, lot/amount |
| **Live Results** | Right panel — pips, P&L, pip value, move % |
| **Risk / Reward** | SL pips, TP pips, and R:R ratio cards |
| **Multi-Lot Breakdown** | Table showing P&L for every standard lot size |

---

## ⚙️ Requirements

- Python **3.8** or higher
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter) — modern UI framework

```bash
pip install customtkinter
```

No other external packages are required. The price feed uses Python's built-in `urllib` and `json` modules.

---

## 🚀 Installation & Usage

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/profit-calculator-pro.git
cd profit-calculator-pro
```

**2. Install dependencies**
```bash
pip install customtkinter
```

**3. Run the application**
```bash
python calculator.py
```

---

## 📦 Supported Instruments

### Forex & CFDs
| Pair | Pip Size | Pip Value |
|------|----------|-----------|
| EUR/USD | 0.0001 | $10.00 |
| GBP/USD | 0.0001 | $10.00 |
| USD/JPY | 0.01   | $9.09  |
| EUR/JPY | 0.01   | $9.09  |
| GBP/JPY | 0.01   | $9.09  |
| USD/CAD | 0.0001 | $7.69  |
| AUD/USD | 0.0001 | $10.00 |
| NZD/USD | 0.0001 | $10.00 |
| USD/CHF | 0.0001 | $10.90 |
| XAU/USD | 0.1    | $1.00  |
| XAG/USD | 0.01   | $5.00  |
| NAS100  | 1.0    | $1.00  |
| US30    | 1.0    | $1.00  |
| UK100   | 1.0    | $1.30  |
| Custom  | *(user-defined)* | *(user-defined)* |

### Crypto Pairs (Live Prices via Binance)
`BTC/USDT` · `ETH/USDT` · `BNB/USDT` · `XRP/USDT` · `SOL/USDT` · `ADA/USDT` · `DOGE/USDT` · `AVAX/USDT` · `LINK/USDT` · `DOT/USDT` · `MATIC/USDT` · `LTC/USDT` · `UNI/USDT` · `ATOM/USDT` · `XLM/USDT` · `Custom`

---

## 🧮 Calculation Formulas

### Forex P&L
```
Pips Moved  = |Exit − Entry| ÷ Pip Size
P&L (USD)   = Signed Pips × Pip Value × Lots
P&L (Local) = P&L (USD) × Account Currency Rate
R:R Ratio   = TP Pips ÷ SL Pips
```

### Crypto P&L
```
P&L (USD)       = (Exit − Entry) × Amount × Leverage
Position Value  = Entry Price × Amount
Margin Used     = Position Value ÷ Leverage
Liq. Price (BUY)  = Entry × (1 − 1/Leverage)
Liq. Price (SELL) = Entry × (1 + 1/Leverage)
```

---

## 🗂️ Project Structure

```
profit-calculator-pro/
│
├── calculator.py          # Main application (single-file)
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

**`requirements.txt`**
```
customtkinter>=5.0.0
```

---

## 🎨 UI Color Palette

| Token | Hex | Usage |
|---|---|---|
| `bg` | `#0D1117` | Main background |
| `panel` | `#161B22` | Side panels |
| `card` | `#1C2333` | Result cards |
| `accent` | `#58A6FF` | Forex highlights |
| `green` | `#3FB950` | Profit / BUY |
| `red` | `#F85149` | Loss / SELL |
| `gold` | `#D29922` | R:R ratio / warnings |
| `purple` | `#BC8CFF` | Crypto tab theme |

---

## ⚠️ Disclaimer

> This application is built **for educational and informational purposes only**. It does not constitute financial advice. All P&L figures are estimates based on the formulas above and may not reflect actual broker spreads, commissions, or slippage. Always verify calculations with your broker before placing trades.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- UI framework: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) by Tom Schimansky
- Live price data: [Binance Public API](https://api.binance.com)

---

### 📢 Stay Updated
Join our WhatsApp channel for daily cyber & Crypto updates, vulnerability write-ups, and security news!

👉 **[Join Our WhatsApp Channel](https://whatsapp.com/channel/0029Vb5n1UC7oQhYnrlUBD26)**

---
*Maintained by **Muhammad Rehan Afzal** | Founder, TeamCyberOps*
