from translate import Translator

# translator= Translator(to_lang="PER")
# translation = translator.translate("This is a pen.")
# print(translation)

tr = Translator(to_lang='ja')
try:
    with open('extra/translated.txt','r') as my_file:
        text = my_file.read()
        trans = tr.translate(text)
        print(trans)
        
except FileNotFoundError as e:
    print('check your shillly file')


