import tkinter as tk
from tkinter import ttk, messagebox
from planner import Planner
from flight import Flight

# Dummy flights — you can load from file or elsewhere
sample_flights = [
    # Flight No, Start, Dep Time, End, Arr Time, Fare
    Flight(0, 0, 100, 1, 180, 150),   # Direct route 0 → 1
    Flight(1, 1, 210, 2, 280, 100),   # 1 → 2, valid after flight 0
    Flight(2, 2, 310, 3, 390, 200),   # 2 → 3, valid after flight 1
    Flight(3, 0, 120, 3, 300, 450),   # Direct route 0 → 3 (longer)
    Flight(4, 1, 250, 4, 320, 80),    # 1 → 4
    Flight(5, 4, 350, 3, 430, 90),    # 4 → 3, via flight 4

    # Extra paths from city 0
    Flight(6, 0, 90, 2, 200, 180),    # 0 → 2 (short path)
    Flight(7, 2, 230, 3, 300, 120),   # 2 → 3
    Flight(8, 3, 340, 4, 420, 110),   # 3 → 4
    Flight(9, 0, 70, 4, 160, 300),    # 0 → 4 direct (expensive)

    # Reverse paths
    Flight(10, 4, 200, 1, 270, 75),   # 4 → 1
    Flight(11, 3, 450, 0, 530, 200),  # 3 → 0
    Flight(12, 2, 500, 0, 580, 250),  # 2 → 0

    # Cheaper alternative paths
    Flight(13, 0, 95, 1, 175, 120),   # 0 → 1 (cheaper than flight 0)
    Flight(14, 1, 195, 3, 270, 160),  # 1 → 3 (shortcut)
    Flight(15, 1, 200, 2, 260, 130),  # 1 → 2 (alt to flight 1)
    Flight(16, 2, 280, 4, 360, 95),   # 2 → 4

    # Longer but cheap
    Flight(17, 0, 80, 4, 180, 100),   # 0 → 4 cheap
    Flight(18, 4, 200, 2, 270, 60),   # 4 → 2
    Flight(19, 2, 290, 3, 350, 70),   # 2 → 3
]

planner = Planner(sample_flights)

def run_query():
    try:
        start_city = int(start_city_entry.get())
        end_city = int(end_city_entry.get())
        t1 = int(t1_entry.get())
        t2 = int(t2_entry.get())
        option = goal_var.get()
        
        if option == "Fewest Flights (Earliest)":
            route = planner.least_flights_earliest_route(start_city, end_city, t1, t2)
        elif option == "Cheapest":
            route = planner.cheapest_route(start_city, end_city, t1, t2)
        elif option == "Fewest Flights (Cheapest)":
            route = planner.least_flights_cheapest_route(start_city, end_city, t1, t2)
        else:
            messagebox.showerror("Error", "Invalid optimization goal selected")
            return
        
        # Display results
        output_text.delete(1.0, tk.END)
        if not route:
            output_text.insert(tk.END, "No route found.\n")
        for flight in route:
            output_text.insert(tk.END, f"Flight {flight.flight_no}: City {flight.start_city} -> City {flight.end_city}, Departs {flight.departure_time}, Arrives {flight.arrival_time}, Fare ₹{flight.fare}\n")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid integers for cities and time.")


# GUI setup
root = tk.Tk()
root.title("Flight Planner")

# Input fields
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Start City:").grid(row=0, column=0)
start_city_entry = tk.Entry(frame)
start_city_entry.grid(row=0, column=1)

tk.Label(frame, text="End City:").grid(row=1, column=0)
end_city_entry = tk.Entry(frame)
end_city_entry.grid(row=1, column=1)

tk.Label(frame, text="Start Time (t1):").grid(row=2, column=0)
t1_entry = tk.Entry(frame)
t1_entry.grid(row=2, column=1)

tk.Label(frame, text="End Time (t2):").grid(row=3, column=0)
t2_entry = tk.Entry(frame)
t2_entry.grid(row=3, column=1)

tk.Label(frame, text="Optimization Goal:").grid(row=4, column=0)
goal_var = tk.StringVar(value="Fewest Flights (Earliest)")
goal_menu = ttk.Combobox(frame, textvariable=goal_var, state="readonly")
goal_menu['values'] = ["Fewest Flights (Earliest)", "Cheapest", "Fewest Flights (Cheapest)"]
goal_menu.grid(row=4, column=1)

tk.Button(root, text="Find Route", command=run_query).pack(pady=5)

# Output area
output_text = tk.Text(root, height=15, width=70)
output_text.pack(pady=10)

root.mainloop()
