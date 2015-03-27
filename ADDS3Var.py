def ADDS3B2(a, b):
    if (a<= '0'):
        if (b<= '0'):
                return ('0','0') #(a='0',b='0')
        else:
            return ('1','0') #(a='0',b='1')
    else:
        if (b<= '0'):
                return ('1','0') #(a='1',b='0')
        else:
            return ('0','1') #(a='1',b='1')
        return ('0','1') #(a='1',b='1')
    raise ValueError('unknown digits in ADDS3b2')
def ADDS3B3(a, b):
    if (a<= '1'):
        if (a<= '0'):
            if (b<= '1'):
                if (b<= '0'):
                        return ('0','0') #(a='0',b='0')
                else:
                    return ('1','0') #(a='0',b='1')
            else:
                return ('2','0') #(a='0',b='2')
        else:
            if (b<= '1'):
                if (b<= '0'):
                        return ('1','0') #(a='1',b='0')
                else:
                    return ('2','0') #(a='1',b='1')
            else:
                return ('0','1') #(a='1',b='2')
    else:
        if (b<= '1'):
            if (b<= '0'):
                    return ('2','0') #(a='2',b='0')
            else:
                return ('0','1') #(a='2',b='1')
        else:
            return ('1','1') #(a='2',b='2')
        return ('1','1') #(a='2',b='2')
    raise ValueError('unknown digits in ADDS3b3')
def ADDS3B4(a, b):
    if (a<= '1'):
        if (a<= '0'):
            if (b<= '1'):
                if (b<= '0'):
                        return ('0','0') #(a='0',b='0')
                else:
                    return ('1','0') #(a='0',b='1')
            elif (b<= '2'):
                    return ('2','0') #(a='0',b='2')
            else:
                return ('3','0') #(a='0',b='3')
        else:
            if (b<= '1'):
                if (b<= '0'):
                        return ('1','0') #(a='1',b='0')
                else:
                    return ('2','0') #(a='1',b='1')
            elif (b<= '2'):
                    return ('3','0') #(a='1',b='2')
            else:
                return ('0','1') #(a='1',b='3')
    elif (a<= '2'):
            if (b<= '1'):
                if (b<= '0'):
                        return ('2','0') #(a='2',b='0')
                else:
                    return ('3','0') #(a='2',b='1')
            elif (b<= '2'):
                    return ('0','1') #(a='2',b='2')
            else:
                return ('1','1') #(a='2',b='3')
    else:
        if (b<= '1'):
            if (b<= '0'):
                    return ('3','0') #(a='3',b='0')
            else:
                return ('0','1') #(a='3',b='1')
        elif (b<= '2'):
                return ('1','1') #(a='3',b='2')
        else:
            return ('2','1') #(a='3',b='3')
        return ('2','1') #(a='3',b='3')
    raise ValueError('unknown digits in ADDS3b4')
def ADDS3B5(a, b):
    if (a<= '2'):
        if (a<= '1'):
            if (a<= '0'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('0','0') #(a='0',b='0')
                        else:
                            return ('1','0') #(a='0',b='1')
                    else:
                        return ('2','0') #(a='0',b='2')
                elif (b<= '3'):
                        return ('3','0') #(a='0',b='3')
                else:
                    return ('4','0') #(a='0',b='4')
            else:
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('1','0') #(a='1',b='0')
                        else:
                            return ('2','0') #(a='1',b='1')
                    else:
                        return ('3','0') #(a='1',b='2')
                elif (b<= '3'):
                        return ('4','0') #(a='1',b='3')
                else:
                    return ('0','1') #(a='1',b='4')
        else:
            if (b<= '2'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('2','0') #(a='2',b='0')
                    else:
                        return ('3','0') #(a='2',b='1')
                else:
                    return ('4','0') #(a='2',b='2')
            elif (b<= '3'):
                    return ('0','1') #(a='2',b='3')
            else:
                return ('1','1') #(a='2',b='4')
    elif (a<= '3'):
            if (b<= '2'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('3','0') #(a='3',b='0')
                    else:
                        return ('4','0') #(a='3',b='1')
                else:
                    return ('0','1') #(a='3',b='2')
            elif (b<= '3'):
                    return ('1','1') #(a='3',b='3')
            else:
                return ('2','1') #(a='3',b='4')
    else:
        if (b<= '2'):
            if (b<= '1'):
                if (b<= '0'):
                        return ('4','0') #(a='4',b='0')
                else:
                    return ('0','1') #(a='4',b='1')
            else:
                return ('1','1') #(a='4',b='2')
        elif (b<= '3'):
                return ('2','1') #(a='4',b='3')
        else:
            return ('3','1') #(a='4',b='4')
        return ('3','1') #(a='4',b='4')
    raise ValueError('unknown digits in ADDS3b5')
def ADDS3B6(a, b):
    if (a<= '2'):
        if (a<= '1'):
            if (a<= '0'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('0','0') #(a='0',b='0')
                        else:
                            return ('1','0') #(a='0',b='1')
                    else:
                        return ('2','0') #(a='0',b='2')
                elif (b<= '4'):
                    if (b<= '3'):
                            return ('3','0') #(a='0',b='3')
                    else:
                        return ('4','0') #(a='0',b='4')
                else:
                    return ('5','0') #(a='0',b='5')
            else:
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('1','0') #(a='1',b='0')
                        else:
                            return ('2','0') #(a='1',b='1')
                    else:
                        return ('3','0') #(a='1',b='2')
                elif (b<= '4'):
                    if (b<= '3'):
                            return ('4','0') #(a='1',b='3')
                    else:
                        return ('5','0') #(a='1',b='4')
                else:
                    return ('0','1') #(a='1',b='5')
        else:
            if (b<= '2'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('2','0') #(a='2',b='0')
                    else:
                        return ('3','0') #(a='2',b='1')
                else:
                    return ('4','0') #(a='2',b='2')
            elif (b<= '4'):
                if (b<= '3'):
                        return ('5','0') #(a='2',b='3')
                else:
                    return ('0','1') #(a='2',b='4')
            else:
                return ('1','1') #(a='2',b='5')
    elif (a<= '4'):
        if (a<= '3'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('3','0') #(a='3',b='0')
                        else:
                            return ('4','0') #(a='3',b='1')
                    else:
                        return ('5','0') #(a='3',b='2')
                elif (b<= '4'):
                    if (b<= '3'):
                            return ('0','1') #(a='3',b='3')
                    else:
                        return ('1','1') #(a='3',b='4')
                else:
                    return ('2','1') #(a='3',b='5')
        else:
            if (b<= '2'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('4','0') #(a='4',b='0')
                    else:
                        return ('5','0') #(a='4',b='1')
                else:
                    return ('0','1') #(a='4',b='2')
            elif (b<= '4'):
                if (b<= '3'):
                        return ('1','1') #(a='4',b='3')
                else:
                    return ('2','1') #(a='4',b='4')
            else:
                return ('3','1') #(a='4',b='5')
    else:
        if (b<= '2'):
            if (b<= '1'):
                if (b<= '0'):
                        return ('5','0') #(a='5',b='0')
                else:
                    return ('0','1') #(a='5',b='1')
            else:
                return ('1','1') #(a='5',b='2')
        elif (b<= '4'):
            if (b<= '3'):
                    return ('2','1') #(a='5',b='3')
            else:
                return ('3','1') #(a='5',b='4')
        else:
            return ('4','1') #(a='5',b='5')
        return ('4','1') #(a='5',b='5')
    raise ValueError('unknown digits in ADDS3b6')
def ADDS3B7(a, b):
    if (a<= '3'):
        if (a<= '1'):
            if (a<= '0'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('0','0') #(a='0',b='0')
                        else:
                            return ('1','0') #(a='0',b='1')
                    elif (b<= '2'):
                            return ('2','0') #(a='0',b='2')
                    else:
                        return ('3','0') #(a='0',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('4','0') #(a='0',b='4')
                    else:
                        return ('5','0') #(a='0',b='5')
                else:
                    return ('6','0') #(a='0',b='6')
            else:
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('1','0') #(a='1',b='0')
                        else:
                            return ('2','0') #(a='1',b='1')
                    elif (b<= '2'):
                            return ('3','0') #(a='1',b='2')
                    else:
                        return ('4','0') #(a='1',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('5','0') #(a='1',b='4')
                    else:
                        return ('6','0') #(a='1',b='5')
                else:
                    return ('0','1') #(a='1',b='6')
        elif (a<= '2'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('2','0') #(a='2',b='0')
                        else:
                            return ('3','0') #(a='2',b='1')
                    elif (b<= '2'):
                            return ('4','0') #(a='2',b='2')
                    else:
                        return ('5','0') #(a='2',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('6','0') #(a='2',b='4')
                    else:
                        return ('0','1') #(a='2',b='5')
                else:
                    return ('1','1') #(a='2',b='6')
        else:
            if (b<= '3'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('3','0') #(a='3',b='0')
                    else:
                        return ('4','0') #(a='3',b='1')
                elif (b<= '2'):
                        return ('5','0') #(a='3',b='2')
                else:
                    return ('6','0') #(a='3',b='3')
            elif (b<= '5'):
                if (b<= '4'):
                        return ('0','1') #(a='3',b='4')
                else:
                    return ('1','1') #(a='3',b='5')
            else:
                return ('2','1') #(a='3',b='6')
    elif (a<= '5'):
        if (a<= '4'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('4','0') #(a='4',b='0')
                        else:
                            return ('5','0') #(a='4',b='1')
                    elif (b<= '2'):
                            return ('6','0') #(a='4',b='2')
                    else:
                        return ('0','1') #(a='4',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('1','1') #(a='4',b='4')
                    else:
                        return ('2','1') #(a='4',b='5')
                else:
                    return ('3','1') #(a='4',b='6')
        else:
            if (b<= '3'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('5','0') #(a='5',b='0')
                    else:
                        return ('6','0') #(a='5',b='1')
                elif (b<= '2'):
                        return ('0','1') #(a='5',b='2')
                else:
                    return ('1','1') #(a='5',b='3')
            elif (b<= '5'):
                if (b<= '4'):
                        return ('2','1') #(a='5',b='4')
                else:
                    return ('3','1') #(a='5',b='5')
            else:
                return ('4','1') #(a='5',b='6')
    else:
        if (b<= '3'):
            if (b<= '1'):
                if (b<= '0'):
                        return ('6','0') #(a='6',b='0')
                else:
                    return ('0','1') #(a='6',b='1')
            elif (b<= '2'):
                    return ('1','1') #(a='6',b='2')
            else:
                return ('2','1') #(a='6',b='3')
        elif (b<= '5'):
            if (b<= '4'):
                    return ('3','1') #(a='6',b='4')
            else:
                return ('4','1') #(a='6',b='5')
        else:
            return ('5','1') #(a='6',b='6')
        return ('5','1') #(a='6',b='6')
    raise ValueError('unknown digits in ADDS3b7')
def ADDS3B8(a, b):
    if (a<= '3'):
        if (a<= '1'):
            if (a<= '0'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('0','0') #(a='0',b='0')
                        else:
                            return ('1','0') #(a='0',b='1')
                    elif (b<= '2'):
                            return ('2','0') #(a='0',b='2')
                    else:
                        return ('3','0') #(a='0',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('4','0') #(a='0',b='4')
                    else:
                        return ('5','0') #(a='0',b='5')
                elif (b<= '6'):
                        return ('6','0') #(a='0',b='6')
                else:
                    return ('7','0') #(a='0',b='7')
            else:
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('1','0') #(a='1',b='0')
                        else:
                            return ('2','0') #(a='1',b='1')
                    elif (b<= '2'):
                            return ('3','0') #(a='1',b='2')
                    else:
                        return ('4','0') #(a='1',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('5','0') #(a='1',b='4')
                    else:
                        return ('6','0') #(a='1',b='5')
                elif (b<= '6'):
                        return ('7','0') #(a='1',b='6')
                else:
                    return ('0','1') #(a='1',b='7')
        elif (a<= '2'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('2','0') #(a='2',b='0')
                        else:
                            return ('3','0') #(a='2',b='1')
                    elif (b<= '2'):
                            return ('4','0') #(a='2',b='2')
                    else:
                        return ('5','0') #(a='2',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('6','0') #(a='2',b='4')
                    else:
                        return ('7','0') #(a='2',b='5')
                elif (b<= '6'):
                        return ('0','1') #(a='2',b='6')
                else:
                    return ('1','1') #(a='2',b='7')
        else:
            if (b<= '3'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('3','0') #(a='3',b='0')
                    else:
                        return ('4','0') #(a='3',b='1')
                elif (b<= '2'):
                        return ('5','0') #(a='3',b='2')
                else:
                    return ('6','0') #(a='3',b='3')
            elif (b<= '5'):
                if (b<= '4'):
                        return ('7','0') #(a='3',b='4')
                else:
                    return ('0','1') #(a='3',b='5')
            elif (b<= '6'):
                    return ('1','1') #(a='3',b='6')
            else:
                return ('2','1') #(a='3',b='7')
    elif (a<= '5'):
        if (a<= '4'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('4','0') #(a='4',b='0')
                        else:
                            return ('5','0') #(a='4',b='1')
                    elif (b<= '2'):
                            return ('6','0') #(a='4',b='2')
                    else:
                        return ('7','0') #(a='4',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('0','1') #(a='4',b='4')
                    else:
                        return ('1','1') #(a='4',b='5')
                elif (b<= '6'):
                        return ('2','1') #(a='4',b='6')
                else:
                    return ('3','1') #(a='4',b='7')
        else:
            if (b<= '3'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('5','0') #(a='5',b='0')
                    else:
                        return ('6','0') #(a='5',b='1')
                elif (b<= '2'):
                        return ('7','0') #(a='5',b='2')
                else:
                    return ('0','1') #(a='5',b='3')
            elif (b<= '5'):
                if (b<= '4'):
                        return ('1','1') #(a='5',b='4')
                else:
                    return ('2','1') #(a='5',b='5')
            elif (b<= '6'):
                    return ('3','1') #(a='5',b='6')
            else:
                return ('4','1') #(a='5',b='7')
    elif (a<= '6'):
            if (b<= '3'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('6','0') #(a='6',b='0')
                    else:
                        return ('7','0') #(a='6',b='1')
                elif (b<= '2'):
                        return ('0','1') #(a='6',b='2')
                else:
                    return ('1','1') #(a='6',b='3')
            elif (b<= '5'):
                if (b<= '4'):
                        return ('2','1') #(a='6',b='4')
                else:
                    return ('3','1') #(a='6',b='5')
            elif (b<= '6'):
                    return ('4','1') #(a='6',b='6')
            else:
                return ('5','1') #(a='6',b='7')
    else:
        if (b<= '3'):
            if (b<= '1'):
                if (b<= '0'):
                        return ('7','0') #(a='7',b='0')
                else:
                    return ('0','1') #(a='7',b='1')
            elif (b<= '2'):
                    return ('1','1') #(a='7',b='2')
            else:
                return ('2','1') #(a='7',b='3')
        elif (b<= '5'):
            if (b<= '4'):
                    return ('3','1') #(a='7',b='4')
            else:
                return ('4','1') #(a='7',b='5')
        elif (b<= '6'):
                return ('5','1') #(a='7',b='6')
        else:
            return ('6','1') #(a='7',b='7')
        return ('6','1') #(a='7',b='7')
    raise ValueError('unknown digits in ADDS3b8')
def ADDS3B9(a, b):
    if (a<= '4'):
        if (a<= '2'):
            if (a<= '1'):
                if (a<= '0'):
                    if (b<= '4'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('0','0') #(a='0',b='0')
                                else:
                                    return ('1','0') #(a='0',b='1')
                            else:
                                return ('2','0') #(a='0',b='2')
                        elif (b<= '3'):
                                return ('3','0') #(a='0',b='3')
                        else:
                            return ('4','0') #(a='0',b='4')
                    elif (b<= '6'):
                        if (b<= '5'):
                                return ('5','0') #(a='0',b='5')
                        else:
                            return ('6','0') #(a='0',b='6')
                    elif (b<= '7'):
                            return ('7','0') #(a='0',b='7')
                    else:
                        return ('8','0') #(a='0',b='8')
                else:
                    if (b<= '4'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('1','0') #(a='1',b='0')
                                else:
                                    return ('2','0') #(a='1',b='1')
                            else:
                                return ('3','0') #(a='1',b='2')
                        elif (b<= '3'):
                                return ('4','0') #(a='1',b='3')
                        else:
                            return ('5','0') #(a='1',b='4')
                    elif (b<= '6'):
                        if (b<= '5'):
                                return ('6','0') #(a='1',b='5')
                        else:
                            return ('7','0') #(a='1',b='6')
                    elif (b<= '7'):
                            return ('8','0') #(a='1',b='7')
                    else:
                        return ('0','1') #(a='1',b='8')
            else:
                if (b<= '4'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('2','0') #(a='2',b='0')
                            else:
                                return ('3','0') #(a='2',b='1')
                        else:
                            return ('4','0') #(a='2',b='2')
                    elif (b<= '3'):
                            return ('5','0') #(a='2',b='3')
                    else:
                        return ('6','0') #(a='2',b='4')
                elif (b<= '6'):
                    if (b<= '5'):
                            return ('7','0') #(a='2',b='5')
                    else:
                        return ('8','0') #(a='2',b='6')
                elif (b<= '7'):
                        return ('0','1') #(a='2',b='7')
                else:
                    return ('1','1') #(a='2',b='8')
        elif (a<= '3'):
                if (b<= '4'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('3','0') #(a='3',b='0')
                            else:
                                return ('4','0') #(a='3',b='1')
                        else:
                            return ('5','0') #(a='3',b='2')
                    elif (b<= '3'):
                            return ('6','0') #(a='3',b='3')
                    else:
                        return ('7','0') #(a='3',b='4')
                elif (b<= '6'):
                    if (b<= '5'):
                            return ('8','0') #(a='3',b='5')
                    else:
                        return ('0','1') #(a='3',b='6')
                elif (b<= '7'):
                        return ('1','1') #(a='3',b='7')
                else:
                    return ('2','1') #(a='3',b='8')
        else:
            if (b<= '4'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('4','0') #(a='4',b='0')
                        else:
                            return ('5','0') #(a='4',b='1')
                    else:
                        return ('6','0') #(a='4',b='2')
                elif (b<= '3'):
                        return ('7','0') #(a='4',b='3')
                else:
                    return ('8','0') #(a='4',b='4')
            elif (b<= '6'):
                if (b<= '5'):
                        return ('0','1') #(a='4',b='5')
                else:
                    return ('1','1') #(a='4',b='6')
            elif (b<= '7'):
                    return ('2','1') #(a='4',b='7')
            else:
                return ('3','1') #(a='4',b='8')
    elif (a<= '6'):
        if (a<= '5'):
                if (b<= '4'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('5','0') #(a='5',b='0')
                            else:
                                return ('6','0') #(a='5',b='1')
                        else:
                            return ('7','0') #(a='5',b='2')
                    elif (b<= '3'):
                            return ('8','0') #(a='5',b='3')
                    else:
                        return ('0','1') #(a='5',b='4')
                elif (b<= '6'):
                    if (b<= '5'):
                            return ('1','1') #(a='5',b='5')
                    else:
                        return ('2','1') #(a='5',b='6')
                elif (b<= '7'):
                        return ('3','1') #(a='5',b='7')
                else:
                    return ('4','1') #(a='5',b='8')
        else:
            if (b<= '4'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('6','0') #(a='6',b='0')
                        else:
                            return ('7','0') #(a='6',b='1')
                    else:
                        return ('8','0') #(a='6',b='2')
                elif (b<= '3'):
                        return ('0','1') #(a='6',b='3')
                else:
                    return ('1','1') #(a='6',b='4')
            elif (b<= '6'):
                if (b<= '5'):
                        return ('2','1') #(a='6',b='5')
                else:
                    return ('3','1') #(a='6',b='6')
            elif (b<= '7'):
                    return ('4','1') #(a='6',b='7')
            else:
                return ('5','1') #(a='6',b='8')
    elif (a<= '7'):
            if (b<= '4'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('7','0') #(a='7',b='0')
                        else:
                            return ('8','0') #(a='7',b='1')
                    else:
                        return ('0','1') #(a='7',b='2')
                elif (b<= '3'):
                        return ('1','1') #(a='7',b='3')
                else:
                    return ('2','1') #(a='7',b='4')
            elif (b<= '6'):
                if (b<= '5'):
                        return ('3','1') #(a='7',b='5')
                else:
                    return ('4','1') #(a='7',b='6')
            elif (b<= '7'):
                    return ('5','1') #(a='7',b='7')
            else:
                return ('6','1') #(a='7',b='8')
    else:
        if (b<= '4'):
            if (b<= '2'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('8','0') #(a='8',b='0')
                    else:
                        return ('0','1') #(a='8',b='1')
                else:
                    return ('1','1') #(a='8',b='2')
            elif (b<= '3'):
                    return ('2','1') #(a='8',b='3')
            else:
                return ('3','1') #(a='8',b='4')
        elif (b<= '6'):
            if (b<= '5'):
                    return ('4','1') #(a='8',b='5')
            else:
                return ('5','1') #(a='8',b='6')
        elif (b<= '7'):
                return ('6','1') #(a='8',b='7')
        else:
            return ('7','1') #(a='8',b='8')
        return ('7','1') #(a='8',b='8')
    raise ValueError('unknown digits in ADDS3b9')
def ADDS3B10(a, b):
    if (a<= '4'):
        if (a<= '2'):
            if (a<= '1'):
                if (a<= '0'):
                    if (b<= '4'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('0','0') #(a='0',b='0')
                                else:
                                    return ('1','0') #(a='0',b='1')
                            else:
                                return ('2','0') #(a='0',b='2')
                        elif (b<= '3'):
                                return ('3','0') #(a='0',b='3')
                        else:
                            return ('4','0') #(a='0',b='4')
                    elif (b<= '7'):
                        if (b<= '6'):
                            if (b<= '5'):
                                    return ('5','0') #(a='0',b='5')
                            else:
                                return ('6','0') #(a='0',b='6')
                        else:
                            return ('7','0') #(a='0',b='7')
                    elif (b<= '8'):
                            return ('8','0') #(a='0',b='8')
                    else:
                        return ('9','0') #(a='0',b='9')
                else:
                    if (b<= '4'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('1','0') #(a='1',b='0')
                                else:
                                    return ('2','0') #(a='1',b='1')
                            else:
                                return ('3','0') #(a='1',b='2')
                        elif (b<= '3'):
                                return ('4','0') #(a='1',b='3')
                        else:
                            return ('5','0') #(a='1',b='4')
                    elif (b<= '7'):
                        if (b<= '6'):
                            if (b<= '5'):
                                    return ('6','0') #(a='1',b='5')
                            else:
                                return ('7','0') #(a='1',b='6')
                        else:
                            return ('8','0') #(a='1',b='7')
                    elif (b<= '8'):
                            return ('9','0') #(a='1',b='8')
                    else:
                        return ('0','1') #(a='1',b='9')
            else:
                if (b<= '4'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('2','0') #(a='2',b='0')
                            else:
                                return ('3','0') #(a='2',b='1')
                        else:
                            return ('4','0') #(a='2',b='2')
                    elif (b<= '3'):
                            return ('5','0') #(a='2',b='3')
                    else:
                        return ('6','0') #(a='2',b='4')
                elif (b<= '7'):
                    if (b<= '6'):
                        if (b<= '5'):
                                return ('7','0') #(a='2',b='5')
                        else:
                            return ('8','0') #(a='2',b='6')
                    else:
                        return ('9','0') #(a='2',b='7')
                elif (b<= '8'):
                        return ('0','1') #(a='2',b='8')
                else:
                    return ('1','1') #(a='2',b='9')
        elif (a<= '3'):
                if (b<= '4'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('3','0') #(a='3',b='0')
                            else:
                                return ('4','0') #(a='3',b='1')
                        else:
                            return ('5','0') #(a='3',b='2')
                    elif (b<= '3'):
                            return ('6','0') #(a='3',b='3')
                    else:
                        return ('7','0') #(a='3',b='4')
                elif (b<= '7'):
                    if (b<= '6'):
                        if (b<= '5'):
                                return ('8','0') #(a='3',b='5')
                        else:
                            return ('9','0') #(a='3',b='6')
                    else:
                        return ('0','1') #(a='3',b='7')
                elif (b<= '8'):
                        return ('1','1') #(a='3',b='8')
                else:
                    return ('2','1') #(a='3',b='9')
        else:
            if (b<= '4'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('4','0') #(a='4',b='0')
                        else:
                            return ('5','0') #(a='4',b='1')
                    else:
                        return ('6','0') #(a='4',b='2')
                elif (b<= '3'):
                        return ('7','0') #(a='4',b='3')
                else:
                    return ('8','0') #(a='4',b='4')
            elif (b<= '7'):
                if (b<= '6'):
                    if (b<= '5'):
                            return ('9','0') #(a='4',b='5')
                    else:
                        return ('0','1') #(a='4',b='6')
                else:
                    return ('1','1') #(a='4',b='7')
            elif (b<= '8'):
                    return ('2','1') #(a='4',b='8')
            else:
                return ('3','1') #(a='4',b='9')
    elif (a<= '7'):
        if (a<= '6'):
            if (a<= '5'):
                    if (b<= '4'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('5','0') #(a='5',b='0')
                                else:
                                    return ('6','0') #(a='5',b='1')
                            else:
                                return ('7','0') #(a='5',b='2')
                        elif (b<= '3'):
                                return ('8','0') #(a='5',b='3')
                        else:
                            return ('9','0') #(a='5',b='4')
                    elif (b<= '7'):
                        if (b<= '6'):
                            if (b<= '5'):
                                    return ('0','1') #(a='5',b='5')
                            else:
                                return ('1','1') #(a='5',b='6')
                        else:
                            return ('2','1') #(a='5',b='7')
                    elif (b<= '8'):
                            return ('3','1') #(a='5',b='8')
                    else:
                        return ('4','1') #(a='5',b='9')
            else:
                if (b<= '4'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('6','0') #(a='6',b='0')
                            else:
                                return ('7','0') #(a='6',b='1')
                        else:
                            return ('8','0') #(a='6',b='2')
                    elif (b<= '3'):
                            return ('9','0') #(a='6',b='3')
                    else:
                        return ('0','1') #(a='6',b='4')
                elif (b<= '7'):
                    if (b<= '6'):
                        if (b<= '5'):
                                return ('1','1') #(a='6',b='5')
                        else:
                            return ('2','1') #(a='6',b='6')
                    else:
                        return ('3','1') #(a='6',b='7')
                elif (b<= '8'):
                        return ('4','1') #(a='6',b='8')
                else:
                    return ('5','1') #(a='6',b='9')
        else:
            if (b<= '4'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('7','0') #(a='7',b='0')
                        else:
                            return ('8','0') #(a='7',b='1')
                    else:
                        return ('9','0') #(a='7',b='2')
                elif (b<= '3'):
                        return ('0','1') #(a='7',b='3')
                else:
                    return ('1','1') #(a='7',b='4')
            elif (b<= '7'):
                if (b<= '6'):
                    if (b<= '5'):
                            return ('2','1') #(a='7',b='5')
                    else:
                        return ('3','1') #(a='7',b='6')
                else:
                    return ('4','1') #(a='7',b='7')
            elif (b<= '8'):
                    return ('5','1') #(a='7',b='8')
            else:
                return ('6','1') #(a='7',b='9')
    elif (a<= '8'):
            if (b<= '4'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('8','0') #(a='8',b='0')
                        else:
                            return ('9','0') #(a='8',b='1')
                    else:
                        return ('0','1') #(a='8',b='2')
                elif (b<= '3'):
                        return ('1','1') #(a='8',b='3')
                else:
                    return ('2','1') #(a='8',b='4')
            elif (b<= '7'):
                if (b<= '6'):
                    if (b<= '5'):
                            return ('3','1') #(a='8',b='5')
                    else:
                        return ('4','1') #(a='8',b='6')
                else:
                    return ('5','1') #(a='8',b='7')
            elif (b<= '8'):
                    return ('6','1') #(a='8',b='8')
            else:
                return ('7','1') #(a='8',b='9')
    else:
        if (b<= '4'):
            if (b<= '2'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('9','0') #(a='9',b='0')
                    else:
                        return ('0','1') #(a='9',b='1')
                else:
                    return ('1','1') #(a='9',b='2')
            elif (b<= '3'):
                    return ('2','1') #(a='9',b='3')
            else:
                return ('3','1') #(a='9',b='4')
        elif (b<= '7'):
            if (b<= '6'):
                if (b<= '5'):
                        return ('4','1') #(a='9',b='5')
                else:
                    return ('5','1') #(a='9',b='6')
            else:
                return ('6','1') #(a='9',b='7')
        elif (b<= '8'):
                return ('7','1') #(a='9',b='8')
        else:
            return ('8','1') #(a='9',b='9')
        return ('8','1') #(a='9',b='9')
    raise ValueError('unknown digits in ADDS3b10')
def ADDS3B11(a, b):
    if (a<= '5'):
        if (a<= '2'):
            if (a<= '1'):
                if (a<= '0'):
                    if (b<= '5'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('0','0') #(a='0',b='0')
                                else:
                                    return ('1','0') #(a='0',b='1')
                            else:
                                return ('2','0') #(a='0',b='2')
                        elif (b<= '4'):
                            if (b<= '3'):
                                    return ('3','0') #(a='0',b='3')
                            else:
                                return ('4','0') #(a='0',b='4')
                        else:
                            return ('5','0') #(a='0',b='5')
                    elif (b<= '8'):
                        if (b<= '7'):
                            if (b<= '6'):
                                    return ('6','0') #(a='0',b='6')
                            else:
                                return ('7','0') #(a='0',b='7')
                        else:
                            return ('8','0') #(a='0',b='8')
                    elif (b<= '9'):
                            return ('9','0') #(a='0',b='9')
                    else:
                        return ('A','0') #(a='0',b='10')
                else:
                    if (b<= '5'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('1','0') #(a='1',b='0')
                                else:
                                    return ('2','0') #(a='1',b='1')
                            else:
                                return ('3','0') #(a='1',b='2')
                        elif (b<= '4'):
                            if (b<= '3'):
                                    return ('4','0') #(a='1',b='3')
                            else:
                                return ('5','0') #(a='1',b='4')
                        else:
                            return ('6','0') #(a='1',b='5')
                    elif (b<= '8'):
                        if (b<= '7'):
                            if (b<= '6'):
                                    return ('7','0') #(a='1',b='6')
                            else:
                                return ('8','0') #(a='1',b='7')
                        else:
                            return ('9','0') #(a='1',b='8')
                    elif (b<= '9'):
                            return ('A','0') #(a='1',b='9')
                    else:
                        return ('0','1') #(a='1',b='10')
            else:
                if (b<= '5'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('2','0') #(a='2',b='0')
                            else:
                                return ('3','0') #(a='2',b='1')
                        else:
                            return ('4','0') #(a='2',b='2')
                    elif (b<= '4'):
                        if (b<= '3'):
                                return ('5','0') #(a='2',b='3')
                        else:
                            return ('6','0') #(a='2',b='4')
                    else:
                        return ('7','0') #(a='2',b='5')
                elif (b<= '8'):
                    if (b<= '7'):
                        if (b<= '6'):
                                return ('8','0') #(a='2',b='6')
                        else:
                            return ('9','0') #(a='2',b='7')
                    else:
                        return ('A','0') #(a='2',b='8')
                elif (b<= '9'):
                        return ('0','1') #(a='2',b='9')
                else:
                    return ('1','1') #(a='2',b='10')
        elif (a<= '4'):
            if (a<= '3'):
                    if (b<= '5'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('3','0') #(a='3',b='0')
                                else:
                                    return ('4','0') #(a='3',b='1')
                            else:
                                return ('5','0') #(a='3',b='2')
                        elif (b<= '4'):
                            if (b<= '3'):
                                    return ('6','0') #(a='3',b='3')
                            else:
                                return ('7','0') #(a='3',b='4')
                        else:
                            return ('8','0') #(a='3',b='5')
                    elif (b<= '8'):
                        if (b<= '7'):
                            if (b<= '6'):
                                    return ('9','0') #(a='3',b='6')
                            else:
                                return ('A','0') #(a='3',b='7')
                        else:
                            return ('0','1') #(a='3',b='8')
                    elif (b<= '9'):
                            return ('1','1') #(a='3',b='9')
                    else:
                        return ('2','1') #(a='3',b='10')
            else:
                if (b<= '5'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('4','0') #(a='4',b='0')
                            else:
                                return ('5','0') #(a='4',b='1')
                        else:
                            return ('6','0') #(a='4',b='2')
                    elif (b<= '4'):
                        if (b<= '3'):
                                return ('7','0') #(a='4',b='3')
                        else:
                            return ('8','0') #(a='4',b='4')
                    else:
                        return ('9','0') #(a='4',b='5')
                elif (b<= '8'):
                    if (b<= '7'):
                        if (b<= '6'):
                                return ('A','0') #(a='4',b='6')
                        else:
                            return ('0','1') #(a='4',b='7')
                    else:
                        return ('1','1') #(a='4',b='8')
                elif (b<= '9'):
                        return ('2','1') #(a='4',b='9')
                else:
                    return ('3','1') #(a='4',b='10')
        else:
            if (b<= '5'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('5','0') #(a='5',b='0')
                        else:
                            return ('6','0') #(a='5',b='1')
                    else:
                        return ('7','0') #(a='5',b='2')
                elif (b<= '4'):
                    if (b<= '3'):
                            return ('8','0') #(a='5',b='3')
                    else:
                        return ('9','0') #(a='5',b='4')
                else:
                    return ('A','0') #(a='5',b='5')
            elif (b<= '8'):
                if (b<= '7'):
                    if (b<= '6'):
                            return ('0','1') #(a='5',b='6')
                    else:
                        return ('1','1') #(a='5',b='7')
                else:
                    return ('2','1') #(a='5',b='8')
            elif (b<= '9'):
                    return ('3','1') #(a='5',b='9')
            else:
                return ('4','1') #(a='5',b='10')
    elif (a<= '8'):
        if (a<= '7'):
            if (a<= '6'):
                    if (b<= '5'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('6','0') #(a='6',b='0')
                                else:
                                    return ('7','0') #(a='6',b='1')
                            else:
                                return ('8','0') #(a='6',b='2')
                        elif (b<= '4'):
                            if (b<= '3'):
                                    return ('9','0') #(a='6',b='3')
                            else:
                                return ('A','0') #(a='6',b='4')
                        else:
                            return ('0','1') #(a='6',b='5')
                    elif (b<= '8'):
                        if (b<= '7'):
                            if (b<= '6'):
                                    return ('1','1') #(a='6',b='6')
                            else:
                                return ('2','1') #(a='6',b='7')
                        else:
                            return ('3','1') #(a='6',b='8')
                    elif (b<= '9'):
                            return ('4','1') #(a='6',b='9')
                    else:
                        return ('5','1') #(a='6',b='10')
            else:
                if (b<= '5'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('7','0') #(a='7',b='0')
                            else:
                                return ('8','0') #(a='7',b='1')
                        else:
                            return ('9','0') #(a='7',b='2')
                    elif (b<= '4'):
                        if (b<= '3'):
                                return ('A','0') #(a='7',b='3')
                        else:
                            return ('0','1') #(a='7',b='4')
                    else:
                        return ('1','1') #(a='7',b='5')
                elif (b<= '8'):
                    if (b<= '7'):
                        if (b<= '6'):
                                return ('2','1') #(a='7',b='6')
                        else:
                            return ('3','1') #(a='7',b='7')
                    else:
                        return ('4','1') #(a='7',b='8')
                elif (b<= '9'):
                        return ('5','1') #(a='7',b='9')
                else:
                    return ('6','1') #(a='7',b='10')
        else:
            if (b<= '5'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('8','0') #(a='8',b='0')
                        else:
                            return ('9','0') #(a='8',b='1')
                    else:
                        return ('A','0') #(a='8',b='2')
                elif (b<= '4'):
                    if (b<= '3'):
                            return ('0','1') #(a='8',b='3')
                    else:
                        return ('1','1') #(a='8',b='4')
                else:
                    return ('2','1') #(a='8',b='5')
            elif (b<= '8'):
                if (b<= '7'):
                    if (b<= '6'):
                            return ('3','1') #(a='8',b='6')
                    else:
                        return ('4','1') #(a='8',b='7')
                else:
                    return ('5','1') #(a='8',b='8')
            elif (b<= '9'):
                    return ('6','1') #(a='8',b='9')
            else:
                return ('7','1') #(a='8',b='10')
    elif (a<= '9'):
            if (b<= '5'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('9','0') #(a='9',b='0')
                        else:
                            return ('A','0') #(a='9',b='1')
                    else:
                        return ('0','1') #(a='9',b='2')
                elif (b<= '4'):
                    if (b<= '3'):
                            return ('1','1') #(a='9',b='3')
                    else:
                        return ('2','1') #(a='9',b='4')
                else:
                    return ('3','1') #(a='9',b='5')
            elif (b<= '8'):
                if (b<= '7'):
                    if (b<= '6'):
                            return ('4','1') #(a='9',b='6')
                    else:
                        return ('5','1') #(a='9',b='7')
                else:
                    return ('6','1') #(a='9',b='8')
            elif (b<= '9'):
                    return ('7','1') #(a='9',b='9')
            else:
                return ('8','1') #(a='9',b='10')
    else:
        if (b<= '5'):
            if (b<= '2'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('A','0') #(a='A',b='0')
                    else:
                        return ('0','1') #(a='A',b='1')
                else:
                    return ('1','1') #(a='A',b='2')
            elif (b<= '4'):
                if (b<= '3'):
                        return ('2','1') #(a='A',b='3')
                else:
                    return ('3','1') #(a='A',b='4')
            else:
                return ('4','1') #(a='A',b='5')
        elif (b<= '8'):
            if (b<= '7'):
                if (b<= '6'):
                        return ('5','1') #(a='A',b='6')
                else:
                    return ('6','1') #(a='A',b='7')
            else:
                return ('7','1') #(a='A',b='8')
        elif (b<= '9'):
                return ('8','1') #(a='A',b='9')
        else:
            return ('9','1') #(a='A',b='10')
        return ('9','1') #(a='A',b='10')
    raise ValueError('unknown digits in ADDS3b11')
def ADDS3B12(a, b):
    if (a<= '5'):
        if (a<= '2'):
            if (a<= '1'):
                if (a<= '0'):
                    if (b<= '5'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('0','0') #(a='0',b='0')
                                else:
                                    return ('1','0') #(a='0',b='1')
                            else:
                                return ('2','0') #(a='0',b='2')
                        elif (b<= '4'):
                            if (b<= '3'):
                                    return ('3','0') #(a='0',b='3')
                            else:
                                return ('4','0') #(a='0',b='4')
                        else:
                            return ('5','0') #(a='0',b='5')
                    elif (b<= '8'):
                        if (b<= '7'):
                            if (b<= '6'):
                                    return ('6','0') #(a='0',b='6')
                            else:
                                return ('7','0') #(a='0',b='7')
                        else:
                            return ('8','0') #(a='0',b='8')
                    elif (b<= '10'):
                        if (b<= '9'):
                                return ('9','0') #(a='0',b='9')
                        else:
                            return ('A','0') #(a='0',b='10')
                    else:
                        return ('B','0') #(a='0',b='11')
                else:
                    if (b<= '5'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('1','0') #(a='1',b='0')
                                else:
                                    return ('2','0') #(a='1',b='1')
                            else:
                                return ('3','0') #(a='1',b='2')
                        elif (b<= '4'):
                            if (b<= '3'):
                                    return ('4','0') #(a='1',b='3')
                            else:
                                return ('5','0') #(a='1',b='4')
                        else:
                            return ('6','0') #(a='1',b='5')
                    elif (b<= '8'):
                        if (b<= '7'):
                            if (b<= '6'):
                                    return ('7','0') #(a='1',b='6')
                            else:
                                return ('8','0') #(a='1',b='7')
                        else:
                            return ('9','0') #(a='1',b='8')
                    elif (b<= '10'):
                        if (b<= '9'):
                                return ('A','0') #(a='1',b='9')
                        else:
                            return ('B','0') #(a='1',b='10')
                    else:
                        return ('0','1') #(a='1',b='11')
            else:
                if (b<= '5'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('2','0') #(a='2',b='0')
                            else:
                                return ('3','0') #(a='2',b='1')
                        else:
                            return ('4','0') #(a='2',b='2')
                    elif (b<= '4'):
                        if (b<= '3'):
                                return ('5','0') #(a='2',b='3')
                        else:
                            return ('6','0') #(a='2',b='4')
                    else:
                        return ('7','0') #(a='2',b='5')
                elif (b<= '8'):
                    if (b<= '7'):
                        if (b<= '6'):
                                return ('8','0') #(a='2',b='6')
                        else:
                            return ('9','0') #(a='2',b='7')
                    else:
                        return ('A','0') #(a='2',b='8')
                elif (b<= '10'):
                    if (b<= '9'):
                            return ('B','0') #(a='2',b='9')
                    else:
                        return ('0','1') #(a='2',b='10')
                else:
                    return ('1','1') #(a='2',b='11')
        elif (a<= '4'):
            if (a<= '3'):
                    if (b<= '5'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('3','0') #(a='3',b='0')
                                else:
                                    return ('4','0') #(a='3',b='1')
                            else:
                                return ('5','0') #(a='3',b='2')
                        elif (b<= '4'):
                            if (b<= '3'):
                                    return ('6','0') #(a='3',b='3')
                            else:
                                return ('7','0') #(a='3',b='4')
                        else:
                            return ('8','0') #(a='3',b='5')
                    elif (b<= '8'):
                        if (b<= '7'):
                            if (b<= '6'):
                                    return ('9','0') #(a='3',b='6')
                            else:
                                return ('A','0') #(a='3',b='7')
                        else:
                            return ('B','0') #(a='3',b='8')
                    elif (b<= '10'):
                        if (b<= '9'):
                                return ('0','1') #(a='3',b='9')
                        else:
                            return ('1','1') #(a='3',b='10')
                    else:
                        return ('2','1') #(a='3',b='11')
            else:
                if (b<= '5'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('4','0') #(a='4',b='0')
                            else:
                                return ('5','0') #(a='4',b='1')
                        else:
                            return ('6','0') #(a='4',b='2')
                    elif (b<= '4'):
                        if (b<= '3'):
                                return ('7','0') #(a='4',b='3')
                        else:
                            return ('8','0') #(a='4',b='4')
                    else:
                        return ('9','0') #(a='4',b='5')
                elif (b<= '8'):
                    if (b<= '7'):
                        if (b<= '6'):
                                return ('A','0') #(a='4',b='6')
                        else:
                            return ('B','0') #(a='4',b='7')
                    else:
                        return ('0','1') #(a='4',b='8')
                elif (b<= '10'):
                    if (b<= '9'):
                            return ('1','1') #(a='4',b='9')
                    else:
                        return ('2','1') #(a='4',b='10')
                else:
                    return ('3','1') #(a='4',b='11')
        else:
            if (b<= '5'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('5','0') #(a='5',b='0')
                        else:
                            return ('6','0') #(a='5',b='1')
                    else:
                        return ('7','0') #(a='5',b='2')
                elif (b<= '4'):
                    if (b<= '3'):
                            return ('8','0') #(a='5',b='3')
                    else:
                        return ('9','0') #(a='5',b='4')
                else:
                    return ('A','0') #(a='5',b='5')
            elif (b<= '8'):
                if (b<= '7'):
                    if (b<= '6'):
                            return ('B','0') #(a='5',b='6')
                    else:
                        return ('0','1') #(a='5',b='7')
                else:
                    return ('1','1') #(a='5',b='8')
            elif (b<= '10'):
                if (b<= '9'):
                        return ('2','1') #(a='5',b='9')
                else:
                    return ('3','1') #(a='5',b='10')
            else:
                return ('4','1') #(a='5',b='11')
    elif (a<= '8'):
        if (a<= '7'):
            if (a<= '6'):
                    if (b<= '5'):
                        if (b<= '2'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('6','0') #(a='6',b='0')
                                else:
                                    return ('7','0') #(a='6',b='1')
                            else:
                                return ('8','0') #(a='6',b='2')
                        elif (b<= '4'):
                            if (b<= '3'):
                                    return ('9','0') #(a='6',b='3')
                            else:
                                return ('A','0') #(a='6',b='4')
                        else:
                            return ('B','0') #(a='6',b='5')
                    elif (b<= '8'):
                        if (b<= '7'):
                            if (b<= '6'):
                                    return ('0','1') #(a='6',b='6')
                            else:
                                return ('1','1') #(a='6',b='7')
                        else:
                            return ('2','1') #(a='6',b='8')
                    elif (b<= '10'):
                        if (b<= '9'):
                                return ('3','1') #(a='6',b='9')
                        else:
                            return ('4','1') #(a='6',b='10')
                    else:
                        return ('5','1') #(a='6',b='11')
            else:
                if (b<= '5'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('7','0') #(a='7',b='0')
                            else:
                                return ('8','0') #(a='7',b='1')
                        else:
                            return ('9','0') #(a='7',b='2')
                    elif (b<= '4'):
                        if (b<= '3'):
                                return ('A','0') #(a='7',b='3')
                        else:
                            return ('B','0') #(a='7',b='4')
                    else:
                        return ('0','1') #(a='7',b='5')
                elif (b<= '8'):
                    if (b<= '7'):
                        if (b<= '6'):
                                return ('1','1') #(a='7',b='6')
                        else:
                            return ('2','1') #(a='7',b='7')
                    else:
                        return ('3','1') #(a='7',b='8')
                elif (b<= '10'):
                    if (b<= '9'):
                            return ('4','1') #(a='7',b='9')
                    else:
                        return ('5','1') #(a='7',b='10')
                else:
                    return ('6','1') #(a='7',b='11')
        else:
            if (b<= '5'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('8','0') #(a='8',b='0')
                        else:
                            return ('9','0') #(a='8',b='1')
                    else:
                        return ('A','0') #(a='8',b='2')
                elif (b<= '4'):
                    if (b<= '3'):
                            return ('B','0') #(a='8',b='3')
                    else:
                        return ('0','1') #(a='8',b='4')
                else:
                    return ('1','1') #(a='8',b='5')
            elif (b<= '8'):
                if (b<= '7'):
                    if (b<= '6'):
                            return ('2','1') #(a='8',b='6')
                    else:
                        return ('3','1') #(a='8',b='7')
                else:
                    return ('4','1') #(a='8',b='8')
            elif (b<= '10'):
                if (b<= '9'):
                        return ('5','1') #(a='8',b='9')
                else:
                    return ('6','1') #(a='8',b='10')
            else:
                return ('7','1') #(a='8',b='11')
    elif (a<= '10'):
        if (a<= '9'):
                if (b<= '5'):
                    if (b<= '2'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('9','0') #(a='9',b='0')
                            else:
                                return ('A','0') #(a='9',b='1')
                        else:
                            return ('B','0') #(a='9',b='2')
                    elif (b<= '4'):
                        if (b<= '3'):
                                return ('0','1') #(a='9',b='3')
                        else:
                            return ('1','1') #(a='9',b='4')
                    else:
                        return ('2','1') #(a='9',b='5')
                elif (b<= '8'):
                    if (b<= '7'):
                        if (b<= '6'):
                                return ('3','1') #(a='9',b='6')
                        else:
                            return ('4','1') #(a='9',b='7')
                    else:
                        return ('5','1') #(a='9',b='8')
                elif (b<= '10'):
                    if (b<= '9'):
                            return ('6','1') #(a='9',b='9')
                    else:
                        return ('7','1') #(a='9',b='10')
                else:
                    return ('8','1') #(a='9',b='11')
        else:
            if (b<= '5'):
                if (b<= '2'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('A','0') #(a='A',b='0')
                        else:
                            return ('B','0') #(a='A',b='1')
                    else:
                        return ('0','1') #(a='A',b='2')
                elif (b<= '4'):
                    if (b<= '3'):
                            return ('1','1') #(a='A',b='3')
                    else:
                        return ('2','1') #(a='A',b='4')
                else:
                    return ('3','1') #(a='A',b='5')
            elif (b<= '8'):
                if (b<= '7'):
                    if (b<= '6'):
                            return ('4','1') #(a='A',b='6')
                    else:
                        return ('5','1') #(a='A',b='7')
                else:
                    return ('6','1') #(a='A',b='8')
            elif (b<= '10'):
                if (b<= '9'):
                        return ('7','1') #(a='A',b='9')
                else:
                    return ('8','1') #(a='A',b='10')
            else:
                return ('9','1') #(a='A',b='11')
    else:
        if (b<= '5'):
            if (b<= '2'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('B','0') #(a='B',b='0')
                    else:
                        return ('0','1') #(a='B',b='1')
                else:
                    return ('1','1') #(a='B',b='2')
            elif (b<= '4'):
                if (b<= '3'):
                        return ('2','1') #(a='B',b='3')
                else:
                    return ('3','1') #(a='B',b='4')
            else:
                return ('4','1') #(a='B',b='5')
        elif (b<= '8'):
            if (b<= '7'):
                if (b<= '6'):
                        return ('5','1') #(a='B',b='6')
                else:
                    return ('6','1') #(a='B',b='7')
            else:
                return ('7','1') #(a='B',b='8')
        elif (b<= '10'):
            if (b<= '9'):
                    return ('8','1') #(a='B',b='9')
            else:
                return ('9','1') #(a='B',b='10')
        else:
            return ('A','1') #(a='B',b='11')
        return ('A','1') #(a='B',b='11')
    raise ValueError('unknown digits in ADDS3b12')
def ADDS3B13(a, b):
    if (a<= '6'):
        if (a<= '3'):
            if (a<= '1'):
                if (a<= '0'):
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('0','0') #(a='0',b='0')
                                else:
                                    return ('1','0') #(a='0',b='1')
                            elif (b<= '2'):
                                    return ('2','0') #(a='0',b='2')
                            else:
                                return ('3','0') #(a='0',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('4','0') #(a='0',b='4')
                            else:
                                return ('5','0') #(a='0',b='5')
                        else:
                            return ('6','0') #(a='0',b='6')
                    elif (b<= '9'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('7','0') #(a='0',b='7')
                            else:
                                return ('8','0') #(a='0',b='8')
                        else:
                            return ('9','0') #(a='0',b='9')
                    elif (b<= '11'):
                        if (b<= '10'):
                                return ('A','0') #(a='0',b='10')
                        else:
                            return ('B','0') #(a='0',b='11')
                    else:
                        return ('C','0') #(a='0',b='12')
                else:
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('1','0') #(a='1',b='0')
                                else:
                                    return ('2','0') #(a='1',b='1')
                            elif (b<= '2'):
                                    return ('3','0') #(a='1',b='2')
                            else:
                                return ('4','0') #(a='1',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('5','0') #(a='1',b='4')
                            else:
                                return ('6','0') #(a='1',b='5')
                        else:
                            return ('7','0') #(a='1',b='6')
                    elif (b<= '9'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('8','0') #(a='1',b='7')
                            else:
                                return ('9','0') #(a='1',b='8')
                        else:
                            return ('A','0') #(a='1',b='9')
                    elif (b<= '11'):
                        if (b<= '10'):
                                return ('B','0') #(a='1',b='10')
                        else:
                            return ('C','0') #(a='1',b='11')
                    else:
                        return ('0','1') #(a='1',b='12')
            elif (a<= '2'):
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('2','0') #(a='2',b='0')
                                else:
                                    return ('3','0') #(a='2',b='1')
                            elif (b<= '2'):
                                    return ('4','0') #(a='2',b='2')
                            else:
                                return ('5','0') #(a='2',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('6','0') #(a='2',b='4')
                            else:
                                return ('7','0') #(a='2',b='5')
                        else:
                            return ('8','0') #(a='2',b='6')
                    elif (b<= '9'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('9','0') #(a='2',b='7')
                            else:
                                return ('A','0') #(a='2',b='8')
                        else:
                            return ('B','0') #(a='2',b='9')
                    elif (b<= '11'):
                        if (b<= '10'):
                                return ('C','0') #(a='2',b='10')
                        else:
                            return ('0','1') #(a='2',b='11')
                    else:
                        return ('1','1') #(a='2',b='12')
            else:
                if (b<= '6'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('3','0') #(a='3',b='0')
                            else:
                                return ('4','0') #(a='3',b='1')
                        elif (b<= '2'):
                                return ('5','0') #(a='3',b='2')
                        else:
                            return ('6','0') #(a='3',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('7','0') #(a='3',b='4')
                        else:
                            return ('8','0') #(a='3',b='5')
                    else:
                        return ('9','0') #(a='3',b='6')
                elif (b<= '9'):
                    if (b<= '8'):
                        if (b<= '7'):
                                return ('A','0') #(a='3',b='7')
                        else:
                            return ('B','0') #(a='3',b='8')
                    else:
                        return ('C','0') #(a='3',b='9')
                elif (b<= '11'):
                    if (b<= '10'):
                            return ('0','1') #(a='3',b='10')
                    else:
                        return ('1','1') #(a='3',b='11')
                else:
                    return ('2','1') #(a='3',b='12')
        elif (a<= '5'):
            if (a<= '4'):
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('4','0') #(a='4',b='0')
                                else:
                                    return ('5','0') #(a='4',b='1')
                            elif (b<= '2'):
                                    return ('6','0') #(a='4',b='2')
                            else:
                                return ('7','0') #(a='4',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('8','0') #(a='4',b='4')
                            else:
                                return ('9','0') #(a='4',b='5')
                        else:
                            return ('A','0') #(a='4',b='6')
                    elif (b<= '9'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('B','0') #(a='4',b='7')
                            else:
                                return ('C','0') #(a='4',b='8')
                        else:
                            return ('0','1') #(a='4',b='9')
                    elif (b<= '11'):
                        if (b<= '10'):
                                return ('1','1') #(a='4',b='10')
                        else:
                            return ('2','1') #(a='4',b='11')
                    else:
                        return ('3','1') #(a='4',b='12')
            else:
                if (b<= '6'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('5','0') #(a='5',b='0')
                            else:
                                return ('6','0') #(a='5',b='1')
                        elif (b<= '2'):
                                return ('7','0') #(a='5',b='2')
                        else:
                            return ('8','0') #(a='5',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('9','0') #(a='5',b='4')
                        else:
                            return ('A','0') #(a='5',b='5')
                    else:
                        return ('B','0') #(a='5',b='6')
                elif (b<= '9'):
                    if (b<= '8'):
                        if (b<= '7'):
                                return ('C','0') #(a='5',b='7')
                        else:
                            return ('0','1') #(a='5',b='8')
                    else:
                        return ('1','1') #(a='5',b='9')
                elif (b<= '11'):
                    if (b<= '10'):
                            return ('2','1') #(a='5',b='10')
                    else:
                        return ('3','1') #(a='5',b='11')
                else:
                    return ('4','1') #(a='5',b='12')
        else:
            if (b<= '6'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('6','0') #(a='6',b='0')
                        else:
                            return ('7','0') #(a='6',b='1')
                    elif (b<= '2'):
                            return ('8','0') #(a='6',b='2')
                    else:
                        return ('9','0') #(a='6',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('A','0') #(a='6',b='4')
                    else:
                        return ('B','0') #(a='6',b='5')
                else:
                    return ('C','0') #(a='6',b='6')
            elif (b<= '9'):
                if (b<= '8'):
                    if (b<= '7'):
                            return ('0','1') #(a='6',b='7')
                    else:
                        return ('1','1') #(a='6',b='8')
                else:
                    return ('2','1') #(a='6',b='9')
            elif (b<= '11'):
                if (b<= '10'):
                        return ('3','1') #(a='6',b='10')
                else:
                    return ('4','1') #(a='6',b='11')
            else:
                return ('5','1') #(a='6',b='12')
    elif (a<= '9'):
        if (a<= '8'):
            if (a<= '7'):
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('7','0') #(a='7',b='0')
                                else:
                                    return ('8','0') #(a='7',b='1')
                            elif (b<= '2'):
                                    return ('9','0') #(a='7',b='2')
                            else:
                                return ('A','0') #(a='7',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('B','0') #(a='7',b='4')
                            else:
                                return ('C','0') #(a='7',b='5')
                        else:
                            return ('0','1') #(a='7',b='6')
                    elif (b<= '9'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('1','1') #(a='7',b='7')
                            else:
                                return ('2','1') #(a='7',b='8')
                        else:
                            return ('3','1') #(a='7',b='9')
                    elif (b<= '11'):
                        if (b<= '10'):
                                return ('4','1') #(a='7',b='10')
                        else:
                            return ('5','1') #(a='7',b='11')
                    else:
                        return ('6','1') #(a='7',b='12')
            else:
                if (b<= '6'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('8','0') #(a='8',b='0')
                            else:
                                return ('9','0') #(a='8',b='1')
                        elif (b<= '2'):
                                return ('A','0') #(a='8',b='2')
                        else:
                            return ('B','0') #(a='8',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('C','0') #(a='8',b='4')
                        else:
                            return ('0','1') #(a='8',b='5')
                    else:
                        return ('1','1') #(a='8',b='6')
                elif (b<= '9'):
                    if (b<= '8'):
                        if (b<= '7'):
                                return ('2','1') #(a='8',b='7')
                        else:
                            return ('3','1') #(a='8',b='8')
                    else:
                        return ('4','1') #(a='8',b='9')
                elif (b<= '11'):
                    if (b<= '10'):
                            return ('5','1') #(a='8',b='10')
                    else:
                        return ('6','1') #(a='8',b='11')
                else:
                    return ('7','1') #(a='8',b='12')
        else:
            if (b<= '6'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('9','0') #(a='9',b='0')
                        else:
                            return ('A','0') #(a='9',b='1')
                    elif (b<= '2'):
                            return ('B','0') #(a='9',b='2')
                    else:
                        return ('C','0') #(a='9',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('0','1') #(a='9',b='4')
                    else:
                        return ('1','1') #(a='9',b='5')
                else:
                    return ('2','1') #(a='9',b='6')
            elif (b<= '9'):
                if (b<= '8'):
                    if (b<= '7'):
                            return ('3','1') #(a='9',b='7')
                    else:
                        return ('4','1') #(a='9',b='8')
                else:
                    return ('5','1') #(a='9',b='9')
            elif (b<= '11'):
                if (b<= '10'):
                        return ('6','1') #(a='9',b='10')
                else:
                    return ('7','1') #(a='9',b='11')
            else:
                return ('8','1') #(a='9',b='12')
    elif (a<= '11'):
        if (a<= '10'):
                if (b<= '6'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('A','0') #(a='A',b='0')
                            else:
                                return ('B','0') #(a='A',b='1')
                        elif (b<= '2'):
                                return ('C','0') #(a='A',b='2')
                        else:
                            return ('0','1') #(a='A',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('1','1') #(a='A',b='4')
                        else:
                            return ('2','1') #(a='A',b='5')
                    else:
                        return ('3','1') #(a='A',b='6')
                elif (b<= '9'):
                    if (b<= '8'):
                        if (b<= '7'):
                                return ('4','1') #(a='A',b='7')
                        else:
                            return ('5','1') #(a='A',b='8')
                    else:
                        return ('6','1') #(a='A',b='9')
                elif (b<= '11'):
                    if (b<= '10'):
                            return ('7','1') #(a='A',b='10')
                    else:
                        return ('8','1') #(a='A',b='11')
                else:
                    return ('9','1') #(a='A',b='12')
        else:
            if (b<= '6'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('B','0') #(a='B',b='0')
                        else:
                            return ('C','0') #(a='B',b='1')
                    elif (b<= '2'):
                            return ('0','1') #(a='B',b='2')
                    else:
                        return ('1','1') #(a='B',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('2','1') #(a='B',b='4')
                    else:
                        return ('3','1') #(a='B',b='5')
                else:
                    return ('4','1') #(a='B',b='6')
            elif (b<= '9'):
                if (b<= '8'):
                    if (b<= '7'):
                            return ('5','1') #(a='B',b='7')
                    else:
                        return ('6','1') #(a='B',b='8')
                else:
                    return ('7','1') #(a='B',b='9')
            elif (b<= '11'):
                if (b<= '10'):
                        return ('8','1') #(a='B',b='10')
                else:
                    return ('9','1') #(a='B',b='11')
            else:
                return ('A','1') #(a='B',b='12')
    else:
        if (b<= '6'):
            if (b<= '3'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('C','0') #(a='C',b='0')
                    else:
                        return ('0','1') #(a='C',b='1')
                elif (b<= '2'):
                        return ('1','1') #(a='C',b='2')
                else:
                    return ('2','1') #(a='C',b='3')
            elif (b<= '5'):
                if (b<= '4'):
                        return ('3','1') #(a='C',b='4')
                else:
                    return ('4','1') #(a='C',b='5')
            else:
                return ('5','1') #(a='C',b='6')
        elif (b<= '9'):
            if (b<= '8'):
                if (b<= '7'):
                        return ('6','1') #(a='C',b='7')
                else:
                    return ('7','1') #(a='C',b='8')
            else:
                return ('8','1') #(a='C',b='9')
        elif (b<= '11'):
            if (b<= '10'):
                    return ('9','1') #(a='C',b='10')
            else:
                return ('A','1') #(a='C',b='11')
        else:
            return ('B','1') #(a='C',b='12')
        return ('B','1') #(a='C',b='12')
    raise ValueError('unknown digits in ADDS3b13')
def ADDS3B14(a, b):
    if (a<= '6'):
        if (a<= '3'):
            if (a<= '1'):
                if (a<= '0'):
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('0','0') #(a='0',b='0')
                                else:
                                    return ('1','0') #(a='0',b='1')
                            elif (b<= '2'):
                                    return ('2','0') #(a='0',b='2')
                            else:
                                return ('3','0') #(a='0',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('4','0') #(a='0',b='4')
                            else:
                                return ('5','0') #(a='0',b='5')
                        else:
                            return ('6','0') #(a='0',b='6')
                    elif (b<= '10'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('7','0') #(a='0',b='7')
                            else:
                                return ('8','0') #(a='0',b='8')
                        elif (b<= '9'):
                                return ('9','0') #(a='0',b='9')
                        else:
                            return ('A','0') #(a='0',b='10')
                    elif (b<= '12'):
                        if (b<= '11'):
                                return ('B','0') #(a='0',b='11')
                        else:
                            return ('C','0') #(a='0',b='12')
                    else:
                        return ('D','0') #(a='0',b='13')
                else:
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('1','0') #(a='1',b='0')
                                else:
                                    return ('2','0') #(a='1',b='1')
                            elif (b<= '2'):
                                    return ('3','0') #(a='1',b='2')
                            else:
                                return ('4','0') #(a='1',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('5','0') #(a='1',b='4')
                            else:
                                return ('6','0') #(a='1',b='5')
                        else:
                            return ('7','0') #(a='1',b='6')
                    elif (b<= '10'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('8','0') #(a='1',b='7')
                            else:
                                return ('9','0') #(a='1',b='8')
                        elif (b<= '9'):
                                return ('A','0') #(a='1',b='9')
                        else:
                            return ('B','0') #(a='1',b='10')
                    elif (b<= '12'):
                        if (b<= '11'):
                                return ('C','0') #(a='1',b='11')
                        else:
                            return ('D','0') #(a='1',b='12')
                    else:
                        return ('0','1') #(a='1',b='13')
            elif (a<= '2'):
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('2','0') #(a='2',b='0')
                                else:
                                    return ('3','0') #(a='2',b='1')
                            elif (b<= '2'):
                                    return ('4','0') #(a='2',b='2')
                            else:
                                return ('5','0') #(a='2',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('6','0') #(a='2',b='4')
                            else:
                                return ('7','0') #(a='2',b='5')
                        else:
                            return ('8','0') #(a='2',b='6')
                    elif (b<= '10'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('9','0') #(a='2',b='7')
                            else:
                                return ('A','0') #(a='2',b='8')
                        elif (b<= '9'):
                                return ('B','0') #(a='2',b='9')
                        else:
                            return ('C','0') #(a='2',b='10')
                    elif (b<= '12'):
                        if (b<= '11'):
                                return ('D','0') #(a='2',b='11')
                        else:
                            return ('0','1') #(a='2',b='12')
                    else:
                        return ('1','1') #(a='2',b='13')
            else:
                if (b<= '6'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('3','0') #(a='3',b='0')
                            else:
                                return ('4','0') #(a='3',b='1')
                        elif (b<= '2'):
                                return ('5','0') #(a='3',b='2')
                        else:
                            return ('6','0') #(a='3',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('7','0') #(a='3',b='4')
                        else:
                            return ('8','0') #(a='3',b='5')
                    else:
                        return ('9','0') #(a='3',b='6')
                elif (b<= '10'):
                    if (b<= '8'):
                        if (b<= '7'):
                                return ('A','0') #(a='3',b='7')
                        else:
                            return ('B','0') #(a='3',b='8')
                    elif (b<= '9'):
                            return ('C','0') #(a='3',b='9')
                    else:
                        return ('D','0') #(a='3',b='10')
                elif (b<= '12'):
                    if (b<= '11'):
                            return ('0','1') #(a='3',b='11')
                    else:
                        return ('1','1') #(a='3',b='12')
                else:
                    return ('2','1') #(a='3',b='13')
        elif (a<= '5'):
            if (a<= '4'):
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('4','0') #(a='4',b='0')
                                else:
                                    return ('5','0') #(a='4',b='1')
                            elif (b<= '2'):
                                    return ('6','0') #(a='4',b='2')
                            else:
                                return ('7','0') #(a='4',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('8','0') #(a='4',b='4')
                            else:
                                return ('9','0') #(a='4',b='5')
                        else:
                            return ('A','0') #(a='4',b='6')
                    elif (b<= '10'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('B','0') #(a='4',b='7')
                            else:
                                return ('C','0') #(a='4',b='8')
                        elif (b<= '9'):
                                return ('D','0') #(a='4',b='9')
                        else:
                            return ('0','1') #(a='4',b='10')
                    elif (b<= '12'):
                        if (b<= '11'):
                                return ('1','1') #(a='4',b='11')
                        else:
                            return ('2','1') #(a='4',b='12')
                    else:
                        return ('3','1') #(a='4',b='13')
            else:
                if (b<= '6'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('5','0') #(a='5',b='0')
                            else:
                                return ('6','0') #(a='5',b='1')
                        elif (b<= '2'):
                                return ('7','0') #(a='5',b='2')
                        else:
                            return ('8','0') #(a='5',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('9','0') #(a='5',b='4')
                        else:
                            return ('A','0') #(a='5',b='5')
                    else:
                        return ('B','0') #(a='5',b='6')
                elif (b<= '10'):
                    if (b<= '8'):
                        if (b<= '7'):
                                return ('C','0') #(a='5',b='7')
                        else:
                            return ('D','0') #(a='5',b='8')
                    elif (b<= '9'):
                            return ('0','1') #(a='5',b='9')
                    else:
                        return ('1','1') #(a='5',b='10')
                elif (b<= '12'):
                    if (b<= '11'):
                            return ('2','1') #(a='5',b='11')
                    else:
                        return ('3','1') #(a='5',b='12')
                else:
                    return ('4','1') #(a='5',b='13')
        else:
            if (b<= '6'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('6','0') #(a='6',b='0')
                        else:
                            return ('7','0') #(a='6',b='1')
                    elif (b<= '2'):
                            return ('8','0') #(a='6',b='2')
                    else:
                        return ('9','0') #(a='6',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('A','0') #(a='6',b='4')
                    else:
                        return ('B','0') #(a='6',b='5')
                else:
                    return ('C','0') #(a='6',b='6')
            elif (b<= '10'):
                if (b<= '8'):
                    if (b<= '7'):
                            return ('D','0') #(a='6',b='7')
                    else:
                        return ('0','1') #(a='6',b='8')
                elif (b<= '9'):
                        return ('1','1') #(a='6',b='9')
                else:
                    return ('2','1') #(a='6',b='10')
            elif (b<= '12'):
                if (b<= '11'):
                        return ('3','1') #(a='6',b='11')
                else:
                    return ('4','1') #(a='6',b='12')
            else:
                return ('5','1') #(a='6',b='13')
    elif (a<= '10'):
        if (a<= '8'):
            if (a<= '7'):
                    if (b<= '6'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('7','0') #(a='7',b='0')
                                else:
                                    return ('8','0') #(a='7',b='1')
                            elif (b<= '2'):
                                    return ('9','0') #(a='7',b='2')
                            else:
                                return ('A','0') #(a='7',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('B','0') #(a='7',b='4')
                            else:
                                return ('C','0') #(a='7',b='5')
                        else:
                            return ('D','0') #(a='7',b='6')
                    elif (b<= '10'):
                        if (b<= '8'):
                            if (b<= '7'):
                                    return ('0','1') #(a='7',b='7')
                            else:
                                return ('1','1') #(a='7',b='8')
                        elif (b<= '9'):
                                return ('2','1') #(a='7',b='9')
                        else:
                            return ('3','1') #(a='7',b='10')
                    elif (b<= '12'):
                        if (b<= '11'):
                                return ('4','1') #(a='7',b='11')
                        else:
                            return ('5','1') #(a='7',b='12')
                    else:
                        return ('6','1') #(a='7',b='13')
            else:
                if (b<= '6'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('8','0') #(a='8',b='0')
                            else:
                                return ('9','0') #(a='8',b='1')
                        elif (b<= '2'):
                                return ('A','0') #(a='8',b='2')
                        else:
                            return ('B','0') #(a='8',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('C','0') #(a='8',b='4')
                        else:
                            return ('D','0') #(a='8',b='5')
                    else:
                        return ('0','1') #(a='8',b='6')
                elif (b<= '10'):
                    if (b<= '8'):
                        if (b<= '7'):
                                return ('1','1') #(a='8',b='7')
                        else:
                            return ('2','1') #(a='8',b='8')
                    elif (b<= '9'):
                            return ('3','1') #(a='8',b='9')
                    else:
                        return ('4','1') #(a='8',b='10')
                elif (b<= '12'):
                    if (b<= '11'):
                            return ('5','1') #(a='8',b='11')
                    else:
                        return ('6','1') #(a='8',b='12')
                else:
                    return ('7','1') #(a='8',b='13')
        elif (a<= '9'):
                if (b<= '6'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('9','0') #(a='9',b='0')
                            else:
                                return ('A','0') #(a='9',b='1')
                        elif (b<= '2'):
                                return ('B','0') #(a='9',b='2')
                        else:
                            return ('C','0') #(a='9',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('D','0') #(a='9',b='4')
                        else:
                            return ('0','1') #(a='9',b='5')
                    else:
                        return ('1','1') #(a='9',b='6')
                elif (b<= '10'):
                    if (b<= '8'):
                        if (b<= '7'):
                                return ('2','1') #(a='9',b='7')
                        else:
                            return ('3','1') #(a='9',b='8')
                    elif (b<= '9'):
                            return ('4','1') #(a='9',b='9')
                    else:
                        return ('5','1') #(a='9',b='10')
                elif (b<= '12'):
                    if (b<= '11'):
                            return ('6','1') #(a='9',b='11')
                    else:
                        return ('7','1') #(a='9',b='12')
                else:
                    return ('8','1') #(a='9',b='13')
        else:
            if (b<= '6'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('A','0') #(a='A',b='0')
                        else:
                            return ('B','0') #(a='A',b='1')
                    elif (b<= '2'):
                            return ('C','0') #(a='A',b='2')
                    else:
                        return ('D','0') #(a='A',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('0','1') #(a='A',b='4')
                    else:
                        return ('1','1') #(a='A',b='5')
                else:
                    return ('2','1') #(a='A',b='6')
            elif (b<= '10'):
                if (b<= '8'):
                    if (b<= '7'):
                            return ('3','1') #(a='A',b='7')
                    else:
                        return ('4','1') #(a='A',b='8')
                elif (b<= '9'):
                        return ('5','1') #(a='A',b='9')
                else:
                    return ('6','1') #(a='A',b='10')
            elif (b<= '12'):
                if (b<= '11'):
                        return ('7','1') #(a='A',b='11')
                else:
                    return ('8','1') #(a='A',b='12')
            else:
                return ('9','1') #(a='A',b='13')
    elif (a<= '12'):
        if (a<= '11'):
                if (b<= '6'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('B','0') #(a='B',b='0')
                            else:
                                return ('C','0') #(a='B',b='1')
                        elif (b<= '2'):
                                return ('D','0') #(a='B',b='2')
                        else:
                            return ('0','1') #(a='B',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('1','1') #(a='B',b='4')
                        else:
                            return ('2','1') #(a='B',b='5')
                    else:
                        return ('3','1') #(a='B',b='6')
                elif (b<= '10'):
                    if (b<= '8'):
                        if (b<= '7'):
                                return ('4','1') #(a='B',b='7')
                        else:
                            return ('5','1') #(a='B',b='8')
                    elif (b<= '9'):
                            return ('6','1') #(a='B',b='9')
                    else:
                        return ('7','1') #(a='B',b='10')
                elif (b<= '12'):
                    if (b<= '11'):
                            return ('8','1') #(a='B',b='11')
                    else:
                        return ('9','1') #(a='B',b='12')
                else:
                    return ('A','1') #(a='B',b='13')
        else:
            if (b<= '6'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('C','0') #(a='C',b='0')
                        else:
                            return ('D','0') #(a='C',b='1')
                    elif (b<= '2'):
                            return ('0','1') #(a='C',b='2')
                    else:
                        return ('1','1') #(a='C',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('2','1') #(a='C',b='4')
                    else:
                        return ('3','1') #(a='C',b='5')
                else:
                    return ('4','1') #(a='C',b='6')
            elif (b<= '10'):
                if (b<= '8'):
                    if (b<= '7'):
                            return ('5','1') #(a='C',b='7')
                    else:
                        return ('6','1') #(a='C',b='8')
                elif (b<= '9'):
                        return ('7','1') #(a='C',b='9')
                else:
                    return ('8','1') #(a='C',b='10')
            elif (b<= '12'):
                if (b<= '11'):
                        return ('9','1') #(a='C',b='11')
                else:
                    return ('A','1') #(a='C',b='12')
            else:
                return ('B','1') #(a='C',b='13')
    else:
        if (b<= '6'):
            if (b<= '3'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('D','0') #(a='D',b='0')
                    else:
                        return ('0','1') #(a='D',b='1')
                elif (b<= '2'):
                        return ('1','1') #(a='D',b='2')
                else:
                    return ('2','1') #(a='D',b='3')
            elif (b<= '5'):
                if (b<= '4'):
                        return ('3','1') #(a='D',b='4')
                else:
                    return ('4','1') #(a='D',b='5')
            else:
                return ('5','1') #(a='D',b='6')
        elif (b<= '10'):
            if (b<= '8'):
                if (b<= '7'):
                        return ('6','1') #(a='D',b='7')
                else:
                    return ('7','1') #(a='D',b='8')
            elif (b<= '9'):
                    return ('8','1') #(a='D',b='9')
            else:
                return ('9','1') #(a='D',b='10')
        elif (b<= '12'):
            if (b<= '11'):
                    return ('A','1') #(a='D',b='11')
            else:
                return ('B','1') #(a='D',b='12')
        else:
            return ('C','1') #(a='D',b='13')
        return ('C','1') #(a='D',b='13')
    raise ValueError('unknown digits in ADDS3b14')
def ADDS3B15(a, b):
    if (a<= '7'):
        if (a<= '3'):
            if (a<= '1'):
                if (a<= '0'):
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('0','0') #(a='0',b='0')
                                else:
                                    return ('1','0') #(a='0',b='1')
                            elif (b<= '2'):
                                    return ('2','0') #(a='0',b='2')
                            else:
                                return ('3','0') #(a='0',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('4','0') #(a='0',b='4')
                            else:
                                return ('5','0') #(a='0',b='5')
                        elif (b<= '6'):
                                return ('6','0') #(a='0',b='6')
                        else:
                            return ('7','0') #(a='0',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('8','0') #(a='0',b='8')
                            else:
                                return ('9','0') #(a='0',b='9')
                        elif (b<= '10'):
                                return ('A','0') #(a='0',b='10')
                        else:
                            return ('B','0') #(a='0',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('C','0') #(a='0',b='12')
                        else:
                            return ('D','0') #(a='0',b='13')
                    else:
                        return ('E','0') #(a='0',b='14')
                else:
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('1','0') #(a='1',b='0')
                                else:
                                    return ('2','0') #(a='1',b='1')
                            elif (b<= '2'):
                                    return ('3','0') #(a='1',b='2')
                            else:
                                return ('4','0') #(a='1',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('5','0') #(a='1',b='4')
                            else:
                                return ('6','0') #(a='1',b='5')
                        elif (b<= '6'):
                                return ('7','0') #(a='1',b='6')
                        else:
                            return ('8','0') #(a='1',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('9','0') #(a='1',b='8')
                            else:
                                return ('A','0') #(a='1',b='9')
                        elif (b<= '10'):
                                return ('B','0') #(a='1',b='10')
                        else:
                            return ('C','0') #(a='1',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('D','0') #(a='1',b='12')
                        else:
                            return ('E','0') #(a='1',b='13')
                    else:
                        return ('0','1') #(a='1',b='14')
            elif (a<= '2'):
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('2','0') #(a='2',b='0')
                                else:
                                    return ('3','0') #(a='2',b='1')
                            elif (b<= '2'):
                                    return ('4','0') #(a='2',b='2')
                            else:
                                return ('5','0') #(a='2',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('6','0') #(a='2',b='4')
                            else:
                                return ('7','0') #(a='2',b='5')
                        elif (b<= '6'):
                                return ('8','0') #(a='2',b='6')
                        else:
                            return ('9','0') #(a='2',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('A','0') #(a='2',b='8')
                            else:
                                return ('B','0') #(a='2',b='9')
                        elif (b<= '10'):
                                return ('C','0') #(a='2',b='10')
                        else:
                            return ('D','0') #(a='2',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('E','0') #(a='2',b='12')
                        else:
                            return ('0','1') #(a='2',b='13')
                    else:
                        return ('1','1') #(a='2',b='14')
            else:
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('3','0') #(a='3',b='0')
                            else:
                                return ('4','0') #(a='3',b='1')
                        elif (b<= '2'):
                                return ('5','0') #(a='3',b='2')
                        else:
                            return ('6','0') #(a='3',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('7','0') #(a='3',b='4')
                        else:
                            return ('8','0') #(a='3',b='5')
                    elif (b<= '6'):
                            return ('9','0') #(a='3',b='6')
                    else:
                        return ('A','0') #(a='3',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('B','0') #(a='3',b='8')
                        else:
                            return ('C','0') #(a='3',b='9')
                    elif (b<= '10'):
                            return ('D','0') #(a='3',b='10')
                    else:
                        return ('E','0') #(a='3',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('0','1') #(a='3',b='12')
                    else:
                        return ('1','1') #(a='3',b='13')
                else:
                    return ('2','1') #(a='3',b='14')
        elif (a<= '5'):
            if (a<= '4'):
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('4','0') #(a='4',b='0')
                                else:
                                    return ('5','0') #(a='4',b='1')
                            elif (b<= '2'):
                                    return ('6','0') #(a='4',b='2')
                            else:
                                return ('7','0') #(a='4',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('8','0') #(a='4',b='4')
                            else:
                                return ('9','0') #(a='4',b='5')
                        elif (b<= '6'):
                                return ('A','0') #(a='4',b='6')
                        else:
                            return ('B','0') #(a='4',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('C','0') #(a='4',b='8')
                            else:
                                return ('D','0') #(a='4',b='9')
                        elif (b<= '10'):
                                return ('E','0') #(a='4',b='10')
                        else:
                            return ('0','1') #(a='4',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('1','1') #(a='4',b='12')
                        else:
                            return ('2','1') #(a='4',b='13')
                    else:
                        return ('3','1') #(a='4',b='14')
            else:
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('5','0') #(a='5',b='0')
                            else:
                                return ('6','0') #(a='5',b='1')
                        elif (b<= '2'):
                                return ('7','0') #(a='5',b='2')
                        else:
                            return ('8','0') #(a='5',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('9','0') #(a='5',b='4')
                        else:
                            return ('A','0') #(a='5',b='5')
                    elif (b<= '6'):
                            return ('B','0') #(a='5',b='6')
                    else:
                        return ('C','0') #(a='5',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('D','0') #(a='5',b='8')
                        else:
                            return ('E','0') #(a='5',b='9')
                    elif (b<= '10'):
                            return ('0','1') #(a='5',b='10')
                    else:
                        return ('1','1') #(a='5',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('2','1') #(a='5',b='12')
                    else:
                        return ('3','1') #(a='5',b='13')
                else:
                    return ('4','1') #(a='5',b='14')
        elif (a<= '6'):
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('6','0') #(a='6',b='0')
                            else:
                                return ('7','0') #(a='6',b='1')
                        elif (b<= '2'):
                                return ('8','0') #(a='6',b='2')
                        else:
                            return ('9','0') #(a='6',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('A','0') #(a='6',b='4')
                        else:
                            return ('B','0') #(a='6',b='5')
                    elif (b<= '6'):
                            return ('C','0') #(a='6',b='6')
                    else:
                        return ('D','0') #(a='6',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('E','0') #(a='6',b='8')
                        else:
                            return ('0','1') #(a='6',b='9')
                    elif (b<= '10'):
                            return ('1','1') #(a='6',b='10')
                    else:
                        return ('2','1') #(a='6',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('3','1') #(a='6',b='12')
                    else:
                        return ('4','1') #(a='6',b='13')
                else:
                    return ('5','1') #(a='6',b='14')
        else:
            if (b<= '7'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('7','0') #(a='7',b='0')
                        else:
                            return ('8','0') #(a='7',b='1')
                    elif (b<= '2'):
                            return ('9','0') #(a='7',b='2')
                    else:
                        return ('A','0') #(a='7',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('B','0') #(a='7',b='4')
                    else:
                        return ('C','0') #(a='7',b='5')
                elif (b<= '6'):
                        return ('D','0') #(a='7',b='6')
                else:
                    return ('E','0') #(a='7',b='7')
            elif (b<= '11'):
                if (b<= '9'):
                    if (b<= '8'):
                            return ('0','1') #(a='7',b='8')
                    else:
                        return ('1','1') #(a='7',b='9')
                elif (b<= '10'):
                        return ('2','1') #(a='7',b='10')
                else:
                    return ('3','1') #(a='7',b='11')
            elif (b<= '13'):
                if (b<= '12'):
                        return ('4','1') #(a='7',b='12')
                else:
                    return ('5','1') #(a='7',b='13')
            else:
                return ('6','1') #(a='7',b='14')
    elif (a<= '11'):
        if (a<= '9'):
            if (a<= '8'):
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('8','0') #(a='8',b='0')
                                else:
                                    return ('9','0') #(a='8',b='1')
                            elif (b<= '2'):
                                    return ('A','0') #(a='8',b='2')
                            else:
                                return ('B','0') #(a='8',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('C','0') #(a='8',b='4')
                            else:
                                return ('D','0') #(a='8',b='5')
                        elif (b<= '6'):
                                return ('E','0') #(a='8',b='6')
                        else:
                            return ('0','1') #(a='8',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('1','1') #(a='8',b='8')
                            else:
                                return ('2','1') #(a='8',b='9')
                        elif (b<= '10'):
                                return ('3','1') #(a='8',b='10')
                        else:
                            return ('4','1') #(a='8',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('5','1') #(a='8',b='12')
                        else:
                            return ('6','1') #(a='8',b='13')
                    else:
                        return ('7','1') #(a='8',b='14')
            else:
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('9','0') #(a='9',b='0')
                            else:
                                return ('A','0') #(a='9',b='1')
                        elif (b<= '2'):
                                return ('B','0') #(a='9',b='2')
                        else:
                            return ('C','0') #(a='9',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('D','0') #(a='9',b='4')
                        else:
                            return ('E','0') #(a='9',b='5')
                    elif (b<= '6'):
                            return ('0','1') #(a='9',b='6')
                    else:
                        return ('1','1') #(a='9',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('2','1') #(a='9',b='8')
                        else:
                            return ('3','1') #(a='9',b='9')
                    elif (b<= '10'):
                            return ('4','1') #(a='9',b='10')
                    else:
                        return ('5','1') #(a='9',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('6','1') #(a='9',b='12')
                    else:
                        return ('7','1') #(a='9',b='13')
                else:
                    return ('8','1') #(a='9',b='14')
        elif (a<= '10'):
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('A','0') #(a='A',b='0')
                            else:
                                return ('B','0') #(a='A',b='1')
                        elif (b<= '2'):
                                return ('C','0') #(a='A',b='2')
                        else:
                            return ('D','0') #(a='A',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('E','0') #(a='A',b='4')
                        else:
                            return ('0','1') #(a='A',b='5')
                    elif (b<= '6'):
                            return ('1','1') #(a='A',b='6')
                    else:
                        return ('2','1') #(a='A',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('3','1') #(a='A',b='8')
                        else:
                            return ('4','1') #(a='A',b='9')
                    elif (b<= '10'):
                            return ('5','1') #(a='A',b='10')
                    else:
                        return ('6','1') #(a='A',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('7','1') #(a='A',b='12')
                    else:
                        return ('8','1') #(a='A',b='13')
                else:
                    return ('9','1') #(a='A',b='14')
        else:
            if (b<= '7'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('B','0') #(a='B',b='0')
                        else:
                            return ('C','0') #(a='B',b='1')
                    elif (b<= '2'):
                            return ('D','0') #(a='B',b='2')
                    else:
                        return ('E','0') #(a='B',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('0','1') #(a='B',b='4')
                    else:
                        return ('1','1') #(a='B',b='5')
                elif (b<= '6'):
                        return ('2','1') #(a='B',b='6')
                else:
                    return ('3','1') #(a='B',b='7')
            elif (b<= '11'):
                if (b<= '9'):
                    if (b<= '8'):
                            return ('4','1') #(a='B',b='8')
                    else:
                        return ('5','1') #(a='B',b='9')
                elif (b<= '10'):
                        return ('6','1') #(a='B',b='10')
                else:
                    return ('7','1') #(a='B',b='11')
            elif (b<= '13'):
                if (b<= '12'):
                        return ('8','1') #(a='B',b='12')
                else:
                    return ('9','1') #(a='B',b='13')
            else:
                return ('A','1') #(a='B',b='14')
    elif (a<= '13'):
        if (a<= '12'):
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('C','0') #(a='C',b='0')
                            else:
                                return ('D','0') #(a='C',b='1')
                        elif (b<= '2'):
                                return ('E','0') #(a='C',b='2')
                        else:
                            return ('0','1') #(a='C',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('1','1') #(a='C',b='4')
                        else:
                            return ('2','1') #(a='C',b='5')
                    elif (b<= '6'):
                            return ('3','1') #(a='C',b='6')
                    else:
                        return ('4','1') #(a='C',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('5','1') #(a='C',b='8')
                        else:
                            return ('6','1') #(a='C',b='9')
                    elif (b<= '10'):
                            return ('7','1') #(a='C',b='10')
                    else:
                        return ('8','1') #(a='C',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('9','1') #(a='C',b='12')
                    else:
                        return ('A','1') #(a='C',b='13')
                else:
                    return ('B','1') #(a='C',b='14')
        else:
            if (b<= '7'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('D','0') #(a='D',b='0')
                        else:
                            return ('E','0') #(a='D',b='1')
                    elif (b<= '2'):
                            return ('0','1') #(a='D',b='2')
                    else:
                        return ('1','1') #(a='D',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('2','1') #(a='D',b='4')
                    else:
                        return ('3','1') #(a='D',b='5')
                elif (b<= '6'):
                        return ('4','1') #(a='D',b='6')
                else:
                    return ('5','1') #(a='D',b='7')
            elif (b<= '11'):
                if (b<= '9'):
                    if (b<= '8'):
                            return ('6','1') #(a='D',b='8')
                    else:
                        return ('7','1') #(a='D',b='9')
                elif (b<= '10'):
                        return ('8','1') #(a='D',b='10')
                else:
                    return ('9','1') #(a='D',b='11')
            elif (b<= '13'):
                if (b<= '12'):
                        return ('A','1') #(a='D',b='12')
                else:
                    return ('B','1') #(a='D',b='13')
            else:
                return ('C','1') #(a='D',b='14')
    else:
        if (b<= '7'):
            if (b<= '3'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('E','0') #(a='E',b='0')
                    else:
                        return ('0','1') #(a='E',b='1')
                elif (b<= '2'):
                        return ('1','1') #(a='E',b='2')
                else:
                    return ('2','1') #(a='E',b='3')
            elif (b<= '5'):
                if (b<= '4'):
                        return ('3','1') #(a='E',b='4')
                else:
                    return ('4','1') #(a='E',b='5')
            elif (b<= '6'):
                    return ('5','1') #(a='E',b='6')
            else:
                return ('6','1') #(a='E',b='7')
        elif (b<= '11'):
            if (b<= '9'):
                if (b<= '8'):
                        return ('7','1') #(a='E',b='8')
                else:
                    return ('8','1') #(a='E',b='9')
            elif (b<= '10'):
                    return ('9','1') #(a='E',b='10')
            else:
                return ('A','1') #(a='E',b='11')
        elif (b<= '13'):
            if (b<= '12'):
                    return ('B','1') #(a='E',b='12')
            else:
                return ('C','1') #(a='E',b='13')
        else:
            return ('D','1') #(a='E',b='14')
        return ('D','1') #(a='E',b='14')
    raise ValueError('unknown digits in ADDS3b15')
def ADDS3B16(a, b):
    if (a<= '7'):
        if (a<= '3'):
            if (a<= '1'):
                if (a<= '0'):
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('0','0') #(a='0',b='0')
                                else:
                                    return ('1','0') #(a='0',b='1')
                            elif (b<= '2'):
                                    return ('2','0') #(a='0',b='2')
                            else:
                                return ('3','0') #(a='0',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('4','0') #(a='0',b='4')
                            else:
                                return ('5','0') #(a='0',b='5')
                        elif (b<= '6'):
                                return ('6','0') #(a='0',b='6')
                        else:
                            return ('7','0') #(a='0',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('8','0') #(a='0',b='8')
                            else:
                                return ('9','0') #(a='0',b='9')
                        elif (b<= '10'):
                                return ('A','0') #(a='0',b='10')
                        else:
                            return ('B','0') #(a='0',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('C','0') #(a='0',b='12')
                        else:
                            return ('D','0') #(a='0',b='13')
                    elif (b<= '14'):
                            return ('E','0') #(a='0',b='14')
                    else:
                        return ('F','0') #(a='0',b='15')
                else:
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('1','0') #(a='1',b='0')
                                else:
                                    return ('2','0') #(a='1',b='1')
                            elif (b<= '2'):
                                    return ('3','0') #(a='1',b='2')
                            else:
                                return ('4','0') #(a='1',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('5','0') #(a='1',b='4')
                            else:
                                return ('6','0') #(a='1',b='5')
                        elif (b<= '6'):
                                return ('7','0') #(a='1',b='6')
                        else:
                            return ('8','0') #(a='1',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('9','0') #(a='1',b='8')
                            else:
                                return ('A','0') #(a='1',b='9')
                        elif (b<= '10'):
                                return ('B','0') #(a='1',b='10')
                        else:
                            return ('C','0') #(a='1',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('D','0') #(a='1',b='12')
                        else:
                            return ('E','0') #(a='1',b='13')
                    elif (b<= '14'):
                            return ('F','0') #(a='1',b='14')
                    else:
                        return ('0','1') #(a='1',b='15')
            elif (a<= '2'):
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('2','0') #(a='2',b='0')
                                else:
                                    return ('3','0') #(a='2',b='1')
                            elif (b<= '2'):
                                    return ('4','0') #(a='2',b='2')
                            else:
                                return ('5','0') #(a='2',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('6','0') #(a='2',b='4')
                            else:
                                return ('7','0') #(a='2',b='5')
                        elif (b<= '6'):
                                return ('8','0') #(a='2',b='6')
                        else:
                            return ('9','0') #(a='2',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('A','0') #(a='2',b='8')
                            else:
                                return ('B','0') #(a='2',b='9')
                        elif (b<= '10'):
                                return ('C','0') #(a='2',b='10')
                        else:
                            return ('D','0') #(a='2',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('E','0') #(a='2',b='12')
                        else:
                            return ('F','0') #(a='2',b='13')
                    elif (b<= '14'):
                            return ('0','1') #(a='2',b='14')
                    else:
                        return ('1','1') #(a='2',b='15')
            else:
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('3','0') #(a='3',b='0')
                            else:
                                return ('4','0') #(a='3',b='1')
                        elif (b<= '2'):
                                return ('5','0') #(a='3',b='2')
                        else:
                            return ('6','0') #(a='3',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('7','0') #(a='3',b='4')
                        else:
                            return ('8','0') #(a='3',b='5')
                    elif (b<= '6'):
                            return ('9','0') #(a='3',b='6')
                    else:
                        return ('A','0') #(a='3',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('B','0') #(a='3',b='8')
                        else:
                            return ('C','0') #(a='3',b='9')
                    elif (b<= '10'):
                            return ('D','0') #(a='3',b='10')
                    else:
                        return ('E','0') #(a='3',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('F','0') #(a='3',b='12')
                    else:
                        return ('0','1') #(a='3',b='13')
                elif (b<= '14'):
                        return ('1','1') #(a='3',b='14')
                else:
                    return ('2','1') #(a='3',b='15')
        elif (a<= '5'):
            if (a<= '4'):
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('4','0') #(a='4',b='0')
                                else:
                                    return ('5','0') #(a='4',b='1')
                            elif (b<= '2'):
                                    return ('6','0') #(a='4',b='2')
                            else:
                                return ('7','0') #(a='4',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('8','0') #(a='4',b='4')
                            else:
                                return ('9','0') #(a='4',b='5')
                        elif (b<= '6'):
                                return ('A','0') #(a='4',b='6')
                        else:
                            return ('B','0') #(a='4',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('C','0') #(a='4',b='8')
                            else:
                                return ('D','0') #(a='4',b='9')
                        elif (b<= '10'):
                                return ('E','0') #(a='4',b='10')
                        else:
                            return ('F','0') #(a='4',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('0','1') #(a='4',b='12')
                        else:
                            return ('1','1') #(a='4',b='13')
                    elif (b<= '14'):
                            return ('2','1') #(a='4',b='14')
                    else:
                        return ('3','1') #(a='4',b='15')
            else:
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('5','0') #(a='5',b='0')
                            else:
                                return ('6','0') #(a='5',b='1')
                        elif (b<= '2'):
                                return ('7','0') #(a='5',b='2')
                        else:
                            return ('8','0') #(a='5',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('9','0') #(a='5',b='4')
                        else:
                            return ('A','0') #(a='5',b='5')
                    elif (b<= '6'):
                            return ('B','0') #(a='5',b='6')
                    else:
                        return ('C','0') #(a='5',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('D','0') #(a='5',b='8')
                        else:
                            return ('E','0') #(a='5',b='9')
                    elif (b<= '10'):
                            return ('F','0') #(a='5',b='10')
                    else:
                        return ('0','1') #(a='5',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('1','1') #(a='5',b='12')
                    else:
                        return ('2','1') #(a='5',b='13')
                elif (b<= '14'):
                        return ('3','1') #(a='5',b='14')
                else:
                    return ('4','1') #(a='5',b='15')
        elif (a<= '6'):
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('6','0') #(a='6',b='0')
                            else:
                                return ('7','0') #(a='6',b='1')
                        elif (b<= '2'):
                                return ('8','0') #(a='6',b='2')
                        else:
                            return ('9','0') #(a='6',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('A','0') #(a='6',b='4')
                        else:
                            return ('B','0') #(a='6',b='5')
                    elif (b<= '6'):
                            return ('C','0') #(a='6',b='6')
                    else:
                        return ('D','0') #(a='6',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('E','0') #(a='6',b='8')
                        else:
                            return ('F','0') #(a='6',b='9')
                    elif (b<= '10'):
                            return ('0','1') #(a='6',b='10')
                    else:
                        return ('1','1') #(a='6',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('2','1') #(a='6',b='12')
                    else:
                        return ('3','1') #(a='6',b='13')
                elif (b<= '14'):
                        return ('4','1') #(a='6',b='14')
                else:
                    return ('5','1') #(a='6',b='15')
        else:
            if (b<= '7'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('7','0') #(a='7',b='0')
                        else:
                            return ('8','0') #(a='7',b='1')
                    elif (b<= '2'):
                            return ('9','0') #(a='7',b='2')
                    else:
                        return ('A','0') #(a='7',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('B','0') #(a='7',b='4')
                    else:
                        return ('C','0') #(a='7',b='5')
                elif (b<= '6'):
                        return ('D','0') #(a='7',b='6')
                else:
                    return ('E','0') #(a='7',b='7')
            elif (b<= '11'):
                if (b<= '9'):
                    if (b<= '8'):
                            return ('F','0') #(a='7',b='8')
                    else:
                        return ('0','1') #(a='7',b='9')
                elif (b<= '10'):
                        return ('1','1') #(a='7',b='10')
                else:
                    return ('2','1') #(a='7',b='11')
            elif (b<= '13'):
                if (b<= '12'):
                        return ('3','1') #(a='7',b='12')
                else:
                    return ('4','1') #(a='7',b='13')
            elif (b<= '14'):
                    return ('5','1') #(a='7',b='14')
            else:
                return ('6','1') #(a='7',b='15')
    elif (a<= '11'):
        if (a<= '9'):
            if (a<= '8'):
                    if (b<= '7'):
                        if (b<= '3'):
                            if (b<= '1'):
                                if (b<= '0'):
                                        return ('8','0') #(a='8',b='0')
                                else:
                                    return ('9','0') #(a='8',b='1')
                            elif (b<= '2'):
                                    return ('A','0') #(a='8',b='2')
                            else:
                                return ('B','0') #(a='8',b='3')
                        elif (b<= '5'):
                            if (b<= '4'):
                                    return ('C','0') #(a='8',b='4')
                            else:
                                return ('D','0') #(a='8',b='5')
                        elif (b<= '6'):
                                return ('E','0') #(a='8',b='6')
                        else:
                            return ('F','0') #(a='8',b='7')
                    elif (b<= '11'):
                        if (b<= '9'):
                            if (b<= '8'):
                                    return ('0','1') #(a='8',b='8')
                            else:
                                return ('1','1') #(a='8',b='9')
                        elif (b<= '10'):
                                return ('2','1') #(a='8',b='10')
                        else:
                            return ('3','1') #(a='8',b='11')
                    elif (b<= '13'):
                        if (b<= '12'):
                                return ('4','1') #(a='8',b='12')
                        else:
                            return ('5','1') #(a='8',b='13')
                    elif (b<= '14'):
                            return ('6','1') #(a='8',b='14')
                    else:
                        return ('7','1') #(a='8',b='15')
            else:
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('9','0') #(a='9',b='0')
                            else:
                                return ('A','0') #(a='9',b='1')
                        elif (b<= '2'):
                                return ('B','0') #(a='9',b='2')
                        else:
                            return ('C','0') #(a='9',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('D','0') #(a='9',b='4')
                        else:
                            return ('E','0') #(a='9',b='5')
                    elif (b<= '6'):
                            return ('F','0') #(a='9',b='6')
                    else:
                        return ('0','1') #(a='9',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('1','1') #(a='9',b='8')
                        else:
                            return ('2','1') #(a='9',b='9')
                    elif (b<= '10'):
                            return ('3','1') #(a='9',b='10')
                    else:
                        return ('4','1') #(a='9',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('5','1') #(a='9',b='12')
                    else:
                        return ('6','1') #(a='9',b='13')
                elif (b<= '14'):
                        return ('7','1') #(a='9',b='14')
                else:
                    return ('8','1') #(a='9',b='15')
        elif (a<= '10'):
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('A','0') #(a='A',b='0')
                            else:
                                return ('B','0') #(a='A',b='1')
                        elif (b<= '2'):
                                return ('C','0') #(a='A',b='2')
                        else:
                            return ('D','0') #(a='A',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('E','0') #(a='A',b='4')
                        else:
                            return ('F','0') #(a='A',b='5')
                    elif (b<= '6'):
                            return ('0','1') #(a='A',b='6')
                    else:
                        return ('1','1') #(a='A',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('2','1') #(a='A',b='8')
                        else:
                            return ('3','1') #(a='A',b='9')
                    elif (b<= '10'):
                            return ('4','1') #(a='A',b='10')
                    else:
                        return ('5','1') #(a='A',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('6','1') #(a='A',b='12')
                    else:
                        return ('7','1') #(a='A',b='13')
                elif (b<= '14'):
                        return ('8','1') #(a='A',b='14')
                else:
                    return ('9','1') #(a='A',b='15')
        else:
            if (b<= '7'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('B','0') #(a='B',b='0')
                        else:
                            return ('C','0') #(a='B',b='1')
                    elif (b<= '2'):
                            return ('D','0') #(a='B',b='2')
                    else:
                        return ('E','0') #(a='B',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('F','0') #(a='B',b='4')
                    else:
                        return ('0','1') #(a='B',b='5')
                elif (b<= '6'):
                        return ('1','1') #(a='B',b='6')
                else:
                    return ('2','1') #(a='B',b='7')
            elif (b<= '11'):
                if (b<= '9'):
                    if (b<= '8'):
                            return ('3','1') #(a='B',b='8')
                    else:
                        return ('4','1') #(a='B',b='9')
                elif (b<= '10'):
                        return ('5','1') #(a='B',b='10')
                else:
                    return ('6','1') #(a='B',b='11')
            elif (b<= '13'):
                if (b<= '12'):
                        return ('7','1') #(a='B',b='12')
                else:
                    return ('8','1') #(a='B',b='13')
            elif (b<= '14'):
                    return ('9','1') #(a='B',b='14')
            else:
                return ('A','1') #(a='B',b='15')
    elif (a<= '13'):
        if (a<= '12'):
                if (b<= '7'):
                    if (b<= '3'):
                        if (b<= '1'):
                            if (b<= '0'):
                                    return ('C','0') #(a='C',b='0')
                            else:
                                return ('D','0') #(a='C',b='1')
                        elif (b<= '2'):
                                return ('E','0') #(a='C',b='2')
                        else:
                            return ('F','0') #(a='C',b='3')
                    elif (b<= '5'):
                        if (b<= '4'):
                                return ('0','1') #(a='C',b='4')
                        else:
                            return ('1','1') #(a='C',b='5')
                    elif (b<= '6'):
                            return ('2','1') #(a='C',b='6')
                    else:
                        return ('3','1') #(a='C',b='7')
                elif (b<= '11'):
                    if (b<= '9'):
                        if (b<= '8'):
                                return ('4','1') #(a='C',b='8')
                        else:
                            return ('5','1') #(a='C',b='9')
                    elif (b<= '10'):
                            return ('6','1') #(a='C',b='10')
                    else:
                        return ('7','1') #(a='C',b='11')
                elif (b<= '13'):
                    if (b<= '12'):
                            return ('8','1') #(a='C',b='12')
                    else:
                        return ('9','1') #(a='C',b='13')
                elif (b<= '14'):
                        return ('A','1') #(a='C',b='14')
                else:
                    return ('B','1') #(a='C',b='15')
        else:
            if (b<= '7'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('D','0') #(a='D',b='0')
                        else:
                            return ('E','0') #(a='D',b='1')
                    elif (b<= '2'):
                            return ('F','0') #(a='D',b='2')
                    else:
                        return ('0','1') #(a='D',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('1','1') #(a='D',b='4')
                    else:
                        return ('2','1') #(a='D',b='5')
                elif (b<= '6'):
                        return ('3','1') #(a='D',b='6')
                else:
                    return ('4','1') #(a='D',b='7')
            elif (b<= '11'):
                if (b<= '9'):
                    if (b<= '8'):
                            return ('5','1') #(a='D',b='8')
                    else:
                        return ('6','1') #(a='D',b='9')
                elif (b<= '10'):
                        return ('7','1') #(a='D',b='10')
                else:
                    return ('8','1') #(a='D',b='11')
            elif (b<= '13'):
                if (b<= '12'):
                        return ('9','1') #(a='D',b='12')
                else:
                    return ('A','1') #(a='D',b='13')
            elif (b<= '14'):
                    return ('B','1') #(a='D',b='14')
            else:
                return ('C','1') #(a='D',b='15')
    elif (a<= '14'):
            if (b<= '7'):
                if (b<= '3'):
                    if (b<= '1'):
                        if (b<= '0'):
                                return ('E','0') #(a='E',b='0')
                        else:
                            return ('F','0') #(a='E',b='1')
                    elif (b<= '2'):
                            return ('0','1') #(a='E',b='2')
                    else:
                        return ('1','1') #(a='E',b='3')
                elif (b<= '5'):
                    if (b<= '4'):
                            return ('2','1') #(a='E',b='4')
                    else:
                        return ('3','1') #(a='E',b='5')
                elif (b<= '6'):
                        return ('4','1') #(a='E',b='6')
                else:
                    return ('5','1') #(a='E',b='7')
            elif (b<= '11'):
                if (b<= '9'):
                    if (b<= '8'):
                            return ('6','1') #(a='E',b='8')
                    else:
                        return ('7','1') #(a='E',b='9')
                elif (b<= '10'):
                        return ('8','1') #(a='E',b='10')
                else:
                    return ('9','1') #(a='E',b='11')
            elif (b<= '13'):
                if (b<= '12'):
                        return ('A','1') #(a='E',b='12')
                else:
                    return ('B','1') #(a='E',b='13')
            elif (b<= '14'):
                    return ('C','1') #(a='E',b='14')
            else:
                return ('D','1') #(a='E',b='15')
    else:
        if (b<= '7'):
            if (b<= '3'):
                if (b<= '1'):
                    if (b<= '0'):
                            return ('F','0') #(a='F',b='0')
                    else:
                        return ('0','1') #(a='F',b='1')
                elif (b<= '2'):
                        return ('1','1') #(a='F',b='2')
                else:
                    return ('2','1') #(a='F',b='3')
            elif (b<= '5'):
                if (b<= '4'):
                        return ('3','1') #(a='F',b='4')
                else:
                    return ('4','1') #(a='F',b='5')
            elif (b<= '6'):
                    return ('5','1') #(a='F',b='6')
            else:
                return ('6','1') #(a='F',b='7')
        elif (b<= '11'):
            if (b<= '9'):
                if (b<= '8'):
                        return ('7','1') #(a='F',b='8')
                else:
                    return ('8','1') #(a='F',b='9')
            elif (b<= '10'):
                    return ('9','1') #(a='F',b='10')
            else:
                return ('A','1') #(a='F',b='11')
        elif (b<= '13'):
            if (b<= '12'):
                    return ('B','1') #(a='F',b='12')
            else:
                return ('C','1') #(a='F',b='13')
        elif (b<= '14'):
                return ('D','1') #(a='F',b='14')
        else:
            return ('E','1') #(a='F',b='15')
        return ('E','1') #(a='F',b='15')
    raise ValueError('unknown digits in ADDS3b16')
