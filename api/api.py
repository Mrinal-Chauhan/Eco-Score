from flask import Flask, request
import base64
import utils.ingred_detect_emul as ingred
import ecoscore as eco
import utils.barcode_reader as bar

app = Flask(__name__)

@app.route('/get-eco-score', methods=['GET','POST'])
def get_data():
      
    data = request.get_json()
    biod = data['bdg']
    sector = data['sec']
    resin = data['resin']
    front_img = data['front']
    back_img = data['back']
    bar_img = data['barcode']
    front_data = base64.b64decode(front_img)
    back_data = base64.b64decode(back_img)
    bar_data = base64.b64decode(bar_img)

    with open('front.jpg','wb') as f:
        f.write(front_data)
    with open('back.jpg','wb') as f:
        f.write(back_data)
    with open('barcode.jpg','wb') as f:
        f.write(bar_data)

    ingred.load()
    bar.load()
    score1 = ingred.detect_ingred('back.jpg')
    score2 = eco.ecoscore(biod, sector, resin)
    score3 = bar.BarcodeReader('barcode.jpg')

    return  score1 + score2 +  score3


if __name__ == '__main__':
    app.run(debug=True)