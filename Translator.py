# translate library to translate text from one language to another

# importing Translatoe
from translate import Translator

# text to be translated
print("enter a text to be converted")
txt = input()

print("enter language of input entered")
inpLang = input()

print("enter language for output")
outLang = input()


# to translate [takes 2 args which are languages]
translate = Translator(from_lang=inpLang, to_lang=outLang)

# calling function
translation = translate.translate(txt)

print(translation)
