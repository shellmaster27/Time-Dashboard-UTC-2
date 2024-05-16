import tkinter as tk
import datetime

# Create a new window
window = tk.Tk()
window.geometry("200x100")
window.title("Ziit")
window.colormapwindows()
window.configure(bg='black')

# Create a label to display the time
time_label = tk.Label(window, font=("Arial", 24), pady=20, bg='black', fg='white')
time_label.pack()


# Function to update the time
def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)  # Update every second

# Call the update_time function to start updating the time
update_time()

# Run the main event loop
window.mainloop()
