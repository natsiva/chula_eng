import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
    ("ก", "Gor Gai (กอ ไก่)"),
    ("\u0e02", "Khor Khai (ขอ ไข่)"),
    ("\u0e04", "Khor Khuat (คอ ควาด)"),
    ("\u0e06", "Khor Khon (ฆอ คณ)"),
    ("\u0e07", "Ngor Ngu (งอ งู)"),
    ("\u0e08", "Jor Jan (จอ จัน)"),
    ("\u0e0a", "Chor Chang (ชอ ช้าง)"),
    ("\u0e0d", "Yor Ying (ญอ อิง)")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_card = None
        self.flipped = False
        
        self.label = tk.Label(root, text="Click Next to start", font=("Arial", 40), width=10, height=3)
        self.label.pack(pady=20)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 20))
        self.flip_button.pack()
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 20))
        self.next_button.pack()
        
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0])
        self.flipped = False
    
    def flip_card(self):
        if self.current_card and not self.flipped:
            self.label.config(text=self.current_card[1])
            self.flipped = True
        else:
            self.label.config(text=self.current_card[0])
            self.flipped = False

root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
