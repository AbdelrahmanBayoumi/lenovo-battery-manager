#!/usr/bin/env python3
"""
Lenovo Battery Conservation Manager
A lightweight, modern utility to monitor battery status and toggle Lenovo Conservation Mode.
"""

import os
import sys
import glob
import subprocess
import threading
import tkinter as tk

# Colors - Modern Dark Theme
BG_COLOR = "#181825"
CARD_BG = "#1e1e2e"
CARD_BORDER = "#313244"
TEXT_PRIMARY = "#cdd6f4"
TEXT_MUTED = "#a6adc8"
ACCENT_CYAN = "#00e5ff"
ACCENT_GREEN = "#a6e3a1"
ACCENT_YELLOW = "#f9e2af"
ACCENT_RED = "#f38ba8"
TOGGLE_OFF_BG = "#45475a"
TOGGLE_ON_BG = "#00b4d8"

# 64x64 PNG App Icon encoded in base64
APP_ICON_B64 = """
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
"""


def find_conservation_path():
    """Find the sysfs path for conservation mode on Lenovo IdeaPad."""
    candidates = [
        "/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode",
        "/sys/bus/platform/drivers/ideapad_laptop/VPC2004:00/conservation_mode",
        "/sys/devices/platform/VPC2004:00/conservation_mode",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
            
    dynamic = glob.glob("/sys/bus/platform/drivers/ideapad_*/VPC*/conservation_mode")
    if dynamic:
        return dynamic[0]
        
    dynamic_devices = glob.glob("/sys/devices/platform/VPC*/conservation_mode")
    if dynamic_devices:
        return dynamic_devices[0]
        
    return candidates[0]


def find_battery_path():
    """Find the battery sysfs directory (BAT0, BAT1, etc.)."""
    for name in ["BAT0", "BAT1", "BATC"]:
        p = f"/sys/class/power_supply/{name}"
        if os.path.exists(p):
            return p
    batteries = glob.glob("/sys/class/power_supply/BAT*")
    if batteries:
        return batteries[0]
    return "/sys/class/power_supply/BAT0"


CONSERVATION_PATH = find_conservation_path()
BATTERY_PATH = find_battery_path()


class ModernToggle(tk.Canvas):
    """Custom smooth, pill-shaped toggle switch."""

    def __init__(self, parent, width=64, height=34, on_toggle=None, **kwargs):
        super().__init__(
            parent,
            width=width,
            height=height,
            bg=CARD_BG,
            highlightthickness=0,
            cursor="hand2",
            **kwargs
        )
        self.width = width
        self.height = height
        self.on_toggle = on_toggle
        self.is_on = False
        self.bind("<Button-1>", self._handle_click)
        self.draw()

    def set_state(self, is_on, trigger_callback=False):
        self.is_on = is_on
        self.draw()
        if trigger_callback and self.on_toggle:
            self.on_toggle(self.is_on)

    def _handle_click(self, event=None):
        new_state = not self.is_on
        if self.on_toggle:
            self.on_toggle(new_state)

    def draw(self):
        self.delete("all")
        pad = 2
        r = (self.height - 2 * pad) / 2
        bg = TOGGLE_ON_BG if self.is_on else TOGGLE_OFF_BG

        x1, y1 = pad, pad
        x2, y2 = self.width - pad, self.height - pad

        # Pill background
        self.create_arc(x1, y1, x1 + 2 * r, y2, start=90, extent=180, fill=bg, outline=bg)
        self.create_arc(x2 - 2 * r, y1, x2, y2, start=270, extent=180, fill=bg, outline=bg)
        self.create_rectangle(x1 + r, y1, x2 - r, y2, fill=bg, outline=bg)

        # Thumb circle
        thumb_r = r - 2
        cx = (x2 - r) if self.is_on else (x1 + r)
        cy = self.height / 2
        self.create_oval(
            cx - thumb_r, cy - thumb_r, cx + thumb_r, cy + thumb_r,
            fill="#ffffff", outline=""
        )


class BatteryApp(tk.Tk):
    def __init__(self):
        # Set className for X11 / Cinnamon WM_CLASS matching
        super().__init__(className="lenovo-battery-manager")

        self.title("Lenovo Battery Manager")
        self.geometry("440x510")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)

        # Set embedded App Icon for window & task manager
        self._load_icon()

        # Center on screen
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (440 // 2)
        y = (self.winfo_screenheight() // 2) - (510 // 2)
        self.geometry(f"+{x}+{y}")

        self.current_mode = None
        self.is_switching = False

        self._build_ui()
        self.refresh_all_data()

        # Background auto refresh every 5 seconds
        self._schedule_refresh()

    def _load_icon(self):
        try:
            self.app_icon = tk.PhotoImage(data=APP_ICON_B64.strip())
            self.iconphoto(True, self.app_icon)
        except Exception as e:
            print("Could not set app icon:", e)

    def _build_ui(self):
        # Header
        header = tk.Frame(self, bg=BG_COLOR, pady=16)
        header.pack(fill="x", padx=24)

        title_lbl = tk.Label(
            header,
            text="Lenovo Battery Care",
            font=("Ubuntu", 17, "bold"),
            fg=TEXT_PRIMARY,
            bg=BG_COLOR
        )
        title_lbl.pack(anchor="w")

        sub_lbl = tk.Label(
            header,
            text="IdeaPad Power & Conservation Controls",
            font=("Ubuntu", 9),
            fg=TEXT_MUTED,
            bg=BG_COLOR
        )
        sub_lbl.pack(anchor="w")

        # Battery Status Card
        card1 = tk.Frame(self, bg=CARD_BG, highlightbackground=CARD_BORDER, highlightthickness=1)
        card1.pack(fill="x", padx=24, pady=8)

        card1_inner = tk.Frame(card1, bg=CARD_BG, padx=18, pady=16)
        card1_inner.pack(fill="x")

        # Percentage + Status Row
        row1 = tk.Frame(card1_inner, bg=CARD_BG)
        row1.pack(fill="x")

        self.percent_label = tk.Label(
            row1,
            text="-- %",
            font=("Ubuntu", 32, "bold"),
            fg=ACCENT_CYAN,
            bg=CARD_BG
        )
        self.percent_label.pack(side="left")

        self.status_badge = tk.Label(
            row1,
            text="Checking...",
            font=("Ubuntu", 10, "bold"),
            fg=TEXT_PRIMARY,
            bg="#2a2b3d",
            padx=10,
            pady=4
        )
        self.status_badge.pack(side="right")

        # Battery Bar Canvas
        self.battery_bar = tk.Canvas(card1_inner, height=12, bg=CARD_BG, highlightthickness=0)
        self.battery_bar.pack(fill="x", pady=(12, 4))

        self.details_label = tk.Label(
            card1_inner,
            text="Battery health and status",
            font=("Ubuntu", 9),
            fg=TEXT_MUTED,
            bg=CARD_BG
        )
        self.details_label.pack(anchor="w", pady=(4, 0))

        # Conservation Mode Card
        card2 = tk.Frame(self, bg=CARD_BG, highlightbackground=CARD_BORDER, highlightthickness=1)
        card2.pack(fill="x", padx=24, pady=12)

        card2_inner = tk.Frame(card2, bg=CARD_BG, padx=18, pady=18)
        card2_inner.pack(fill="x")

        switch_row = tk.Frame(card2_inner, bg=CARD_BG)
        switch_row.pack(fill="x")

        text_col = tk.Frame(switch_row, bg=CARD_BG)
        text_col.pack(side="left", fill="x", expand=True)

        cm_title = tk.Label(
            text_col,
            text="Conservation Mode",
            font=("Ubuntu", 13, "bold"),
            fg=TEXT_PRIMARY,
            bg=CARD_BG
        )
        cm_title.pack(anchor="w")

        self.cm_status_text = tk.Label(
            text_col,
            text="Loading state...",
            font=("Ubuntu", 10),
            fg=TEXT_MUTED,
            bg=CARD_BG
        )
        self.cm_status_text.pack(anchor="w", pady=(3, 0))

        # Toggle Switch
        self.toggle = ModernToggle(switch_row, on_toggle=self.request_toggle)
        self.toggle.pack(side="right", padx=(10, 0))

        # Separator inside card
        sep = tk.Frame(card2_inner, height=1, bg=CARD_BORDER)
        sep.pack(fill="x", pady=12)

        info_text = (
            "💡 When enabled, charging stops at 55-60% to prolong battery lifespan.\n"
            "Recommended when keeping your laptop plugged in."
        )
        cm_desc = tk.Label(
            card2_inner,
            text=info_text,
            font=("Ubuntu", 8),
            fg=TEXT_MUTED,
            bg=CARD_BG,
            justify="left"
        )
        cm_desc.pack(anchor="w")

        # Bottom Bar: Status Message & Refresh Button
        bottom_bar = tk.Frame(self, bg=BG_COLOR)
        bottom_bar.pack(fill="x", padx=24, pady=(12, 16), side="bottom")

        self.msg_label = tk.Label(
            bottom_bar,
            text="",
            font=("Ubuntu", 9),
            fg=ACCENT_YELLOW,
            bg=BG_COLOR
        )
        self.msg_label.pack(side="left")

        self.refresh_btn = tk.Button(
            bottom_bar,
            text="🔄 Refresh",
            font=("Ubuntu", 9, "bold"),
            fg=TEXT_PRIMARY,
            bg=CARD_BG,
            activebackground=CARD_BORDER,
            activeforeground=TEXT_PRIMARY,
            relief="flat",
            bd=0,
            padx=12,
            pady=6,
            cursor="hand2",
            command=self.manual_refresh
        )
        self.refresh_btn.pack(side="right")

    def _draw_battery_bar(self, percentage, is_charging):
        self.battery_bar.delete("all")
        w = self.battery_bar.winfo_width()
        if w < 10:
            w = 350
        h = 10
        # Background track
        self.battery_bar.create_rectangle(0, 0, w, h, fill="#313244", outline="")
        
        # Color based on percentage & mode
        if percentage <= 15:
            fill_color = ACCENT_RED
        elif self.current_mode == 1:
            fill_color = ACCENT_CYAN
        elif is_charging:
            fill_color = ACCENT_GREEN
        else:
            fill_color = "#89b4fa"

        filled_w = max(0, min(w, int((percentage / 100.0) * w)))
        if filled_w > 0:
            self.battery_bar.create_rectangle(0, 0, filled_w, h, fill=fill_color, outline="")

    def read_battery_info(self):
        cap_file = os.path.join(BATTERY_PATH, "capacity")
        stat_file = os.path.join(BATTERY_PATH, "status")
        
        capacity = 0
        status = "Unknown"
        
        if os.path.exists(cap_file):
            try:
                with open(cap_file, "r") as f:
                    capacity = int(f.read().strip())
            except Exception:
                pass
                
        if os.path.exists(stat_file):
            try:
                with open(stat_file, "r") as f:
                    status = f.read().strip()
            except Exception:
                pass

        return capacity, status

    def read_conservation_mode(self):
        if os.path.exists(CONSERVATION_PATH):
            try:
                with open(CONSERVATION_PATH, "r") as f:
                    val = f.read().strip()
                    return int(val)
            except Exception:
                return None
        return None

    def manual_refresh(self):
        self.refresh_all_data()
        self.msg_label.config(text="✓ Refreshed", fg=ACCENT_GREEN)
        self.after(1500, lambda: self.msg_label.config(text=""))

    def refresh_all_data(self):
        # Battery Data
        cap, status = self.read_battery_info()
        self.percent_label.config(text=f"{cap}%")
        
        is_charging = status.lower() == "charging"
        
        # Update Status Badge
        if status.lower() == "charging":
            self.status_badge.config(text="⚡ Charging", fg=ACCENT_GREEN, bg="#1a3328")
        elif status.lower() == "discharging":
            self.status_badge.config(text="🔋 On Battery", fg="#89b4fa", bg="#1e2d42")
        elif status.lower() == "full":
            self.status_badge.config(text="✓ Full", fg=ACCENT_GREEN, bg="#1a3328")
        elif status.lower() == "not charging":
            self.status_badge.config(text="🔌 Plugged In (Holding)", fg=ACCENT_CYAN, bg="#143142")
        else:
            self.status_badge.config(text=f"🔌 {status}", fg=TEXT_PRIMARY, bg="#2a2b3d")

        # Conservation Mode
        mode = self.read_conservation_mode()
        self.current_mode = mode
        
        if mode is None:
            self.cm_status_text.config(text="⚠️ Device node not detected", fg=ACCENT_RED)
            self.details_label.config(text=f"Node path: {CONSERVATION_PATH}")
        elif mode == 1:
            self.toggle.set_state(True)
            self.cm_status_text.config(text="Enabled (Stops charging at ~60%)", fg=ACCENT_CYAN)
            self.details_label.config(text="Conservation active: Battery health is protected.")
        else:
            self.toggle.set_state(False)
            self.cm_status_text.config(text="Disabled (Standard 100% charging)", fg=TEXT_MUTED)
            self.details_label.config(text="Standard mode: Charges normally to 100%.")

        self._draw_battery_bar(cap, is_charging)

    def _schedule_refresh(self):
        if not self.is_switching:
            self.refresh_all_data()
        self.after(5000, self._schedule_refresh)

    def request_toggle(self, new_state):
        if self.is_switching:
            return
        
        target_val = 1 if new_state else 0
        self.is_switching = True
        self.msg_label.config(text="Prompting for authorization...", fg=ACCENT_YELLOW)

        thread = threading.Thread(target=self._apply_toggle, args=(target_val,))
        thread.daemon = True
        thread.start()

    def _apply_toggle(self, target_val):
        cmd = ["pkexec", "sh", "-c", f"echo {target_val} > '{CONSERVATION_PATH}'"]
        proc = subprocess.run(cmd, capture_output=True, text=True)

        self.after(0, self._on_toggle_finished, proc.returncode, target_val)

    def _on_toggle_finished(self, returncode, target_val):
        self.is_switching = False
        if returncode == 0:
            # Enforce multi-stage auto-refresh to give EC hardware time to transition
            self.msg_label.config(text="✓ Updated! Syncing status...", fg=ACCENT_CYAN)
            self.refresh_all_data()

            # Hardware takes 0.5s - 2s to reflect charging status in sysfs
            self.after(600, self.refresh_all_data)
            self.after(1500, self.refresh_all_data)
            self.after(3000, self._finish_sync)
        elif returncode == 126 or returncode == 127:
            # User dismissed or auth failed
            self.msg_label.config(text="Authentication cancelled", fg=ACCENT_YELLOW)
            self.refresh_all_data()
            self.after(2500, lambda: self.msg_label.config(text=""))
        else:
            self.msg_label.config(text="Failed to update mode", fg=ACCENT_RED)
            self.refresh_all_data()

    def _finish_sync(self):
        self.refresh_all_data()
        self.msg_label.config(text="✓ Synced", fg=ACCENT_GREEN)
        self.after(2000, lambda: self.msg_label.config(text=""))


if __name__ == "__main__":
    app = BatteryApp()
    app.mainloop()
