from concurrent.futures import thread
from glob import glob
from importlib_metadata import Sectioned
from termcolor import colored
from time import process_time, sleep
ascii_art = '''

 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄               ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌             ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          ▐░▌          ▐░▌       ▐░▌             ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          ▐░▌          ▐░▌       ▐░▌                       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌          
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌              ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌             ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀               ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀                                                                                                                 

'''
print(colored(ascii_art,'green'))


from threading import Thread
import os

def loading_animation(process):
    anim = [
    '   ',
    '.  ',
    '.. ',
    '...',
    '.. ',
    '.  ',
    '    ']

    notcomplete = process.is_alive()
    i = 0
    while notcomplete:
        print(colored('[$] Checking Dependencies'+anim[i % len(anim)],'yellow'), end='\r')
        sleep(.1)
        i += 1
        notcomplete = process.is_alive()

def depen_check():
    try:
        import warnings, os
        warnings.filterwarnings('ignore')
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        global object_classifier
        global ingredient_detect
        global barcode_reader
        from utils import object_classifier, ingredient_detect, barcode_reader
        ingredient_detect.load()
        object_classifier.load()
        barcode_reader.load()
        import easyocr
    except Exception as e:
        print(colored('[$] Dependency error: '+ str(e),'red'))
depen_thread = Thread(target=depen_check)
depen_thread.start()

loading_animation(depen_thread)
depen_thread.join()
print('                             ')

# while True:
#     front_img_path = input(colored('[$] Enter the path of Front Image: ','yellow'))
#     if not os.path.isfile(front_img_path):
#         print(colored('[$] File does not exists!','red'))
#         continue
#     break

while True:
    back_img_path = input(colored('[$] Enter the path of Back Image: ','yellow'))
    if not os.path.isfile(back_img_path):
        print(colored('[$] File does not exists!','red'))
        continue
    break

# while True:
#     code_img_path = input(colored('[$] Enter the path of Barcode Image: ','yellow'))
#     if not os.path.isfile(code_img_path):
#         print(colored('[$] File does not exists!','red'))
#         continue
#     break
code_img_path = 'C:/Users/Anshu/Desktop/ECO_SCORE_APP/barcode.jpg'

while True:
    resin_ic = input(colored('[$] Enter the Plastic Resin Code ( Leave blank if not present ): ','yellow'))
    if resin_ic == '':
        resin_ic = 0
    elif int(resin_ic) > 7 or int(resin_ic) < 1:
        print(colored('[$] Code is not Valid!','red'))
        continue
    
    break


print(colored('''[$] Enter Number according to Sector from which the product belongs:

1) Food, beverages, tobacco
2) Furniture and wood products
3) Agriculture, forestry and fishing
4) Chemicals & Pharmaceutical
5) Textile
6) Cosmetics & Toiletries
7) Machinery & equipment
8) Others
''','yellow'))
while True:
    sector = int(input(colored('[$] Choose a number: ','yellow')))
    if sector > 8 or sector < 1:
        print(colored('[$] Choose a valid number!','red'))
        continue
    break


degradable = int(input(colored('''[$] Would you categorize the product as biodegradable/non-biodegradable? :

1) Biodegradable
2) Non - Biodegradable
3) Not sure
[$] Enter an option number from above: ''','yellow')))

# Main

# Object Classification


# object_name = object_classifier.classifier(front_img_path)

# confidence = next(iter(object_name.values()))
# if confidence > 72:
#     pass


# Back Image Scanning

object_ingred = ingredient_detect.detect_ingred(back_img_path)


# barcode reader
barcode_score = barcode_reader.BarcodeReader(code_img_path)

# Calculate the score:

# resin
resin_ic = int(resin_ic)
if resin_ic == 1:
    resin_score = 50
elif resin_ic == 2:
    resin_score = 40
elif resin_ic == 3:
    resin_score = 30
elif resin_ic == 4:
    resin_score =20
elif resin_ic == 5:
    resin_score = 10
elif resin_ic == 6:
    resin_score = 0
elif resin_ic == 7:
    resin_score = 0
else:
    resin_score = (object_ingred[2]*10)+60
    if resin_score > 100:
        resin_score = 100
# -------

# ingredients

chem_score = (15-object_ingred[0])*5
if chem_score < 0:
    chem_score = 0
oil_score = (10-object_ingred[1])*5
if oil_score < 0:
    oil_score = 0

# feedback
if degradable == 1:
    feedback_score = 100
elif degradable == 2:
    feedback_score = 0
else:
    feedback_score = 50

# sector

if sector == 1:
    sector_score = 30
elif sector == 2:
    sector_score = 25
elif sector == 3:
    sector_score = 25
elif sector == 4:
    sector_score = 30
elif sector == 5:
    sector_score = 35
elif sector == 6:
    sector_score = 15
elif sector == 7:
    sector_score = 40
else:
    sector_score = 30


# Total score

Eco_Score = resin_score+int(barcode_score)+chem_score+oil_score+feedback_score+sector_score+100
# print(resin_score)
# print(barcode_score)
# print(chem_score)
# print(oil_score)
# print(feedback_score)
# print(sector_score)
print(colored('[$] Eco - Score: ' + str(Eco_Score),'blue'))