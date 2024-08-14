def ecoscore(bio,sec,resin):
    # feedback score
    if bio == 1:
        feedback_score = 100
    elif bio == 2:
        feedback_score = 0
    else:
        feedback_score = 50
    # sector score
    if sec == 1:
        sector_score = 30
    elif sec == 2:
        sector_score = 25
    elif sec == 3:
        sector_score = 25
    elif sec == 4:
        sector_score = 30
    elif sec == 5:
        sector_score = 35
    elif sec == 6:
        sector_score = 15
    elif sec == 7:
        sector_score = 40
    else:
        sector_score = 30
    # resin score
    if resin == 1:
        resin_score = 50
    elif resin == 2:
        resin_score = 40
    elif resin == 3:
        resin_score = 30
    elif resin == 4:
        resin_score =20
    elif resin == 5:
        resin_score = 10
    elif resin == 6:
        resin_score = 0
    elif resin == 7:
        resin_score = 0
    return feedback_score + sector_score + resin_score