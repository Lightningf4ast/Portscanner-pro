import tkinter as tk
from tkinter import ttk, messagebox
import asyncio
import threading

from core.scanner_async import scan_range
from core.service import get_service
from core.exporter import save_txt, save_json

results = []

def start_scan():
    ip = entry_ip.get()
    start = entry_start.get()
    end = entry_end.get()

    if not ip or not start or not end:
        messagebox.showerror("Error", "Fill all fields")
        return

    try:
        start = int(start)
        end = int(end)
    except:
        messagebox.showerror("Error", "Invalid ports")
        return

    output.delete("1.0", tk.END)
    progress["value"] = 0
    results.clear()

    def run():
        ports = asyncio.run(scan_range(ip, start, end, 0.5))

        total = len(ports) if ports else 1

        for i, p in enumerate(ports):
            service = get_service(p)
            line = f"[OPEN] {p} ({service})"

            results.append({"port": p, "service": service})

            output.insert(tk.END, line + "\n")
            progress["value"] = (i + 1) / total * 100

        output.insert(tk.END, "\nScan Complete\n")

    threading.Thread(target=run).start()


def save():
    if not results:
        messagebox.showinfo("Info", "No results to save")
        return

    save_txt(results)
    save_json(results)
    messagebox.showinfo("Saved", "Results saved")


# ---- UI ----
root = tk.Tk()
root.title("🔥 Pro Port Scanner")
root.geometry("700x500")
root.configure(bg="#0f172a")

frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=10)

def label(text, row):
    tk.Label(frame, text=text, fg="white", bg="#0f172a").grid(row=row, column=0)

def entry(row):
    e = tk.Entry(frame)
    e.grid(row=row, column=1)
    return e

label("Target IP", 0)
entry_ip = entry(0)

label("Start Port", 1)
entry_start = entry(1)

label("End Port", 2)
entry_end = entry(2)

tk.Button(root, text="Start Scan", command=start_scan).pack(pady=5)
tk.Button(root, text="Save Results", command=save).pack(pady=5)

progress = ttk.Progressbar(root, length=400)
progress.pack(pady=10)

output = tk.Text(root, bg="black", fg="lime")
output.pack(expand=True, fill="both")

root.mainloop()
