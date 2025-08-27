# 💡 Switch Game (Tkinter)

A simple **Python Tkinter-based game** where you toggle switches on and off.  
The goal is to **turn off all the switches** before you run out of chances.  
However, beware ⚡ — after each move, one random switch might turn back on!

---

## 🎮 How to Play
- You start with **6 switches** (all ON by default).
- Click on a switch to toggle it **ON/OFF**.
- After some turns, a random switch may flip automatically.
- You have **12 chances** to turn all switches OFF.
- **Win Condition:** All switches OFF ✅  
- **Lose Condition:** Chances run out ❌

---

## 🧠 How It Works

- The game uses two images: `ON.png` and `OFF.png` to visually indicate the state of each switch.
- The program uses a combination of logic and randomness to create a fun and slightly unpredictable gameplay experience.
- Button states are updated dynamically using the `PhotoImage` and `Button` widgets in Tkinter.

---

## 🛠️ Tech Stack
- **Language:** Python 3  
- **GUI Library:** Tkinter  
- **Modules:** `random`, `tkinter`  

---

## 📂 Project Structure
switch-game/
├── switch_game.py     # Main game logic
├── ON.png             # Switch ON image
├── OFF.png            # Switch OFF image
└── README.md          # Project documentation

---

### Run the Game

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/switch-game.git
   cd switch-game
2. Add your ON.png and OFF.png images to the project directory.
3. Run the game:
   ```bash
   python switch_game.py

---

## ✨ Author

**Adarsh Agrawal** 

---

## 🚧 Future Improvements

- Refactor `click()` function to reduce repetitive code using loops or dictionaries
- Add sound effects and animations for better user experience
- Implement a scoring system or timer for extra challenge
- Add a restart/replay button after win/lose
- Create difficulty levels with different switch counts
- Improve UI layout for better scaling on different screen sizes
- Package game as a standalone executable (`.exe` or `.app`) for easy distribution

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.
