
def load():
    global cv2
    global decode
    import cv2
    from pyzbar.pyzbar import decode
    
  
# Make one method to decode the barcode
def BarcodeReader(image):
    import warnings
    warnings.filterwarnings('ignore')
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
    
      
    # If not detected then print the message
    if not detectedBarcodes:
        barcode_detected = False
    else:
        barcode_detected = True
          # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:
            if barcode.data!="":
                value = int(barcode.data.decode('utf-8')[:3])
    list50 = [868,868,500,501,502,503,504,505,506,507,508,509,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,590,471,885,955,840,841,842,843,844,845,846,847,848,849,482,487,622,629,893,896,779]
    list25 = [690,691,692,693,694,695,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,890,460,461,462,463,464,465,466,467,468,469,450,451,452,453,454,455,453,457,458,459,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,880,626,899,754,755,628,600,601,750,930,931,932,933,934,935,936,937,938,939]
    if value in list25:
        score = 25
    elif value in list50:
        score = 50
    else:
        score = 75

    return score
