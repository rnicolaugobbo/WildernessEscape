class TreeNode:
    def __init__(self, story_piece: str) -> None:
        self.story_piece = story_piece
        self.choices = []
    
    def add_child(self, node: str) -> None:
        self.choices.append(node)

user_choice = input("What's your name?\n")
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

choice_a = TreeNode(
"""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode(
"""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

# print(story_root.story_piece)