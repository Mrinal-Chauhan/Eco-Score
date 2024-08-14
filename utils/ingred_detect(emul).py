import warnings, os
warnings.filterwarnings('ignore')
def load():
    import easyocr
    global reader
    reader = easyocr.Reader(['en'],gpu=False, verbose=False)

def detect_ingred(path):
    global emul_count
    results = reader.readtext(path)
    back_text = []
    chemical_count = 0
    for result in results:
        if result[2] >= 0.6:
            back_text.append(result[1])
    
    affix = ['akyl','phen','tetra','meth','eth','but','sodium','meth','eth','prop','but','penta','hexa','hept','oct','non','deca','yl','ol', 'ate','one','ium','ine','ins','ide']
    oils = ['oil','processed','fats','extracted','cobalt','nickel','chromium','lead','tin','calamine','zinc','iron','extract']
    eco = ['eco friendly','Environmental friendly','green','sustainably sourced','sustainable','recyclable','compostable','energy efficient','natural','energy saving']
    oil_count = 0
    eco_count = 0
    charac = []
    final_charac = []


    for i in back_text:

        # CHECKING EMULSIFIERS
        emulsifiers = ['emulsifier','colour','stabilizer','glazing agent','leavening agent','acidity regulator']
        for emulsifier in emulsifiers:
            if emulsifier in i.lower():  
                emul_counter = False
                emul_code = ''
                for j in i:
                    if j == '(':
                        emul_counter = True
                    elif j == ')':
                        emul_counter = False
                    elif emul_counter:
                        emul_code += j
                emul_count = len(emul_code.split(','))
                
                print(emul_code)
                print(emul_count)
                break

        if ',' in i:
            l1 = i.split(',')
            for j in l1:
                y = j.strip()
                charac.append(y)
        elif ';'in i:
            l1 = i.split(';')
            for j in l1:
                y = j.strip()
                charac.append(y)
        else:
            charac.append(i)

    for i in charac:
        if ';' in i:
            l2 = i.split(';')
            for k in l2:
                z = k.strip()
                final_charac.append(z) 
        elif ',' in i:
            l2 = i.split(',')
            for k in l2:
                z = k.strip()
                final_charac.append(z)
        else:
            final_charac.append(i) 
    
    
    print('BACK TEXT: ',back_text)
    print('\n FINAL CHAR',final_charac)
    for ingredients in final_charac:
        for characters in affix:
            if ingredients.startswith(characters) or ingredients.endswith(characters):
                # print(ingredients)
                chemical_count +=1
                break
    for i in final_charac:
        for x in oils:
            if x in i.lower():
                oil_count += 1
                
    for j in final_charac:
        for y in eco:
            if y in j.lower():
                eco_count+=1

            
    return chemical_count + int(emul_count), oil_count, eco_count

load()
a = detect_ingred(r'C:\Users\Anshu\Desktop\ECO_SCORE_APP\cadbury.jpg')
print(a)
