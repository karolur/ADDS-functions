def ADDS3(a, b):
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
    raise ValueError('unknown digits in ADDS3')
