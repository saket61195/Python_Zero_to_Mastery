from translate import Translator  # without internet it will not work

# translator= Translator(to_lang="PER")
# translation = translator.translate("This is a pen.")
# print(translation)

tr = Translator(to_lang='ja')
try:
    with open('/home/saket/learning/python_programming/myowncode/P11_file_io/extra/translated.txt', 'r') as my_file:
        # with open('extra/translated.txt', 'r') as my_file:
        text = my_file.read()
        trans = tr.translate(text)
        print(trans)
        with open('/home/saket/learning/python_programming/myowncode/P11_file_io/extra/translted_la.txt', 'w') as my_file2:
            # with open('extra/translted_la.txt', 'w') as my_file2:
            my_file2.write(trans)
except FileNotFoundError as e:
    print('check your shillly file')
