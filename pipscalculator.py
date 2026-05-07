"""
╔══════════════════════════════════════════════════════════════════╗
║     FOREX + CRYPTO PIP & PROFIT CALCULATOR — Advanced UI v3.0   ║
║     Built with CustomTkinter | Dark Terminal Style               ║
╚══════════════════════════════════════════════════════════════════╝
"""

import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import math
import urllib.request
import json
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ─── Color Palette ────────────────────────────────────────────
C = {
    "bg":        "#0D1117",
    "panel":     "#161B22",
    "card":      "#1C2333",
    "border":    "#30363D",
    "accent":    "#58A6FF",
    "green":     "#3FB950",
    "red":       "#F85149",
    "gold":      "#D29922",
    "purple":    "#BC8CFF",
    "orange":    "#F0883E",
    "text":      "#E6EDF3",
    "muted":     "#8B949E",
    "highlight": "#1F6FEB",
    "crypto_bg": "#0F1923",
    "crypto_card":"#1A2535",
}

# ─── Forex Pair Data ──────────────────────────────────────────
FOREX_PAIRS = {
    "EUR/USD": {"pip": 0.0001, "pip_val": 10.0,  "decimals": 5},
    "GBP/USD": {"pip": 0.0001, "pip_val": 10.0,  "decimals": 5},
    "USD/JPY": {"pip": 0.01,   "pip_val": 9.09,  "decimals": 3},
    "EUR/JPY": {"pip": 0.01,   "pip_val": 9.09,  "decimals": 3},
    "GBP/JPY": {"pip": 0.01,   "pip_val": 9.09,  "decimals": 3},
    "USD/CAD": {"pip": 0.0001, "pip_val": 7.69,  "decimals": 5},
    "AUD/USD": {"pip": 0.0001, "pip_val": 10.0,  "decimals": 5},
    "NZD/USD": {"pip": 0.0001, "pip_val": 10.0,  "decimals": 5},
    "USD/CHF": {"pip": 0.0001, "pip_val": 10.90, "decimals": 5},
    "XAU/USD": {"pip": 0.1,    "pip_val": 1.0,   "decimals": 2},
    "XAG/USD": {"pip": 0.01,   "pip_val": 5.0,   "decimals": 3},
    "NAS100":  {"pip": 1.0,    "pip_val": 1.0,   "decimals": 1},
    "US30":    {"pip": 1.0,    "pip_val": 1.0,   "decimals": 1},
    "UK100":   {"pip": 1.0,    "pip_val": 1.30,  "decimals": 1},
    "Custom":  {"pip": 0.0001, "pip_val": 10.0,  "decimals": 5},
}

# ─── Crypto Data ──────────────────────────────────────────────
CRYPTO_PAIRS = {
    "BTC/USDT":  {"symbol": "BTCUSDT",  "icon": "₿",  "color": "#F7931A", "contract_size": 1.0,   "decimals": 2},
    "ETH/USDT":  {"symbol": "ETHUSDT",  "icon": "Ξ",  "color": "#627EEA", "contract_size": 1.0,   "decimals": 2},
    "BNB/USDT":  {"symbol": "BNBUSDT",  "icon": "B",  "color": "#F3BA2F", "contract_size": 1.0,   "decimals": 2},
    "XRP/USDT":  {"symbol": "XRPUSDT",  "icon": "✕",  "color": "#00AAE4", "contract_size": 1.0,   "decimals": 4},
    "SOL/USDT":  {"symbol": "SOLUSDT",  "icon": "◎",  "color": "#9945FF", "contract_size": 1.0,   "decimals": 2},
    "ADA/USDT":  {"symbol": "ADAUSDT",  "icon": "A",  "color": "#0D1E7A", "contract_size": 1.0,   "decimals": 4},
    "DOGE/USDT": {"symbol": "DOGEUSDT", "icon": "Ð",  "color": "#C3A634", "contract_size": 1.0,   "decimals": 5},
    "AVAX/USDT": {"symbol": "AVAXUSDT", "icon": "A",  "color": "#E84142", "contract_size": 1.0,   "decimals": 2},
    "LINK/USDT": {"symbol": "LINKUSDT", "icon": "⬡",  "color": "#2A5ADA", "contract_size": 1.0,   "decimals": 3},
    "DOT/USDT":  {"symbol": "DOTUSDT",  "icon": "●",  "color": "#E6007A", "contract_size": 1.0,   "decimals": 3},
    "MATIC/USDT":{"symbol": "MATICUSDT","icon": "M",  "color": "#8247E5", "contract_size": 1.0,   "decimals": 4},
    "LTC/USDT":  {"symbol": "LTCUSDT",  "icon": "Ł",  "color": "#BFBBBB", "contract_size": 1.0,   "decimals": 2},
    "UNI/USDT":  {"symbol": "UNIUSDT",  "icon": "U",  "color": "#FF007A", "contract_size": 1.0,   "decimals": 3},
    "ATOM/USDT": {"symbol": "ATOMUSDT", "icon": "⚛",  "color": "#2E3148", "contract_size": 1.0,   "decimals": 3},
    "XLM/USDT":  {"symbol": "XLMUSDT",  "icon": "*",  "color": "#7B7B7B", "contract_size": 1.0,   "decimals": 5},
    "Custom":    {"symbol": "",          "icon": "⚙",  "color": "#8B949E", "contract_size": 1.0,   "decimals": 4},
}

LOT_SIZES = {
    "Standard (1.00)": 1.0,
    "Mini (0.10)":     0.1,
    "Micro (0.01)":    0.01,
    "Nano (0.001)":    0.001,
}

CURRENCIES = {
    "USD": ("$",  1.0),
    "PKR": ("₨", 278.0),
    "EUR": ("€",  0.92),
    "GBP": ("£",  0.79),
}

CRYPTO_AMOUNTS = ["0.001", "0.01", "0.1", "0.5", "1", "2", "5", "10", "Custom"]


# ══════════════════════════════════════════════════════════════
class ForexCalc(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Forex + Crypto Profit Calculator  |  v3.0")
        self.geometry("1100x900")
        self.minsize(920, 760)
        self.configure(fg_color=C["bg"])
        self._live_prices = {}
        self._build_ui()
        self.forex_calculate()
        # Start price fetcher thread
        threading.Thread(target=self._fetch_prices, daemon=True).start()

    # ══ Build UI ═════════════════════════════════════════════
    def _build_ui(self):
        self._header()
        # Tab bar
        self.tab_frame = ctk.CTkFrame(self, fg_color=C["panel"],
                                      corner_radius=0, height=44)
        self.tab_frame.pack(fill="x")
        self.tab_frame.pack_propagate(False)

        self.tab_var = tk.StringVar(value="forex")
        self.btn_forex  = self._tab_btn("FOREX / INDICES / METALS", "forex")
        self.btn_crypto = self._tab_btn("CRYPTO CALCULATOR", "crypto")
        self._switch_tab("forex")

        # Content area
        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.pack(fill="both", expand=True, padx=20, pady=(8, 8))

        self._build_forex_tab()
        self._build_crypto_tab()
        self._footer()
        self._show_tab("forex")

    def _tab_btn(self, text, tag):
        btn = ctk.CTkButton(
            self.tab_frame, text=text, width=200, height=44,
            fg_color="transparent", hover_color=C["card"],
            font=("Courier", 12, "bold"), corner_radius=0,
            command=lambda t=tag: self._switch_tab(t)
        )
        btn.pack(side="left", padx=0)
        return btn

    def _switch_tab(self, tab):
        self.tab_var.set(tab)
        if tab == "forex":
            self.btn_forex.configure( fg_color=C["highlight"], text_color=C["text"])
            self.btn_crypto.configure(fg_color="transparent",  text_color=C["muted"])
        else:
            self.btn_crypto.configure(fg_color=C["purple"],    text_color=C["bg"])
            self.btn_forex.configure( fg_color="transparent",  text_color=C["muted"])
        if hasattr(self, "forex_frame") and hasattr(self, "crypto_frame"):
            self._show_tab(tab)

    def _show_tab(self, tab):
        if tab == "forex":
            self.crypto_frame.pack_forget()
            self.forex_frame.pack(fill="both", expand=True)
        else:
            self.forex_frame.pack_forget()
            self.crypto_frame.pack(fill="both", expand=True)

    # ══ Header ════════════════════════════════════════════════
    def _header(self):
        hdr = ctk.CTkFrame(self, fg_color=C["panel"], corner_radius=0, height=58)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)

        lf = ctk.CTkFrame(hdr, fg_color="transparent")
        lf.pack(side="left", padx=20, pady=8)
        ctk.CTkLabel(lf, text="◈", font=("Courier", 24), text_color=C["accent"]).pack(side="left")
        t = ctk.CTkFrame(lf, fg_color="transparent")
        t.pack(side="left", padx=10)
        ctk.CTkLabel(t, text="PROFIT CALCULATOR PRO",
                     font=("Courier", 14, "bold"), text_color=C["text"]).pack(anchor="w")
        ctk.CTkLabel(t, text="Forex · Indices · Metals · Crypto",
                     font=("Courier", 10), text_color=C["muted"]).pack(anchor="w")

        rf = ctk.CTkFrame(hdr, fg_color="transparent")
        rf.pack(side="right", padx=20)
        for clr, lbl in [(C["green"], "LIVE"), (C["purple"], "CRYPTO"), (C["gold"], "PKR"), (C["accent"], "v3.0")]:
            d = ctk.CTkFrame(rf, fg_color="transparent")
            d.pack(side="left", padx=6)
            ctk.CTkLabel(d, text="●", font=("Arial", 11), text_color=clr).pack(side="left")
            ctk.CTkLabel(d, text=lbl, font=("Courier", 9), text_color=C["muted"]).pack(side="left", padx=2)

    # ══ FOREX TAB ════════════════════════════════════════════
    def _build_forex_tab(self):
        self.forex_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        self.forex_frame.columnconfigure((0, 1), weight=1)
        self.forex_frame.rowconfigure(0, weight=1)
        self._forex_left(self.forex_frame)
        self._forex_right(self.forex_frame)

    def _forex_left(self, parent):
        # Outer frame holds border + section header (non-scrolling)
        outer = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=12,
                             border_width=1, border_color=C["border"])
        outer.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=4)
        outer.columnconfigure(0, weight=1)
        outer.rowconfigure(1, weight=1)

        self._sec(outer, "⚙  TRADE PARAMETERS")

        frame = ctk.CTkScrollableFrame(outer, fg_color="transparent",
                                       scrollbar_button_color=C["border"],
                                       scrollbar_button_hover_color=C["accent"])
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(0, weight=1)
        self._lbl(frame, "Currency Pair / Instrument")
        self.pair_var = ctk.StringVar(value="EUR/USD")
        ctk.CTkOptionMenu(frame, variable=self.pair_var,
                          values=list(FOREX_PAIRS.keys()),
                          command=self._on_pair_change,
                          fg_color=C["card"], button_color=C["highlight"],
                          button_hover_color=C["accent"],
                          dropdown_fg_color=C["card"],
                          font=("Courier", 13)).pack(fill="x", padx=16, pady=(2, 10))

        self._lbl(frame, "Trade Direction")
        df = ctk.CTkFrame(frame, fg_color="transparent")
        df.pack(fill="x", padx=16, pady=(2, 10))
        self.dir_var = tk.StringVar(value="BUY")
        self.btn_buy = ctk.CTkButton(df, text="▲  BUY / LONG", width=140,
                                     fg_color=C["green"], hover_color="#2EA043",
                                     font=("Courier", 13, "bold"),
                                     command=lambda: self._set_dir("BUY"))
        self.btn_buy.pack(side="left", padx=(0, 8))
        self.btn_sell = ctk.CTkButton(df, text="▼  SELL / SHORT", width=140,
                                      fg_color=C["card"], hover_color=C["red"],
                                      font=("Courier", 13, "bold"),
                                      command=lambda: self._set_dir("SELL"))
        self.btn_sell.pack(side="left")

        r2 = ctk.CTkFrame(frame, fg_color="transparent")
        r2.pack(fill="x", padx=16, pady=(0, 6))
        r2.columnconfigure((0, 1), weight=1)
        for col, label, var_name, default in [
            (0, "Entry Price",       "entry_var", "1.08000"),
            (1, "Exit / Target",     "exit_var",  "1.11790"),
        ]:
            f = ctk.CTkFrame(r2, fg_color="transparent")
            f.grid(row=0, column=col, sticky="ew", padx=(0 if col==0 else 6, 6 if col==0 else 0))
            self._lbl(f, label, 0)
            var = ctk.StringVar(value=default)
            setattr(self, var_name, var)
            e = ctk.CTkEntry(f, textvariable=var, font=("Courier", 14),
                             fg_color=C["card"], border_color=C["border"])
            e.pack(fill="x")
            e.bind("<KeyRelease>", lambda ev: self.forex_calculate())

        r3 = ctk.CTkFrame(frame, fg_color="transparent")
        r3.pack(fill="x", padx=16, pady=(4, 6))
        r3.columnconfigure((0, 1), weight=1)
        for col, label, var_name, default, bclr, tclr in [
            (0, "Stop Loss",   "sl_var",  "1.07500", "#5E2020", C["red"]),
            (1, "Take Profit", "tp_var",  "1.12000", "#1B4D2E", C["green"]),
        ]:
            f = ctk.CTkFrame(r3, fg_color="transparent")
            f.grid(row=0, column=col, sticky="ew", padx=(0 if col==0 else 6, 6 if col==0 else 0))
            self._lbl(f, label, 0)
            var = ctk.StringVar(value=default)
            setattr(self, var_name, var)
            e = ctk.CTkEntry(f, textvariable=var, font=("Courier", 13),
                             fg_color=C["card"], border_color=bclr, text_color=tclr)
            e.pack(fill="x")
            e.bind("<KeyRelease>", lambda ev: self.forex_calculate())

        self._lbl(frame, "Lot Size")
        lf2 = ctk.CTkFrame(frame, fg_color="transparent")
        lf2.pack(fill="x", padx=16, pady=(2, 6))
        lf2.columnconfigure((0, 1), weight=1)
        self.lot_preset_var = ctk.StringVar(value="Standard (1.00)")
        ctk.CTkOptionMenu(lf2, variable=self.lot_preset_var,
                          values=list(LOT_SIZES.keys()),
                          command=self._on_lot_change,
                          fg_color=C["card"], button_color=C["highlight"],
                          button_hover_color=C["accent"],
                          dropdown_fg_color=C["card"],
                          font=("Courier", 12), width=180).grid(row=0, column=0, sticky="ew", padx=(0,6))
        self.lot_var = ctk.StringVar(value="1.00")
        le = ctk.CTkEntry(lf2, textvariable=self.lot_var, font=("Courier", 14),
                          fg_color=C["card"], border_color=C["accent"])
        le.grid(row=0, column=1, sticky="ew")
        le.bind("<KeyRelease>", lambda ev: self.forex_calculate())

        self._lbl(frame, "Account Currency")
        self.acc_var = ctk.StringVar(value="USD")
        ctk.CTkOptionMenu(frame, variable=self.acc_var,
                          values=list(CURRENCIES.keys()),
                          command=lambda v: self.forex_calculate(),
                          fg_color=C["card"], button_color=C["highlight"],
                          button_hover_color=C["accent"],
                          dropdown_fg_color=C["card"],
                          font=("Courier", 13)).pack(fill="x", padx=16, pady=(2, 10))

        # Custom fields
        self.custom_frame = ctk.CTkFrame(frame, fg_color=C["card"],
                                         corner_radius=8, border_width=1, border_color=C["gold"])
        self._lbl(self.custom_frame, "Custom Pip Size", 6)
        self.custom_pip_var = ctk.StringVar(value="0.0001")
        ctk.CTkEntry(self.custom_frame, textvariable=self.custom_pip_var,
                     font=("Courier", 12), fg_color=C["panel"]).pack(fill="x", padx=8, pady=(0,4))
        self._lbl(self.custom_frame, "Custom Pip Value ($)", 6)
        self.custom_val_var = ctk.StringVar(value="10.00")
        ctk.CTkEntry(self.custom_frame, textvariable=self.custom_val_var,
                     font=("Courier", 12), fg_color=C["panel"]).pack(fill="x", padx=8, pady=(0,8))

        ctk.CTkButton(frame, text="▶  CALCULATE", height=44,
                      fg_color=C["highlight"], hover_color=C["accent"],
                      font=("Courier", 14, "bold"),
                      command=self.forex_calculate).pack(fill="x", padx=16, pady=(8, 16))
        ctk.CTkLabel(frame, text="", height=20).pack()

    def _forex_right(self, parent):
        frame = ctk.CTkScrollableFrame(parent, fg_color="transparent",
                                       scrollbar_button_color=C["border"],
                                       scrollbar_button_hover_color=C["accent"])
        frame.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=4)
        frame.columnconfigure(0, weight=1)

        res = ctk.CTkFrame(frame, fg_color=C["panel"], corner_radius=12,
                           border_width=1, border_color=C["border"])
        res.pack(fill="x", pady=(0, 8))
        res.columnconfigure((0,1), weight=1)
        self._sec(res, "📊  LIVE RESULTS")
        g = ctk.CTkFrame(res, fg_color="transparent")
        g.pack(fill="x", padx=12, pady=(0,12))
        g.columnconfigure((0,1), weight=1)
        self.lbl_pips   = self._rcard(g, "PIPS MOVED", "—", C["accent"], 0, 0)
        self.lbl_points = self._rcard(g, "POINTS",     "—", C["gold"],   0, 1)
        self.lbl_pct    = self._rcard(g, "MOVE %",     "—", C["muted"],  1, 0)
        self.lbl_pipval = self._rcard(g, "PIP VALUE",  "—", C["muted"],  1, 1)

        pnl = ctk.CTkFrame(res, fg_color=C["card"], corner_radius=10,
                           border_width=1, border_color=C["border"])
        pnl.pack(fill="x", padx=12, pady=(0,8))
        ctk.CTkLabel(pnl, text="TOTAL PROFIT / LOSS",
                     font=("Courier", 10, "bold"), text_color=C["muted"]).pack(pady=(10,2))
        self.lbl_pnl = ctk.CTkLabel(pnl, text="$0.00",
                                    font=("Courier", 28, "bold"), text_color=C["green"])
        self.lbl_pnl.pack()
        self.lbl_pnl_sub = ctk.CTkLabel(pnl, text="—",
                                        font=("Courier", 10), text_color=C["muted"])
        self.lbl_pnl_sub.pack(pady=(0,10))

        rr = ctk.CTkFrame(frame, fg_color=C["panel"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        rr.pack(fill="x", pady=(0,8))
        rr.columnconfigure((0,1,2), weight=1)
        self._sec(rr, "⚖  RISK / REWARD")
        rg = ctk.CTkFrame(rr, fg_color="transparent")
        rg.pack(fill="x", padx=12, pady=(0,12))
        rg.columnconfigure((0,1,2), weight=1)
        self.lbl_sl_pips = self._rcard(rg, "SL PIPS",  "—", C["red"],   0, 0)
        self.lbl_tp_pips = self._rcard(rg, "TP PIPS",  "—", C["green"], 0, 1)
        self.lbl_rr      = self._rcard(rg, "R:R RATIO","—", C["gold"],  0, 2)

        ml = ctk.CTkFrame(frame, fg_color=C["panel"], corner_radius=12,
                          border_width=1, border_color=C["border"])
        ml.pack(fill="both", expand=True)
        self._sec(ml, "📋  MULTI-LOT BREAKDOWN")
        hr = ctk.CTkFrame(ml, fg_color=C["card"], corner_radius=6)
        hr.pack(fill="x", padx=12, pady=(0,4))
        for col in ["Lot Size", "Lots", "Pip Value", "P&L"]:
            ctk.CTkLabel(hr, text=col, font=("Courier", 10, "bold"),
                         text_color=C["accent"]).pack(side="left", expand=True, pady=6)
        self.forex_breakdown = ctk.CTkFrame(ml, fg_color="transparent")
        self.forex_breakdown.pack(fill="x", padx=12, pady=(0,12))
        ctk.CTkLabel(frame, text="", height=20).pack()

    # ══ CRYPTO TAB ═══════════════════════════════════════════
    def _build_crypto_tab(self):
        self.crypto_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        self.crypto_frame.columnconfigure((0, 1), weight=1)
        self.crypto_frame.rowconfigure(0, weight=1)
        self._crypto_left(self.crypto_frame)
        self._crypto_right(self.crypto_frame)

    def _crypto_left(self, parent):
        outer = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=12,
                             border_width=1, border_color=C["purple"])
        outer.grid(row=0, column=0, sticky="nsew", padx=(0,8), pady=4)
        outer.columnconfigure(0, weight=1)
        outer.rowconfigure(1, weight=1)

        self._sec(outer, "₿  CRYPTO PARAMETERS", C["purple"])

        frame = ctk.CTkScrollableFrame(outer, fg_color="transparent",
                                       scrollbar_button_color=C["border"],
                                       scrollbar_button_hover_color=C["purple"])
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(0, weight=1)

        # Coin selector
        self._lbl(frame, "Crypto Pair")
        self.crypto_pair_var = ctk.StringVar(value="BTC/USDT")
        self.crypto_pair_menu = ctk.CTkOptionMenu(
            frame, variable=self.crypto_pair_var,
            values=list(CRYPTO_PAIRS.keys()),
            command=self._on_crypto_pair_change,
            fg_color=C["crypto_card"], button_color="#6B3FA0",
            button_hover_color=C["purple"],
            dropdown_fg_color=C["crypto_card"],
            font=("Courier", 13))
        self.crypto_pair_menu.pack(fill="x", padx=16, pady=(2,10))

        # Live price display
        self.crypto_price_card = ctk.CTkFrame(frame, fg_color=C["crypto_card"],
                                              corner_radius=8, border_width=1,
                                              border_color=C["purple"])
        self.crypto_price_card.pack(fill="x", padx=16, pady=(0,10))
        price_inner = ctk.CTkFrame(self.crypto_price_card, fg_color="transparent")
        price_inner.pack(fill="x", padx=12, pady=8)
        ctk.CTkLabel(price_inner, text="LIVE PRICE",
                     font=("Courier", 9, "bold"), text_color=C["muted"]).pack(side="left")
        self.lbl_live_price = ctk.CTkLabel(price_inner, text="Fetching...",
                                           font=("Courier", 14, "bold"), text_color=C["purple"])
        self.lbl_live_price.pack(side="right")

        # Direction
        self._lbl(frame, "Trade Direction")
        cdf = ctk.CTkFrame(frame, fg_color="transparent")
        cdf.pack(fill="x", padx=16, pady=(2,10))
        self.crypto_dir_var = tk.StringVar(value="BUY")
        self.cbtn_buy = ctk.CTkButton(cdf, text="▲  BUY / LONG", width=140,
                                      fg_color=C["green"], hover_color="#2EA043",
                                      font=("Courier", 13, "bold"),
                                      command=lambda: self._set_crypto_dir("BUY"))
        self.cbtn_buy.pack(side="left", padx=(0,8))
        self.cbtn_sell = ctk.CTkButton(cdf, text="▼  SELL / SHORT", width=140,
                                       fg_color=C["card"], hover_color=C["red"],
                                       font=("Courier", 13, "bold"),
                                       command=lambda: self._set_crypto_dir("SELL"))
        self.cbtn_sell.pack(side="left")

        # Entry / Exit
        cr2 = ctk.CTkFrame(frame, fg_color="transparent")
        cr2.pack(fill="x", padx=16, pady=(0,6))
        cr2.columnconfigure((0,1), weight=1)
        for col, label, var_name, default in [
            (0, "Entry Price ($)", "c_entry_var", ""),
            (1, "Exit Price ($)",  "c_exit_var",  ""),
        ]:
            f = ctk.CTkFrame(cr2, fg_color="transparent")
            f.grid(row=0, column=col, sticky="ew",
                   padx=(0 if col==0 else 6, 6 if col==0 else 0))
            self._lbl(f, label, 0)
            var = ctk.StringVar(value=default)
            setattr(self, var_name, var)
            e = ctk.CTkEntry(f, textvariable=var, font=("Courier", 14),
                             fg_color=C["crypto_card"], border_color=C["purple"],
                             placeholder_text="e.g. 65000")
            e.pack(fill="x")
            e.bind("<KeyRelease>", lambda ev: self.crypto_calculate())

        # SL / TP
        cr3 = ctk.CTkFrame(frame, fg_color="transparent")
        cr3.pack(fill="x", padx=16, pady=(4,6))
        cr3.columnconfigure((0,1), weight=1)
        for col, label, var_name, bclr, tclr, ph in [
            (0, "Stop Loss ($)",   "c_sl_var",  "#5E2020", C["red"],   "e.g. 63000"),
            (1, "Take Profit ($)", "c_tp_var",  "#1B4D2E", C["green"], "e.g. 70000"),
        ]:
            f = ctk.CTkFrame(cr3, fg_color="transparent")
            f.grid(row=0, column=col, sticky="ew",
                   padx=(0 if col==0 else 6, 6 if col==0 else 0))
            self._lbl(f, label, 0)
            var = ctk.StringVar(value="")
            setattr(self, var_name, var)
            e = ctk.CTkEntry(f, textvariable=var, font=("Courier", 13),
                             fg_color=C["crypto_card"], border_color=bclr,
                             text_color=tclr, placeholder_text=ph)
            e.pack(fill="x")
            e.bind("<KeyRelease>", lambda ev: self.crypto_calculate())

        # Amount
        self._lbl(frame, "Coin Amount")
        caf = ctk.CTkFrame(frame, fg_color="transparent")
        caf.pack(fill="x", padx=16, pady=(2,6))
        caf.columnconfigure((0,1), weight=1)
        self.c_amt_preset = ctk.StringVar(value="1")
        ctk.CTkOptionMenu(caf, variable=self.c_amt_preset,
                          values=CRYPTO_AMOUNTS,
                          command=self._on_crypto_amt,
                          fg_color=C["crypto_card"], button_color="#6B3FA0",
                          button_hover_color=C["purple"],
                          dropdown_fg_color=C["crypto_card"],
                          font=("Courier", 12), width=140).grid(row=0, column=0, sticky="ew", padx=(0,6))
        self.c_amt_var = ctk.StringVar(value="1")
        ae = ctk.CTkEntry(caf, textvariable=self.c_amt_var, font=("Courier", 14),
                          fg_color=C["crypto_card"], border_color=C["purple"])
        ae.grid(row=0, column=1, sticky="ew")
        ae.bind("<KeyRelease>", lambda ev: self.crypto_calculate())

        # Leverage
        self._lbl(frame, "Leverage (1x = Spot)")
        self.c_lev_var = ctk.StringVar(value="1")
        lev_frame = ctk.CTkFrame(frame, fg_color="transparent")
        lev_frame.pack(fill="x", padx=16, pady=(2,6))
        lev_frame.columnconfigure(0, weight=1)
        self.lev_slider = ctk.CTkSlider(lev_frame, from_=1, to=100, number_of_steps=99,
                                        command=self._on_lev_slide,
                                        button_color=C["purple"],
                                        button_hover_color=C["accent"],
                                        progress_color=C["purple"])
        self.lev_slider.set(1)
        self.lev_slider.pack(fill="x", pady=(0,4))
        lev_row = ctk.CTkFrame(lev_frame, fg_color="transparent")
        lev_row.pack(fill="x")
        self.lbl_lev = ctk.CTkLabel(lev_row, text="1x",
                                    font=("Courier", 13, "bold"), text_color=C["purple"])
        self.lbl_lev.pack(side="left")
        ctk.CTkLabel(lev_row, text="← drag to set leverage",
                     font=("Courier", 10), text_color=C["muted"]).pack(side="left", padx=8)

        # Account currency
        self._lbl(frame, "Account Currency")
        self.c_acc_var = ctk.StringVar(value="USD")
        ctk.CTkOptionMenu(frame, variable=self.c_acc_var,
                          values=list(CURRENCIES.keys()),
                          command=lambda v: self.crypto_calculate(),
                          fg_color=C["crypto_card"], button_color="#6B3FA0",
                          button_hover_color=C["purple"],
                          dropdown_fg_color=C["crypto_card"],
                          font=("Courier", 13)).pack(fill="x", padx=16, pady=(2,10))

        # Custom coin
        self.c_custom_frame = ctk.CTkFrame(frame, fg_color=C["crypto_card"],
                                           corner_radius=8, border_width=1, border_color=C["gold"])
        self._lbl(self.c_custom_frame, "Coin Name", 6)
        self.c_custom_name = ctk.StringVar(value="MY_COIN")
        ctk.CTkEntry(self.c_custom_frame, textvariable=self.c_custom_name,
                     font=("Courier", 12), fg_color=C["panel"]).pack(fill="x", padx=8, pady=(0,8))

        ctk.CTkButton(frame, text="▶  CALCULATE", height=44,
                      fg_color="#6B3FA0", hover_color=C["purple"],
                      font=("Courier", 14, "bold"),
                      command=self.crypto_calculate).pack(fill="x", padx=16, pady=(8,16))
        ctk.CTkLabel(frame, text="", height=20).pack()

    def _crypto_right(self, parent):
        frame = ctk.CTkScrollableFrame(parent, fg_color="transparent",
                                       scrollbar_button_color=C["border"],
                                       scrollbar_button_hover_color=C["purple"])
        frame.grid(row=0, column=1, sticky="nsew", padx=(8,0), pady=4)
        frame.columnconfigure(0, weight=1)

        # Results
        res = ctk.CTkFrame(frame, fg_color=C["panel"], corner_radius=12,
                           border_width=1, border_color=C["purple"])
        res.pack(fill="x", pady=(0,8))
        res.columnconfigure((0,1), weight=1)
        self._sec(res, "₿  CRYPTO RESULTS", C["purple"])

        cg = ctk.CTkFrame(res, fg_color="transparent")
        cg.pack(fill="x", padx=12, pady=(0,12))
        cg.columnconfigure((0,1), weight=1)
        self.c_lbl_move   = self._rcard(cg, "PRICE MOVE",   "—", C["purple"], 0, 0)
        self.c_lbl_pct    = self._rcard(cg, "MOVE %",       "—", C["gold"],   0, 1)
        self.c_lbl_margin = self._rcard(cg, "MARGIN USED",  "—", C["orange"], 1, 0)
        self.c_lbl_liq    = self._rcard(cg, "LIQ. PRICE",   "—", C["red"],    1, 1)

        cpnl = ctk.CTkFrame(res, fg_color=C["crypto_card"], corner_radius=10,
                            border_width=1, border_color=C["purple"])
        cpnl.pack(fill="x", padx=12, pady=(0,8))
        ctk.CTkLabel(cpnl, text="TOTAL PROFIT / LOSS",
                     font=("Courier", 10, "bold"), text_color=C["muted"]).pack(pady=(10,2))
        self.c_lbl_pnl = ctk.CTkLabel(cpnl, text="$0.00",
                                      font=("Courier", 28, "bold"), text_color=C["green"])
        self.c_lbl_pnl.pack()
        self.c_lbl_pnl_sub = ctk.CTkLabel(cpnl, text="—",
                                          font=("Courier", 10), text_color=C["muted"])
        self.c_lbl_pnl_sub.pack(pady=(0,10))

        # RR
        rr = ctk.CTkFrame(frame, fg_color=C["panel"], corner_radius=12,
                          border_width=1, border_color=C["purple"])
        rr.pack(fill="x", pady=(0,8))
        rr.columnconfigure((0,1,2), weight=1)
        self._sec(rr, "⚖  RISK / REWARD", C["purple"])
        rg = ctk.CTkFrame(rr, fg_color="transparent")
        rg.pack(fill="x", padx=12, pady=(0,12))
        rg.columnconfigure((0,1,2), weight=1)
        self.c_lbl_sl = self._rcard(rg, "SL LOSS",  "—", C["red"],    0, 0)
        self.c_lbl_tp = self._rcard(rg, "TP GAIN",  "—", C["green"],  0, 1)
        self.c_lbl_rr = self._rcard(rg, "R:R RATIO","—", C["gold"],   0, 2)

        # Multi-amount breakdown
        ml = ctk.CTkFrame(frame, fg_color=C["panel"], corner_radius=12,
                          border_width=1, border_color=C["purple"])
        ml.pack(fill="both", expand=True)
        self._sec(ml, "📋  MULTI-AMOUNT BREAKDOWN", C["purple"])
        hr = ctk.CTkFrame(ml, fg_color=C["crypto_card"], corner_radius=6)
        hr.pack(fill="x", padx=12, pady=(0,4))
        for col in ["Amount", "Position $", "P&L", "P&L (PKR)"]:
            ctk.CTkLabel(hr, text=col, font=("Courier", 10, "bold"),
                         text_color=C["purple"]).pack(side="left", expand=True, pady=6)
        self.crypto_breakdown = ctk.CTkFrame(ml, fg_color="transparent")
        self.crypto_breakdown.pack(fill="x", padx=12, pady=(0,12))
        ctk.CTkLabel(frame, text="", height=20).pack()

    # ══ Footer ════════════════════════════════════════════════
    def _footer(self):
        foot = ctk.CTkFrame(self, fg_color=C["panel"], corner_radius=0, height=28)
        foot.pack(fill="x", side="bottom")
        foot.pack_propagate(False)
        ctk.CTkLabel(foot,
                     text="Forex: P&L = Pips × Pip Value × Lots  |  Crypto: P&L = (Exit−Entry) × Amount × Leverage  |  ⚠ For educational use only",
                     font=("Courier", 9), text_color=C["muted"]).pack(pady=5)

    # ══ Helpers ═══════════════════════════════════════════════
    def _sec(self, p, text, color=None):
        color = color or C["accent"]
        r = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=0, height=32)
        r.pack(fill="x", pady=(0,8))
        r.pack_propagate(False)
        ctk.CTkLabel(r, text=text, font=("Courier", 11, "bold"),
                     text_color=color).pack(side="left", padx=14, pady=6)

    def _lbl(self, p, text, pad=10):
        ctk.CTkLabel(p, text=text, font=("Courier", 11),
                     text_color=C["muted"]).pack(anchor="w", padx=16, pady=(pad,2))

    def _rcard(self, p, label, value, color, row, col):
        card = ctk.CTkFrame(p, fg_color=C["card"], corner_radius=8,
                            border_width=1, border_color=C["border"])
        card.grid(row=row, column=col, sticky="ew", padx=4, pady=4, ipady=4)
        ctk.CTkLabel(card, text=label, font=("Courier", 9, "bold"),
                     text_color=C["muted"]).pack(pady=(8,0))
        lbl = ctk.CTkLabel(card, text=value, font=("Courier", 15, "bold"), text_color=color)
        lbl.pack(pady=(2,8))
        return lbl

    # ══ Event Handlers ════════════════════════════════════════
    def _on_pair_change(self, val):
        if val == "Custom":
            self.custom_frame.pack(fill="x", padx=16, pady=(0,8))
        else:
            self.custom_frame.pack_forget()
        self.forex_calculate()

    def _on_lot_change(self, val):
        if val in LOT_SIZES:
            self.lot_var.set(f"{LOT_SIZES[val]:.2f}")
        self.forex_calculate()

    def _set_dir(self, d):
        self.dir_var.set(d)
        self.btn_buy.configure( fg_color=C["green"] if d=="BUY"  else C["card"])
        self.btn_sell.configure(fg_color=C["red"]   if d=="SELL" else C["card"])
        self.forex_calculate()

    def _set_crypto_dir(self, d):
        self.crypto_dir_var.set(d)
        self.cbtn_buy.configure( fg_color=C["green"] if d=="BUY"  else C["card"])
        self.cbtn_sell.configure(fg_color=C["red"]   if d=="SELL" else C["card"])
        self.crypto_calculate()

    def _on_crypto_pair_change(self, val):
        if val == "Custom":
            self.c_custom_frame.pack(fill="x", padx=16, pady=(0,8))
        else:
            self.c_custom_frame.pack_forget()
            price = self._live_prices.get(val, None)
            if price:
                self.c_entry_var.set(f"{price:.2f}")
                self.lbl_live_price.configure(text=f"${price:,.2f}")
        self.crypto_calculate()

    def _on_crypto_amt(self, val):
        if val != "Custom":
            self.c_amt_var.set(val)
        self.crypto_calculate()

    def _on_lev_slide(self, val):
        lev = int(val)
        self.c_lev_var.set(str(lev))
        self.lbl_lev.configure(text=f"{lev}x")
        self.crypto_calculate()

    # ══ Price Fetcher ══════════════════════════════════════════
    def _fetch_prices(self):
        symbols = [v["symbol"] for k, v in CRYPTO_PAIRS.items() if k != "Custom"]
        for sym in symbols:
            try:
                url = f"https://api.binance.com/api/v3/ticker/price?symbol={sym}"
                with urllib.request.urlopen(url, timeout=5) as r:
                    data = json.loads(r.read())
                    pair = next(k for k, v in CRYPTO_PAIRS.items() if v["symbol"] == sym)
                    self._live_prices[pair] = float(data["price"])
                    if pair == self.crypto_pair_var.get():
                        self.after(0, lambda p=float(data["price"]): (
                            self.lbl_live_price.configure(text=f"${p:,.2f}"),
                            self.c_entry_var.set(f"{p:.2f}") if not self.c_entry_var.get() else None
                        ))
            except:
                pass

    # ══ FOREX CALCULATION ═════════════════════════════════════
    def forex_calculate(self, *_):
        try:
            pair_name = self.pair_var.get()
            direction = self.dir_var.get()
            acc_sym, acc_rate = CURRENCIES[self.acc_var.get()]
            entry = float(self.entry_var.get())
            exit_ = float(self.exit_var.get())
            lots  = float(self.lot_var.get())

            if pair_name == "Custom":
                pip_size  = float(self.custom_pip_var.get())
                pip_value = float(self.custom_val_var.get())
            else:
                p = FOREX_PAIRS[pair_name]
                pip_size  = p["pip"]
                pip_value = p["pip_val"]

            raw_move   = exit_ - entry
            signed     = raw_move if direction == "BUY" else -raw_move
            pips       = abs(raw_move) / pip_size
            spips      = signed / pip_size
            points     = pips * 10
            pct        = abs(raw_move) / entry * 100
            pvl        = pip_value * lots
            pnl_usd    = spips * pvl
            pnl_acc    = pnl_usd * acc_rate

            try:
                sl = float(self.sl_var.get())
                sl_pips = abs(entry - sl) / pip_size
            except: sl_pips = 0
            try:
                tp = float(self.tp_var.get())
                tp_pips = abs(tp - entry) / pip_size
            except: tp_pips = 0
            rr = tp_pips / sl_pips if sl_pips > 0 else 0

            self.lbl_pips.configure(  text=f"{pips:,.1f}")
            self.lbl_points.configure(text=f"{points:,.0f}")
            self.lbl_pct.configure(   text=f"{pct:.2f}%")
            self.lbl_pipval.configure(text=f"${pvl:.2f}")

            clr  = C["green"] if pnl_usd >= 0 else C["red"]
            sign = "+" if pnl_acc >= 0 else ""
            self.lbl_pnl.configure(
                text=f"{sign}{acc_sym}{abs(pnl_acc):,.2f}", text_color=clr)
            self.lbl_pnl_sub.configure(
                text=f"{spips:+.1f} pips × ${pvl:.2f}/pip")

            self.lbl_sl_pips.configure(text=f"{sl_pips:.1f}", text_color=C["red"])
            self.lbl_tp_pips.configure(text=f"{tp_pips:.1f}", text_color=C["green"])
            self.lbl_rr.configure(    text=f"1:{rr:.2f}",     text_color=C["gold"])

            for w in self.forex_breakdown.winfo_children(): w.destroy()
            for ll, ls in LOT_SIZES.items():
                pl = spips * pip_value * ls * acc_rate
                c  = C["green"] if pl >= 0 else C["red"]
                s  = "+" if pl >= 0 else ""
                row = ctk.CTkFrame(self.forex_breakdown, fg_color=C["card"],
                                   corner_radius=6, border_width=1, border_color=C["border"])
                row.pack(fill="x", pady=2)
                for txt, a in [
                    (ll.split("(")[0].strip(), "w"),
                    (f"{ls:.3f} lot",           "center"),
                    (f"${pip_value*ls:.2f}",     "center"),
                    (f"{s}{acc_sym}{abs(pl):,.2f}", "e"),
                ]:
                    tc = c if (txt.startswith("+") or (txt.startswith("-") and acc_sym in txt)) else C["text"]
                    ctk.CTkLabel(row, text=txt, font=("Courier", 11),
                                 text_color=tc, anchor=a).pack(side="left", expand=True, padx=8, pady=6)
        except (ValueError, ZeroDivisionError):
            pass

    # ══ CRYPTO CALCULATION ════════════════════════════════════
    def crypto_calculate(self, *_):
        try:
            pair_name = self.crypto_pair_var.get()
            direction = self.crypto_dir_var.get()
            acc_sym, acc_rate = CURRENCIES[self.c_acc_var.get()]
            entry  = float(self.c_entry_var.get())
            exit_  = float(self.c_exit_var.get())
            amount = float(self.c_amt_var.get())
            lev    = max(1, int(float(self.c_lev_var.get())))

            raw_move   = exit_ - entry
            signed     = raw_move if direction == "BUY" else -raw_move
            pct        = abs(raw_move) / entry * 100
            spct       = (signed / entry * 100) * lev

            position_val = entry * amount
            margin_used  = position_val / lev
            pnl_usd      = signed * amount * lev
            pnl_acc      = pnl_usd * acc_rate

            # Liquidation price estimate
            if direction == "BUY":
                liq_price = entry * (1 - 1/lev) if lev > 1 else 0
            else:
                liq_price = entry * (1 + 1/lev) if lev > 1 else 0

            try:
                sl = float(self.c_sl_var.get())
                sl_loss = abs(entry - sl) * amount * lev
                sl_loss_acc = sl_loss * acc_rate
            except: sl_loss = 0; sl_loss_acc = 0
            try:
                tp = float(self.c_tp_var.get())
                tp_gain = abs(tp - entry) * amount * lev
                tp_gain_acc = tp_gain * acc_rate
            except: tp_gain = 0; tp_gain_acc = 0
            rr = tp_gain / sl_loss if sl_loss > 0 else 0

            clr  = C["green"] if pnl_usd >= 0 else C["red"]
            sign = "+" if pnl_acc >= 0 else ""

            self.c_lbl_move.configure(  text=f"${abs(raw_move):,.4g}", text_color=clr)
            self.c_lbl_pct.configure(   text=f"{pct:.2f}%",            text_color=clr)
            self.c_lbl_margin.configure(text=f"${margin_used:,.2f}")
            self.c_lbl_liq.configure(   text=f"${liq_price:,.2f}" if lev > 1 else "N/A (Spot)")

            self.c_lbl_pnl.configure(
                text=f"{sign}{acc_sym}{abs(pnl_acc):,.2f}", text_color=clr)
            self.c_lbl_pnl_sub.configure(
                text=f"{amount} coins × ${abs(signed):,.4g}/coin × {lev}x lev")

            sl_clr = C["red"]   if sl_loss_acc > 0 else C["muted"]
            tp_clr = C["green"] if tp_gain_acc > 0 else C["muted"]
            self.c_lbl_sl.configure(text=f"-{acc_sym}{sl_loss_acc:,.2f}" if sl_loss_acc>0 else "—", text_color=sl_clr)
            self.c_lbl_tp.configure(text=f"+{acc_sym}{tp_gain_acc:,.2f}" if tp_gain_acc>0 else "—", text_color=tp_clr)
            self.c_lbl_rr.configure(text=f"1:{rr:.2f}" if rr>0 else "—", text_color=C["gold"])

            # Multi-amount breakdown
            for w in self.crypto_breakdown.winfo_children(): w.destroy()
            _, pkr_rate = CURRENCIES["PKR"]
            for amt in [0.001, 0.01, 0.1, 0.5, 1.0, 5.0, 10.0]:
                pl_usd  = signed * amt * lev
                pl_acc  = pl_usd * acc_rate
                pl_pkr  = pl_usd * pkr_rate
                pos_val = entry * amt
                c  = C["green"] if pl_usd >= 0 else C["red"]
                s  = "+" if pl_usd >= 0 else ""
                row = ctk.CTkFrame(self.crypto_breakdown, fg_color=C["crypto_card"],
                                   corner_radius=6, border_width=1, border_color=C["border"])
                row.pack(fill="x", pady=2)
                for txt in [
                    f"{amt} coin",
                    f"${pos_val:,.2f}",
                    f"{s}${abs(pl_usd):,.2f}",
                    f"{s}₨{abs(pl_pkr):,.0f}",
                ]:
                    tc = c if txt.startswith("+") or txt.startswith("-") else C["text"]
                    ctk.CTkLabel(row, text=txt, font=("Courier", 11),
                                 text_color=tc).pack(side="left", expand=True, padx=8, pady=5)

        except (ValueError, ZeroDivisionError):
            pass


# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        import customtkinter
    except ImportError:
        print("\n[!] customtkinter not installed.")
        print("Run: pip install customtkinter\n")
        exit(1)

    app = ForexCalc()
    app.mainloop()