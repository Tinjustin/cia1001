# The Magical Crystal of Destiny

A colorful, interactive text-based adventure game where you explore a mysterious cave in search of a magical crystal. Make choices that affect your journey, collect items, and discover different endings!

## 🎮 Features

- **Rich Text Display**
  - Colorful text output using Colorama
  - Smooth text animation effects
  - ASCII art title screen
  - Clear visual feedback for choices and outcomes

- **Game Mechanics**
  - Health system (starts at 100)
  - Inventory system for collecting items
  - Multiple story paths and endings
  - Interactive choice system
  - Safe game termination with Ctrl+C

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone this repository or download the files
2. Install the required package by running:
```bash
pip install -r requirements.txt
```

### Running the Game

Run the game using:
```bash
python hello_world.py
```

## 🎯 How to Play

1. Read the story text carefully as it appears
2. When presented with choices, enter the number corresponding to your desired action
3. Keep track of your health and inventory
4. Make strategic decisions that affect your journey
5. Try different choices to discover all possible endings!

## 🗺️ Story Paths

The game features multiple paths and outcomes:

### Cave Entrance (First Choice)
- **Enter cautiously**
  - Gain a torch
  - Safe entry into the cave
- **Search for supplies**
  - Find healing potion and rope
  - Better prepared for challenges
- **Call out**
  - Take 10 damage
  - Risky but direct approach

### Crystal Chamber (Second Choice)
- **Take the crystal**
  - Obtain the magical artifact
  - Trigger cave tremors
- **Examine closely**
  - Discover ancient warnings
  - Avoid the curse
- **Leave it alone**
  - Peaceful resolution
  - Safe but unrewarding

## 🎨 Visual Elements

### Color Scheme
- **Cyan** (Fore.CYAN)
  - Title screen
  - Welcome messages
  - Final messages
- **Yellow** (Fore.YELLOW)
  - Menu options
  - Health and inventory display
- **Green** (Fore.GREEN)
  - Input prompts
  - Success messages
- **Red** (Fore.RED)
  - Error messages
  - Damage notifications
- **Blue** (Fore.BLUE)
  - Story progression
  - Discovery messages
- **White** (Fore.WHITE)
  - Main narrative text

### ASCII Art
```
╔═══════════════════════════════════════╗
║  THE MAGICAL CRYSTAL OF DESTINY       ║
╚═══════════════════════════════════════╝
```

## 🛠️ Technical Details

### Code Structure
- `print_slow(text, delay=0.03)`: Creates typewriter effect
- `display_title()`: Renders ASCII title art
- `make_choice(options)`: Handles user input
- `game()`: Main game loop and story logic

### Error Handling
- Input validation for menu choices
- Exception handling for KeyboardInterrupt
- Type checking for user inputs

## 📦 Dependencies

The game uses:
- `colorama==0.4.6`
  - Provides cross-platform colored terminal text
  - Used for all text coloring and styling

## ⌨️ Controls

- Use number keys (1-3) to select choices
- Press Enter to confirm selections
- Ctrl+C to safely exit the game

## 💡 Tips

1. Pay attention to your health - starting with 100
2. Collect items when possible - they might be useful
3. Read the story carefully for hints
4. Try different paths to see all endings
5. Use Ctrl+C if you need to exit quickly

## 🐛 Troubleshooting

If you encounter issues:

1. **Colors not showing**
   - Verify colorama is installed
   - Check terminal supports ANSI colors

2. **Text printing too fast/slow**
   - Adjust delay in print_slow function

3. **Input not registering**
   - Ensure you're entering numbers only
   - Check keyboard input mode