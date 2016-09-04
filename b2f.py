#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Standard libraries import.
import sys

# Third libraries import.

# Projet modules import.
import lib.cJSONprocessInterface as cJSONProcessInterface

######################

def main(arg):
    """
    Main function.
    @Param : some arguments, in case of use.
    @Return : 0 = all was good.
              ... = some problem occures.
    """
    ITEMS_JSON = "items.json"
    ITERATE = False
    ITERATE = True

    json = cJSONProcessInterface.ClassJSONProcessInterface(ITERATE)
    jsonDatas = json.jsonRead(ITEMS_JSON)

    extracted = json.extractRaw(jsonDatas)
    print("type extracted :", type(extracted))

    if not extracted:
        print ("extracted n'est ni list ni generator !!")
        return 1

    a = iter(extracted)
    goOn = True if a else Fale

    while goOn:
        try:
            print(next(a))
            input()
        except StopIteration:
            goOn = False
        except KeyboardInterrupt:
            goOn = False

    #jsonDatas = items.jsonRead(ITEMS_JSON)
    #print(jsonDatas)

    #ijsonDatas = items.ijsonRead(ITEMS_JSON)
    #for ijsonData in ijsonDatas:
        #print(ijsonData)

    #print(items.extractRaw(ijsonDatas))

    #print(items.extractValueFrom("id", jsonDatas))


    return 0

######################

if (__name__ == "__main__"):
    rc = main(sys.argv[1:])      # Keep only the after script name arguments.
    sys.exit(rc)
