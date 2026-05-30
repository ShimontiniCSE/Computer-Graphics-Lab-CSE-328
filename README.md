# Object Catch Simulation in Python Turtle Graphics 🎯

---

## 📌 Course Information
- **Course Title**: Computer Graphics Lab  
- **Course Code**: CSE‑328  
- **Prepared For**: Ms. Faria Sultana Bintha Rohman (Lab Technical Officer)  
- **Prepared By**: Sajeda Sultana Syma (ID: 232031053, Batch 31st UG, Term 6th, Semester Spring 6M)  
- **Department**: Computer Science & Engineering, Feni University  
- **Date of Submission**: 30‑05‑2026  

---

## 📖 Theory
The *Object Catching Simulation* is a simple interactive game built using Python’s **Turtle Graphics** library.  
A red circular object appears at random positions on the screen. The player must click on the object before it disappears.  
The game tracks successful catches and missed attempts, ending after **three misses**.

---

## 🎯 Objectives
- Simulate a reflex‑based catching game using mouse input.  
- Demonstrate event handling (`onclick`) and timed events (`ontimer`) in Turtle Graphics.  
- Record player performance through **score** and **miss count**.  

---

## ⚙️ Materials & Tools
- **Programming Language**: Python 3.x  
- **IDE**: Visual Studio Code  
- **Libraries**:  
  - `turtle` (for graphics and drawing)  
  - `random` (for generating random positions)  
- **Functions Used**:  
  - `onclick()` → mouse interaction  
  - `ontimer()` → timed events  
- **Output**:  
  - Turtle Graphics window (interactive interface)  
  - Terminal messages:  
    - `"Caught! Score: X"`  
    - `"Missed! Misses: Y"`  
    - `"Game Over! Final Score: Z"`  

---

## 🧩 Methodology
1. **Environment Setup**: A Turtle screen of size 600×600 pixels is created.  
2. **Game Object**: A red circle (`obj`) is initialized but hidden until each round.  
3. **Game Cycle**:  
   - `show_object()` → places the circle at a random position and makes it visible.  
   - After 1.2 seconds, `next_round()` hides the object if not clicked, counts a miss, and starts the next cycle.  
   - If clicked (`catch()`), the object is hidden immediately and the score increases.  
4. **Termination**: The game ends when the player accumulates **3 misses**.  

---

## 💻 Code Implementation
The full implementation is available in the repository under `Object_Catch.py`.

---

## 📸 Screenshots
### SS‑1: Object Catch Window  
This figure shows the Turtle Graphics window where a **red circular object** appears at random positions. The player must click on this object before it disappears.  
![SS-1](https://github.com/ShimontiniCSE/Computer-Graphics-Lab-CSE-328/blob/main/SS-1.png)

### SS‑2: Terminal Output  
This figure shows the **terminal output** of the game. It records successful catches, missed attempts, and displays the final score once the player misses three times.  
![SS-2](https://github.com/ShimontiniCSE/Computer-Graphics-Lab-CSE-328/blob/main/SS-2.png)

---

## 📝 Sample Output

Caught! Score: 1
Caught! Score: 2
Caught! Score: 3
Caught! Score: 4
Missed! Misses: 1
Caught! Score: 5
Missed! Misses: 2
Caught! Score: 6
Missed! Misses: 3
Game Over! Final Score: 6


---

## ✅ Conclusion
This project demonstrates how **Turtle Graphics** can be used to build interactive reflex‑based games.  
It combines **randomization, event handling, and timed cycles** to create a simple but engaging simulation.  
The program is useful for learning **mouse events, timers, and graphical interaction** in Python.

---
