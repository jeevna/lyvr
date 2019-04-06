from PIL import Image

import pytesseract

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def ocr(image):
    # image example = 'labsample1.jpg'
    img = Image.open(image)

    text = pytesseract.image_to_string(img, lang='eng')

    dict = {}
    dictTemp =[]

    text = text.split(' ')
    for word in text:
        a=str(word).split('\n')
        for w in a:
            wrd = w.rstrip(",").lstrip(",")
            if wrd != 'SERUM' and wrd != 'AM' and wrd != 'TOTAL' and wrd != 'RATIO' and wrd != '(SGOT)' and wrd != 'S' and wrd != 'IF':
                dictTemp.append(wrd)


    # print(dictTemp)
    b = False
    bFin = False
    c = False
    i = 0


    dictCor = []
    cont = True
    for word in dictTemp:

        if word == '' and b:
            print("==========++++++++++++++++")
            b = False
            bFin = True
        if b:
            print("-------", word)
            dict[word] = []
            dictCor.append(word)
        if word == 'Report':
            # print('reached here')
            b = True

        # chars = split(word)
        if word == 'FASTING' and c:
            c = False
        if c:
            print("-------------------")
            # print(dict.keys())

            if cont:
                dict[dictCor[i]].append(word)
                rng = (dictTemp[dictTemp.index(word) + 1])
                ch = list(rng)

                goodorbad = -1   #0 is under, 1 is good, 2 is over
                if ">" in ch:
                    goodorbad = 1
                elif "-" in ch:
                    rng = rng.split("-")
                    if float(word)> int(float(rng[0])) and float(word) < int(float(rng[1])):
                        goodorbad = 1
                    elif float(word) < float(rng[0]):
                        goodorbad = 0
                    else:
                        goodorbad = 2
                if len(dict[dictCor[i]]) == 1:
                    dict[dictCor[i]].append(goodorbad)

                i += 1

            cont = not cont
        if word=='Range' and bFin:
            print("----------------------++++")
            # print(word)
            c = True
            bFin = False


    for k in dict.keys():
        if len(dict[k]) != 2:
            del dict[k]
    return dict
