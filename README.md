# Path Visualization
## Built with:
- Python Language
- pygame: For visuals
- queue: Used for part of Search Algorithim

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