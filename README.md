# Tom and Jerry Maze Game 🐱🐭

A Python-based maze game featuring Tom and Jerry with multiple pathfinding algorithms, different game modes, and interactive gameplay.
##Screen Shot

![image](https://github.com/user-attachments/assets/0b362801-d743-43bc-92b1-d97499ff540e)


## 🎥 Demo Video

[![Tom and Jerry Maze Game Demo](https://img.youtube.com/vi/ju5hfgw210U/0.jpg)](https://www.youtube.com/watch?v=ju5hfgw210U&t=78s)

Click the image above to watch the game demo on YouTube!

## 🎮 Features

- Multiple maze sizes (20x20, 40x40, 100x100)
- Different game modes:
  - Player Mode: Navigate manually through the maze
  - Bot Mode: Watch AI solve the maze
  - Both Mode: Combine manual control with AI assistance
- Multiple pathfinding algorithms:
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - A* Search
  - Dijkstra's Algorithm
- Interactive gameplay features:
  - User account system with secure login
  - Save/Load game progress
  - Real-time score tracking
  - Time-based challenges
  - Mini-map display
- Animations and sound effects

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Pygame library
- Other required libraries listed in `requirements.txt`

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tom-jerry-maze.git
cd tom-jerry-maze
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python ProjectTest.py
```

## 🎯 How to Play

1. **Login/Register**: Start by creating an account or logging in
2. **Select Game Mode**: Choose between Player, Bot, or Both modes
3. **Choose Maze Size**: Select your preferred maze complexity
4. **Navigate the Maze**: 
   - Use arrow keys for movement
   - Press SPACE for path suggestions
   - Press Q to change pathfinding algorithm
   - Press ESC to pause/menu

## 🎨 Game Controls

- **Arrow Keys**: Move Tom
- **SPACE**: Show suggested path
- **Q**: Switch between algorithms
- **ESC**: Pause game
- **R**: Reset current level
- **M**: Return to main menu

## 🧩 Features in Detail

### Game Modes

1. **Player Mode**
   - Manual navigation through the maze
   - Optional path suggestions
   - Time and step tracking

2. **Bot Mode**
   - Watch AI solve the maze
   - Compare different pathfinding algorithms
   - Learning tool for algorithm visualization

3. **Both Mode**
   - Combine manual control with AI assistance
   - Switch between manual and automatic navigation

### Pathfinding Algorithms

1. **DFS (Depth-First Search)**
   - Explores as far as possible along each branch before backtracking
   - Good for memory usage

2. **BFS (Breadth-First Search)**
   - Explores all neighbor nodes at present depth before moving to nodes at next depth
   - Guarantees shortest path

3. **A* Search**
   - Uses heuristics to find optimal path
   - Combines path cost and estimated distance to goal

4. **Dijkstra's Algorithm**
   - Finds shortest path between nodes in a graph
   - Consider's edge weights

## 💾 Save/Load System

- Save current game progress
- Multiple save slots available
- Auto-save feature
- Load previous games

## 🏆 Scoring System

- Time-based scoring
- Step count tracking
- Level completion bonuses
- High score leaderboard

## 🛠️ Technical Details

The game is built using:
- Python 3.x
- Pygame for graphics and animation
- Object-oriented programming principles
- Custom pathfinding implementations
- SQLite for user data storage

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- My Teamates:
  + Dao Sy Duy Minh 
  + Nguyen Lam Phu Quy
  + Nguyen Tran Trung Kien ( myself )
  + Bang My Linh
- Pygame community for resources and support
- Original Tom and Jerry characters by Hanna-Barbera
- [List any other resources or inspirations]
