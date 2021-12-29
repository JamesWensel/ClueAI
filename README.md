# ClueAI
AI that can play clue built from scratch in python.
Run best in google colab, but base python files included as well

### clueai.py
Provides functionality for tracking game. Mainly records all suggestions made, and the player (if any) who disproves the suggestion. Performs necessary logic to determine the killer

### roomdecider.py
Decides which room should be moved to next by the player based on current room and known information. 

### suggestioncreator.py
Creates the suggestion that should be made by the player in a given room based on current known information. 
