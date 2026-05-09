<div align="center">

```
 ╔═══════════════════════════════════════════════════════════════╗
 ║          ◈  P R O F I T  C A L C U L A T O R  P R O          ║
 ║          Forex · Indices · Metals · Crypto  |  v5.0           ║
 ╚═══════════════════════════════════════════════════════════════╝
```

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.x-BC8CFF?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-30363D?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-3FB950?style=flat-square)
![Version](https://img.shields.io/badge/Version-5.0-F0883E?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-3FB950?style=flat-square)

<br/>

**A professional desktop trading calculator for Forex, Indices, Metals & Crypto.**
Real-time position risk warnings, live crypto prices, multi-lot/amount breakdowns,
and full P&L analysis — all in a dark terminal UI built with Python.

<br/>

> 💡 *"Does the calculator flag position sizing errors before entry or just show them after?"*
> **v5.0 answers this. Risk is analyzed BEFORE you trade.**

</div>

---

## ✨ What's New in v5.0

### ⚠ Position Risk Warning System
The calculator now **warns you BEFORE entering a trade**, not after.

| Risk Level | Condition | Color |
|---|---|---|
| ✅ **SAFE** | Risk ≤ 1% of account | Green |
| ⚠ **MODERATE** | Risk ≤ 2% of account | Gold/Yellow |
| 🔴 **HIGH RISK** | Risk ≤ 5% of account | Red |
| ☠ **ACCOUNT DANGER** | Risk > 5% of account | Critical Red |

- **Safe Lot / Safe Amount** — automatically recommends correct position size for 2% risk
- **Risk % per lot** — shown in multi-lot breakdown table for every lot size
- **Liquidation Risk** — crypto tab shows how far price is from liquidation level (%)
- **Account Balance field** — added to both tabs as the foundation for all risk calculations

---

## 🗂 Features

### 📈 Forex / Indices / Metals Tab

| Feature | Detail |
|---|---|
| Instruments | 14 pairs — EUR/USD, GBP/USD, USD/JPY, XAU/USD, NAS100, US30, UK100 and more |
| Pip & Points | Instant calculation of pips moved, points, move % |
| BUY / SELL | Color-coded direction toggle — green/red |
| Entry, Exit, SL, TP | All four price inputs with live recalculation |
| Lot Sizes | Standard (1.0), Mini (0.1), Micro (0.01), Nano (0.001) + custom |
| Risk Analysis | Real-time risk % and dollar risk based on account balance + SL |
| Safe Lot Size | Recommended lot for exactly 2% account risk |
| Multi-Lot Table | P&L and Risk % for all 4 lot sizes simultaneously |
| Account Currency | USD, PKR ₨, EUR, GBP |
| Custom Pair | Set your own pip size and pip value |

### ₿ Crypto Calculator Tab

| Feature | Detail |
|---|---|
| Pairs | 15 coins — BTC, ETH, BNB, XRP, SOL, ADA, DOGE, AVAX, LINK, DOT, MATIC, LTC, UNI, ATOM, XLM |
| Live Prices | Auto-fetched from Binance API on pair selection |
| Leverage | Slider from 1x (Spot) to 100x with real-time recalculation |
| Risk Warning | Position risk analysis with badge, color panel, and message |
| Safe Amount | Recommended coin amount for 2% account risk |
| Liquidation Price | Estimated liq. price + distance percentage |
| Margin Used | Required margin for leveraged positions |
| Multi-Amount Table | P&L in USD + PKR + Risk % for 7 position sizes (0.001 → 10 coins) |
| Custom Coin | Enter your own coin for unlisted assets |

### 🎨 UI / UX

- Dark terminal aesthetic — GitHub-inspired color palette
- Scrollable panels — no hidden buttons at any screen size
- Two-tab layout — Forex and Crypto fully separated
- Real-time recalculation on every keystroke
- Color-coded outputs — green profit, red loss, gold warning
- Risk panel background changes color based on risk level

---

## 🚀 Quick Start

### Requirements

- Python 3.8 or higher
- Internet connection (for live crypto prices)

### Install dependency

```bash
pip install customtkinter
```

### Run

```bash
python forex_crypto_v5.py
```

---

## 📦 Full Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Navigate into the folder
cd YOUR_REPO_NAME

# Install dependency
pip install customtkinter

# Run
python forex_crypto_v5.py
```

---

## 🧮 Formulas Used

### Forex
```
Pips     = |Exit − Entry| ÷ Pip Size
Points   = Pips × 10
P&L      = Pips × Pip Value × Lots
Risk %   = (SL Pips × Pip Value × Lots) ÷ Account Balance × 100
Safe Lot = (Account Balance × 0.02) ÷ (SL Pips × Pip Value)
R:R      = TP Pips ÷ SL Pips
```

### Crypto
```
P&L           = (Exit − Entry) × Amount × Leverage
Margin Used   = Entry × Amount ÷ Leverage
Liq. Price    = Entry × (1 − 1/Leverage)   [BUY]
              = Entry × (1 + 1/Leverage)   [SELL]
Risk %        = SL Loss ÷ Account Balance × 100
Safe Amount   = (Account Balance × 0.02) ÷ (SL Distance × Leverage)
```

---

## 📁 Project Structure

```
your-repo/
│
├── forex_crypto_v5.py      ← Main application
├── README.md               ← This file
├── requirements.txt        ← Python dependencies
└── screenshots/            ← Add your UI screenshots here
    ├── forex_tab.png
    └── crypto_tab.png
```

---

## 📋 requirements.txt

```
customtkinter>=5.0.0
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🌍 Supported Instruments

### Forex & Metals
`EUR/USD` `GBP/USD` `USD/JPY` `EUR/JPY` `GBP/JPY` `USD/CAD`
`AUD/USD` `NZD/USD` `USD/CHF` `XAU/USD` `XAG/USD` `Custom`

### Indices
`NAS100` `US30` `UK100`

### Crypto (via Binance API)
`BTC/USDT` `ETH/USDT` `BNB/USDT` `XRP/USDT` `SOL/USDT` `ADA/USDT`
`DOGE/USDT` `AVAX/USDT` `LINK/USDT` `DOT/USDT` `MATIC/USDT` `LTC/USDT`
`UNI/USDT` `ATOM/USDT` `XLM/USDT` `Custom`

---

## 💱 Supported Account Currencies

| Symbol | Currency |
|--------|----------|
| $ | US Dollar (USD) |
| ₨ | Pakistani Rupee (PKR) |
| € | Euro (EUR) |
| £ | British Pound (GBP) |

---

## ⚙️ How to Use

### Forex Tab
1. Enter your **Account Balance** at the top
2. Select your **Currency Pair**
3. Choose **BUY** or **SELL**
4. Enter **Entry Price**, **Exit Price**, **Stop Loss**, **Take Profit**
5. Select or type your **Lot Size**
6. Choose **Account Currency**
7. Click **CALCULATE** — or just type, results update live

### Crypto Tab
1. Enter your **Account Balance**
2. Select your **Crypto Pair** — live price auto-fills entry
3. Choose **BUY** or **SELL**
4. Enter **Entry Price** and **Exit Price**
5. Set **Stop Loss** and **Take Profit**
6. Enter **Coin Amount**
7. Drag the **Leverage Slider** — 1x means Spot trading
8. Risk warnings and results update instantly

---

## 🔧 Customization

### Update PKR exchange rate

```python
CURRENCIES = {
    "USD": ("$",  1.0),
    "PKR": ("₨", 278.0),   # ← update this number
    "EUR": ("€",  0.92),
    "GBP": ("£",  0.79),
}
```

### Change risk thresholds

```python
RISK_SAFE   = 1.0   # <= 1%  → SAFE   (green)
RISK_WARN   = 2.0   # <= 2%  → WARN   (gold)
RISK_DANGER = 5.0   # >  2%  → DANGER (red)
```

### Add a new Forex pair

```python
FOREX_PAIRS = {
    ...
    "EUR/GBP": {"pip": 0.0001, "pip_val": 10.0, "decimals": 5},
}
```

### Add a new Crypto pair

```python
CRYPTO_PAIRS = {
    ...
    "PEPE/USDT": {"symbol": "PEPEUSDT", "decimals": 8},
}
```

---

## 📝 Changelog

### v5.0 — Position Risk Warnings *(Latest)*
- Account Balance field added to both tabs
- Real-time Position Risk Analysis panel with color-coded status
- Safe Lot / Safe Amount recommendation at 2% risk
- Risk % column in multi-lot and multi-amount breakdown tables
- Liquidation Risk distance % for crypto leveraged trades
- Panel background color changes per risk level

### v4.0 — Layout Fix
- Scrollable left and right panels
- No more hidden buttons on smaller screens
- Window size increased to 1100×900

### v3.0 — Crypto Tab Added
- Full Crypto Calculator tab with 15 pairs
- Live prices via Binance API
- Leverage slider 1x–100x
- Liquidation price estimation
- Multi-amount breakdown with PKR column

### v2.0 — Forex Calculator
- 14 Forex / Indices / Metal instruments
- Multi-lot breakdown table
- Risk/Reward ratio
- PKR account currency support

### v1.0 — Initial Release
- Basic pip and P&L calculator

---

## ⚠️ Disclaimer

> This tool is built **for educational and analytical purposes only.**
> It does not constitute financial advice. Always do your own research
> before placing real trades. Trading involves significant risk of loss.
> Past performance is not indicative of future results.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

```bash
# Fork → Clone → Create branch
git checkout -b feature/my-feature

# Commit
git commit -m "Add my feature"

# Push
git push origin feature/my-feature

# Open a Pull Request on GitHub
```

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

### 📢 Stay Updated
Join our WhatsApp channel for daily cyber updates, vulnerability write-ups, and security news!

👉 **[Join Our WhatsApp Channel](https://whatsapp.com/channel/0029Vb5n1UC7oQhYnrlUBD26)**

---
*Maintained by **Muhammad Rehan Afzal** | Founder, TeamCyberOps*
---
<div align="center">

Made with ❤️ for traders · **[@rehan-qx]**

</div>
