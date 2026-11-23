import tkinter as tk
import time

window = tk.Tk()
window.title("Live Frame Output")
window.geometry("500x350")

# Monospaced font ("Menlo" on Mac, "Consolas" on Windows, or "Courier") keeps characters aligned
text_box = tk.Text(window, font=("Menlo", 10), bg="black", fg="white")
text_box.pack(expand=True, fill="both")

counter = 0

def update_text():
    global counter
    counter += 1
    
    # 1. Clear all existing text from line 1, character 0 to the end
    text_box.delete("1.0", tk.END)
    
    # 2. Insert the newly generated text
    new_content = f"Frame: {counter}\nTime: {time.strftime('%H:%M:%S')}\n" + ("#" * (counter % 30))
    text_box.insert(tk.END, new_content)
    
    # 3. Schedule this function to run again in 50 milliseconds (~20 FPS)
    window.after(50, update_text)

# Start the continuous loop
update_text()
window.mainloop()