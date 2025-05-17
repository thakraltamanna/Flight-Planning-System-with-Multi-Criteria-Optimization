# Flight-Planning-System-with-Multi-Criteria-Optimization
## By: Tamanna Thakral

This project is a simulation of a flight planning system that finds optimal flight routes between cities based on multiple objectives:
- Fewest number of flights with earliest arrival
- Cheapest cost
- Fewest flights with cheapest cost

The system processes a set of flights (departure city, arrival city, timings, cost) and efficiently determines the best route based on user requirements.

---

## Features

- Supports route finding between any two cities with time window constraints
- Optimizes based on:
  - **Fewest Flights + Earliest Arrival**
  - **Minimum Total Cost**
  - **Fewest Flights + Minimum Cost**
- Handles real-world constraints like minimum layover time
- Returns a complete itinerary with ordered flight details

---

## Technologies Used

- **Python 3**
- **Graph Algorithms** (BFS/Dijkstra variations)
- **Custom Flight & Planner Classes**

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/optiroute-planner.git
cd optiroute-planner
