import io  # importing io module
from googletrans import Translator  # importing translator from googletrans package

try:
    # creating an instance of Translator class
    translator = Translator()
    # opening essay as file
    with io.open('./text.txt', mode='r', encoding="utf-8") as file:
        # converting the words in essay file into list and storing it in lines
        lines = file.readlines()
        for line in lines:
            # translating each line into japanese language
            translation = translator.translate(line, dest='ja')
            with open('./translated.txt', mode='a', encoding="utf-8") as translated_file:
                # creating a new file and appending the translated words to it.
                translated_file.write(translation.text)
except FileNotFoundError:
    print('File not found')
except UnicodeEncodeError as err:
    print('Unicode Encode Error')
