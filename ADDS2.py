def ADDS2(a, b):
    if(a=='0'):
        if(b=='0'):
            return ('0','0')
        if(b=='1'):
            return ('1','0')
        if(b=='2'):
            return ('2','0')
        if(b=='3'):
            return ('3','0')
        if(b=='4'):
            return ('4','0')
        if(b=='5'):
            return ('5','0')
        if(b=='6'):
            return ('6','0')
        if(b=='7'):
            return ('7','0')
        if(b=='8'):
            return ('8','0')
        if(b=='9'):
            return ('9','0')
    if(a=='1'):
        if(b=='0'):
            return ('1','0')
        if(b=='1'):
            return ('2','0')
        if(b=='2'):
            return ('3','0')
        if(b=='3'):
            return ('4','0')
        if(b=='4'):
            return ('5','0')
        if(b=='5'):
            return ('6','0')
        if(b=='6'):
            return ('7','0')
        if(b=='7'):
            return ('8','0')
        if(b=='8'):
            return ('9','0')
        if(b=='9'):
            return ('0','1')
    if(a=='2'):
        if(b=='0'):
            return ('2','0')
        if(b=='1'):
            return ('3','0')
        if(b=='2'):
            return ('4','0')
        if(b=='3'):
            return ('5','0')
        if(b=='4'):
            return ('6','0')
        if(b=='5'):
            return ('7','0')
        if(b=='6'):
            return ('8','0')
        if(b=='7'):
            return ('9','0')
        if(b=='8'):
            return ('0','1')
        if(b=='9'):
            return ('1','1')
    if(a=='3'):
        if(b=='0'):
            return ('3','0')
        if(b=='1'):
            return ('4','0')
        if(b=='2'):
            return ('5','0')
        if(b=='3'):
            return ('6','0')
        if(b=='4'):
            return ('7','0')
        if(b=='5'):
            return ('8','0')
        if(b=='6'):
            return ('9','0')
        if(b=='7'):
            return ('0','1')
        if(b=='8'):
            return ('1','1')
        if(b=='9'):
            return ('2','1')
    if(a=='4'):
        if(b=='0'):
            return ('4','0')
        if(b=='1'):
            return ('5','0')
        if(b=='2'):
            return ('6','0')
        if(b=='3'):
            return ('7','0')
        if(b=='4'):
            return ('8','0')
        if(b=='5'):
            return ('9','0')
        if(b=='6'):
            return ('0','1')
        if(b=='7'):
            return ('1','1')
        if(b=='8'):
            return ('2','1')
        if(b=='9'):
            return ('3','1')
    if(a=='5'):
        if(b=='0'):
            return ('5','0')
        if(b=='1'):
            return ('6','0')
        if(b=='2'):
            return ('7','0')
        if(b=='3'):
            return ('8','0')
        if(b=='4'):
            return ('9','0')
        if(b=='5'):
            return ('0','1')
        if(b=='6'):
            return ('1','1')
        if(b=='7'):
            return ('2','1')
        if(b=='8'):
            return ('3','1')
        if(b=='9'):
            return ('4','1')
    if(a=='6'):
        if(b=='0'):
            return ('6','0')
        if(b=='1'):
            return ('7','0')
        if(b=='2'):
            return ('8','0')
        if(b=='3'):
            return ('9','0')
        if(b=='4'):
            return ('0','1')
        if(b=='5'):
            return ('1','1')
        if(b=='6'):
            return ('2','1')
        if(b=='7'):
            return ('3','1')
        if(b=='8'):
            return ('4','1')
        if(b=='9'):
            return ('5','1')
    if(a=='7'):
        if(b=='0'):
            return ('7','0')
        if(b=='1'):
            return ('8','0')
        if(b=='2'):
            return ('9','0')
        if(b=='3'):
            return ('0','1')
        if(b=='4'):
            return ('1','1')
        if(b=='5'):
            return ('2','1')
        if(b=='6'):
            return ('3','1')
        if(b=='7'):
            return ('4','1')
        if(b=='8'):
            return ('5','1')
        if(b=='9'):
            return ('6','1')
    if(a=='8'):
        if(b=='0'):
            return ('8','0')
        if(b=='1'):
            return ('9','0')
        if(b=='2'):
            return ('0','1')
        if(b=='3'):
            return ('1','1')
        if(b=='4'):
            return ('2','1')
        if(b=='5'):
            return ('3','1')
        if(b=='6'):
            return ('4','1')
        if(b=='7'):
            return ('5','1')
        if(b=='8'):
            return ('6','1')
        if(b=='9'):
            return ('7','1')
    if(a=='9'):
        if(b=='0'):
            return ('9','0')
        if(b=='1'):
            return ('0','1')
        if(b=='2'):
            return ('1','1')
        if(b=='3'):
            return ('2','1')
        if(b=='4'):
            return ('3','1')
        if(b=='5'):
            return ('4','1')
        if(b=='6'):
            return ('5','1')
        if(b=='7'):
            return ('6','1')
        if(b=='8'):
            return ('7','1')
        if(b=='9'):
            return ('8','1')
    raise ValueError('unknown digits in ADDS2')
