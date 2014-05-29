from tkinter import *

# On crée une fenêtre, racine de notre interface
root = Tk()

root.wm_title("Cypher v0.1")

frame_root = Frame(root, width=700,height=400,borderwidth=3)
frame_root.pack()
# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre
# interface racine
champ_label = Label(root, text="Bienvenue dans Cypher")
# On affiche le label dans la fenêtre
champ_label.pack()

#bouton quitter
bouton_quit = Button(root, text="Quitter",command=root.quit)
bouton_quit.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
root.mainloop()
