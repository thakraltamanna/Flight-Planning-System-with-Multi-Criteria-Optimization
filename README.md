# Flight Planner 
## By: Tamanna Thakral

This project is a flight planning tool built using Python. It provides an interactive GUI built with Tkinter, allowing users to find optimal flight routes between cities based on different optimization goals.

## Features

- Find a route with the **fewest number of flights** (and earliest arrival among such routes)
- Find the **cheapest route** regardless of number of flights
- Find a route with the **fewest flights** (and cheapest among such routes)
- Visual interface for selecting start and end cities, time constraints, and optimization goal
- Displays flight-by-flight breakdown of the selected route

## File Structure
.  
├── flight.py # Flight class definition  
├── planner.py # MinHeap and Planner class with core logic  
├── gui.py # Tkinter-based GUI to run the planner  
├── sample_data.py # (Optional) Sample data generator for flights  
├── README.md # Project documentation  


## Getting Started

### Requirements

- Python 3.x
- Tkinter (usually pre-installed with Python)

### How to Run

1. Clone or download the project files.
2. Ensure all `.py` files (`flight.py`, `planner.py`, `gui.py`) are in the same directory.
3. Run the GUI:

```bash
python gui.py
