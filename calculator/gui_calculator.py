# -*- coding: utf-8 -*-

# Mini GUI Calculator - Tkinter (Beginner-friendly)
# Python 3.x

import tkinter as tk
from tkinter import messagebox
import math
import re

ALLOWED_PATTERN = re.compile(r"^[0-9\.\+\-\*\/\(\)\s\*]+$")

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("💜 Mor Tuşlu Hesap Makinesi")
        self.resizable(False, False)
        self.configure(bg="#ffb6c1")  # pencere arka planı (açık pembe)

        self.expr_var = tk.StringVar(value="")
        self._build_ui()

    def _build_ui(self):
        # Ekran
        entry = tk.Entry(
            self, textvariable=self.expr_var, font=("Segoe UI", 18),
            justify="right", width=20, bd=5,
            bg="#ffe4ec", fg="#4a0e2e"
        )
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        entry.focus_set()

        # Mor tuş renkleri
        button_bg = "#9370db"       # orta mor
        button_fg = "white"         # yazılar beyaz
        active_bg = "#b19cd9"       # açık mor (aktifken)

        # Butonlar
        buttons = [
            ("C",   1, 0), ("⌫", 1, 1), ("(",  1, 2), (")", 1, 3),
            ("7",   2, 0), ("8", 2, 1), ("9", 2, 2), ("/",  2, 3),
            ("4",   3, 0), ("5", 3, 1), ("6", 3, 2), ("*",  3, 3),
            ("1",   4, 0), ("2", 4, 1), ("3", 4, 2), ("-",  4, 3),
            ("0",   5, 0), (".", 5, 1), ("=", 5, 2), ("+",  5, 3),
        ]

        for (text, r, c) in buttons:
            cmd = (lambda t=text: self.on_button(t))
            tk.Button(
                self, text=text, width=5, height=2, command=cmd,
                font=("Segoe UI", 12, "bold"),
                bg=button_bg, fg=button_fg, activebackground=active_bg
            ).grid(row=r, column=c, padx=5, pady=5)

        # Ekstra butonlar: karekök ve kare
        tk.Button(self, text="√", width=5, height=2, command=self.sqrt_current,
                  font=("Segoe UI", 12, "bold"),
                  bg=button_bg, fg=button_fg, activebackground=active_bg).grid(row=6, column=0, padx=5, pady=8)

        tk.Button(self, text="x²", width=5, height=2, command=self.square_current,
                  font=("Segoe UI", 12, "bold"),
                  bg=button_bg, fg=button_fg, activebackground=active_bg).grid(row=6, column=1, padx=5, pady=8)

        # Alt bilgi
        info = tk.Label(self, text="= hesapla | C temizle | ⌫ sil",
                        fg="#4a0e2e", bg="#ffb6c1", font=("Segoe UI", 10))
        info.grid(row=7, column=0, columnspan=4, pady=(0,10))

        # Kısayollar
        self.bind("<Return>", lambda e: self.evaluate())
        self.bind("<KP_Enter>", lambda e: self.evaluate())
        self.bind("<Escape>", lambda e: self.clear())
        self.bind("<BackSpace>", lambda e: self.backspace())

    # --- Fonksiyonlar ---
    def on_button(self, t: str):
        if t == "C":
            self.clear()
        elif t == "⌫":
            self.backspace()
        elif t == "=":
            self.evaluate()
        else:
            self.insert_text(t)

    def insert_text(self, t: str):
        self.expr_var.set(self.expr_var.get() + t)

    def clear(self):
        self.expr_var.set("")

    def backspace(self):
        self.expr_var.set(self.expr_var.get()[:-1])

    def sqrt_current(self):
        try:
            value = self._safe_eval(self.expr_var.get())
            if value < 0:
                raise ValueError("Negatif sayının karekökü yok.")
            self.expr_var.set(self._fmt(math.sqrt(value)))
        except Exception as e:
            messagebox.showerror("Hata", str(e))

    def square_current(self):
        try:
            value = self._safe_eval(self.expr_var.get())
            self.expr_var.set(self._fmt(value ** 2))
        except Exception as e:
            messagebox.showerror("Hata", str(e))

    def evaluate(self):
        try:
            result = self._safe_eval(self.expr_var.get())
            self.expr_var.set(self._fmt(result))
        except ZeroDivisionError:
            messagebox.showerror("Hata", "0'a bölme tanımsızdır.")
        except Exception as e:
            messagebox.showerror("Hata", str(e))

    # Yardımcılar
    def _safe_eval(self, expr: str):
        expr = expr.strip()
        if not expr:
            return 0
        if not ALLOWED_PATTERN.match(expr):
            raise ValueError("Geçersiz karakter var.")
        return eval(expr, {"__builtins__": None}, {})

    def _fmt(self, x):
        return str(int(x)) if isinstance(x, (int, float)) and x == int(x) else str(x)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

