# installed langdetect

# Importing langdetect library
import customtkinter as ctk
from langdetect import detect


# Dictionary of some famous Languages and their respective codes
codes={
 'ar': 'Arabic', 'et': 'Armenian', 'art': 'Artificial Langauge',
 'sq': 'Albanian','bn': 'Bangla', 'bh': 'Bhojpuri',
'bul': 'Bulgarian', 'cai': 'Central American Indian Language',
 'cze': 'Caech', 'dan': 'Danish', 'ger': 'German', 'eg': 'Egyptian', 'en': 'English',
 'fre': 'french', 'gon': 'Gondi', 'grc': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
 'ind': 'Indonesian', 'ita': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
 'kas': 'Kashmiri', 'geo': 'Georgian', 'kor': 'Korean', 'lat': 'Latin',
 'mar': 'Marathi', 'mni': 'Manipuri', 'mul': 'Multiple Languages', 'dut': 'Dutch',
'te': 'Telugu', 'ta': 'Tamil','cy':'Welsh'}


root = ctk.CTk()
root.geometry("350x300")
root.resizable(False,False)
root.title("language detection")


# label for operatng system
label = ctk.CTkLabel(root,
                    text="Language Detection",
                    font=("Roboto",17,"bold"))
label.grid(row=0,column=0, columnspan=2,padx=10, pady=20)


# entry feild
entry = ctk.CTkEntry(root,
                     height=30,
                     width=200,
                    placeholder_text="enter text to detect")
entry.grid(row=1,column=0,columnspan=2,padx=(20,10), pady=(20,20),sticky="ew")


# Function to detect the language of a sentence
def detect_language(text):
    return detect(text)


# output func
def outFunc():
    # getting text from entry
    text = entry.get()
    # calling func to detect
    finalAns = codes[detect_language(text)]
    # adding ans to output label
    label1.configure(text= "output: "+finalAns)


# submit btn
submitBtn = ctk.CTkButton(root,
                          text="submit",
                          command=outFunc)
submitBtn.grid(row=2,column=0,padx=15, pady=(10))


# clear func
def clear():
    # clears entry
    entry.delete(0,"end")


# clear btn
clearBtn = ctk.CTkButton(root,
                          text="Clear",
                          command=clear)
clearBtn.grid(row=2,column=1,padx=20, pady=(10))

# output frame
output = ctk.CTkFrame(root,
                      height=60,
                      fg_color="grey10")
output.grid(row=3, column=0, columnspan=2, padx=(20,20), pady=(10,10), sticky="snew")


# label for output
label1 = ctk.CTkLabel(output,
                    text="output: ",
                    font=("Roboto",17,"bold"))
label1.grid(row=0,column=0, columnspan=2,padx=10, pady=10)



root.mainloop()

