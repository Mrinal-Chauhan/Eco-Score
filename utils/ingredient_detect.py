import warnings, os
warnings.filterwarnings('ignore')
def load():
    import easyocr
    global reader
    reader = easyocr.Reader(['en'],gpu=False, verbose=False)
def detect_ingred(path):
    results = reader.readtext(path)
    back_text = []
    chemical_count = 0
    for result in results:
        if result[2] >= 0.65:
            back_text.append(result[1])
    affix = ['akyl','phen','tetra','meth','eth','but','sodium','meth','eth','prop','but','penta','hexa','hept','oct','non','deca','yl','ol', 'ate','one','ium','ine','ins']
    oils = ['oil','processed','fats','extracted','cobalt','nickel','chromium','lead','tin','calamine','zinc','iron']
    eco = ['eco friendly','Environmental friendly','green','sustainably sourced','sustainable','recyclable','compostable','energy efficient','natural','energy saving']
    oil_count = 0
    eco_count = 0
    charac = []
    for i in back_text:
        if ',' in i:
            charac+= i.split(',')
        else:
            charac.append(i)

    for ingredients in charac:
        for characters in affix:
            if ingredients.startswith(characters) or ingredients.endswith(characters):
                chemical_count +=1
                break
    for i in charac:
        for x in oils:
            if x in i:
                oil_count += 1
                break
    for j in charac:
        for y in eco:
            if y in j:
                eco_count+=1
                break
    return chemical_count, oil_count, eco_count