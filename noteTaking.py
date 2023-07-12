import tkinter as tk

class NoteTakingApp:

    def __init__(self, master):
        self.master = master
        master.title("Note Taking App")

        self.label = tk.Label(master, text="Enter your note:")
        self.label.pack()

        self.note_text = tk.Text(master)
        self.note_text.pack()

        self.save_button = tk.Button(master, text="Save Note", command=self.save_note)
        self.save_button.pack()

    def save_note(self):
        note = self.note_text.get("1.0", "end-1c")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        self.note_text.delete("1.0", "end")

root = tk.Tk()
app = NoteTakingApp(root)
root.mainloop()