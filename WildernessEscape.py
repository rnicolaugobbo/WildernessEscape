class TreeNode:
    def __init__(self, story_piece: str) -> None:
        self.story_piece = story_piece
        self.choices = []


print("Once upon a time...")

story_root = TreeNode(
"""
You are in a forest clearing. 
There is a path to the left. 
A bear emerges from the trees and roars! 
Do you:  
1 ) Roar back! 
2 ) Run to the left...
""")