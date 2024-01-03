# Path Visualization
Currently utilizes Breadth First Search In order to find *End Node*(cell) *from Start Node*
## Built with:
- Python Language
- pygame: For visuals
- queue: Used for part of Search Algorithim

## How to use
Make sure to have pygame installed in your system before running PathVisualization.py
Just run, PathVisualization.py
1. A Grid will appear that you can change
    - Mouse1 to draw walls.
    - Mouse2 to delete walls.
2. Press '''Space''', to being search.
3. Watch as it starts from the green square to find the end, creates a yellow line showing the optimal path.

## What I Learned:
- Creating graphics on the screen, and figuring out how to calculate the positions of where I wanted to create graphics.
- Pygame, very convenient, especially compared to Java's graphic apis.
- Learning different algorithim designs, and apply what I learned in class into my own project.
- Realized I could just update the screen when I changed something instead of 60 times a second.
## Troubles:
- Converting Grid into Display, and the Display back into Grid
- Figuring out on converting pygame coordinates into grid coordinates.
- Figuring out how python dealt with objects, as it was different from Java and C++.
- Had issues on figuring out on how to render the program, for when searching algorithim
- Had to scrap initial idea on using search algorithim using a recursive solution
    - Wrong approach as program loses control, and will search the whole grid instead of stopping when finding end

## Considerations
- Updating only the cells on the grid that changed for future operations
- Honestly could have made it all in the class, but I like it in different classes as it's cleaner, and helps abstract the code while allowing PathVisualization.py to be clean

## Author's Comment:
- Created this after seeing some youtube videos, and was able to learn about the different kind of searches in class, decided to create this because it's cool and quite fascinating.
- Like an algorithim, but visualized which is kind of satisfying, hoping to implement more advance algorithims that take account for if we know where the "end node" is and the "start node".
