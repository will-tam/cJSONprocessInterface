#!/usr/bin/python3
# -*- coding: utf-8 -*-

def extractGenDeco(function):
    def decoFunc(args):
        print("type de args : {0} ; args = {1}".format(type(args), args))
        for a in args:
            print("a =", a)
            yield a

    return decoFunc

@extractGenDeco
def extractGen(l):
    pass

if __name__ == "__main__":
    thisList= ["Stars", "think", 13, 2, 8, 4, "buup", 6]

    extracted = extractGen(thisList)
    print("type extracted : {0} ; extracted = {1}".format(type(extracted), extracted))

    for e in extracted:
        print("e =", e)
