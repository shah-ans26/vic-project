import random
import tkinter
from tkinter import messagebox
from ursina import *

tkinter.messagebox.showinfo(title="Welcome", message="Welcome to the rolling game!")
tkinter.messagebox.showinfo(title="Instructions",message="Each roll you do has a random chance to obtain a random weapon",)

ITEMS = {
    "victor nut sack": 2,
    "andy wants this code": 5,
    "zia pubes": 12,
    "stinky chips": 30,
    "bibi": 75,
    "art folders": 150,
    "turkish megnetic pubes": 250,
    "Exotic": 500,
    "Very Rare": 750,
    "Hyper Legendary": 1000,
    "Tripple T Sahur": 10000,
}

inventory = {} #lwk keep this epmty

def rolldice():
    rolled_item = "Nothing"
 
    for item, rarity in sorted(ITEMS.items(), key=lambda x: x[1], reverse=True):
        if random.randint(1, rarity) == 1:
            rolled_item = item
            break

    if rolled_item != "Nothing":
        msg = f"You rolled: {rolled_item}!\nRarity: 1 in {ITEMS[rolled_item]}"
  
        if rolled_item in inventory:
            inventory[rolled_item] += 1  
        else:
            inventory[rolled_item] = 1  
    else:
        msg = "You rolled: Nothing!"

    messagebox.showinfo(title="You rolled!", message=msg)

def show_inventory():
    if not inventory:
        messagebox.showinfo(title="Inventory", message="Your inventory is empty!")
    else:
        
        inventory_text = "Your Inventory\n"
        for item, count in inventory.items():
            inventory_text += f" {item}: x{count}\n"

        messagebox.showinfo(title="Inventory", message=inventory_text)

root = tkinter.Tk()
root.title("Roll & Quit")
root.geometry("350x250")

roll_button = tkinter.Button(root, text="Roll", command=rolldice, width=10, bg="lightblue")
roll_button.pack(pady=15)

loopr_roll_button = tkinter.Button(root, text="Loop Roll", command=lambda: [rolldice() for _ in range(10)], width=10, bg="lightgreen")
loopr_roll_button.pack(pady=15)

quit_button = tkinter.Button(root, text="Quit", command=root.destroy, width=10, bg="lightcoral")
quit_button.pack(pady=15)

inventory_button = tkinter.Button(root, text="Inventory", command=show_inventory, width=10, bg="lightyellow")
inventory_button.pack(pady=10)

root.mainloop()