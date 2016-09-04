# -*- coding: utf-8 -*-

# Standard libraries import.
import json
import codecs

# Third libraries import.

# Projet modules import.

class ClasspJSONProcessing():
    """
    Python JSON various handling interface.

    Public attributs :
        self.jsonDatas = datas after parsing. It's a simple json datas.
    """

    def __init__(self):
        """
        __init__ : constructeur
        @paramètres : none.
        @retour : none.
        """
        self.jsonDatas = None

    def jsonRead(self, jsonStream):
        """
        Open and read the .json file.
        @Parameters : jsonStream = the .json file name or json datas stream.
        @Return : the json datas. If problem, return False.
        """
        try:
            with codecs.open(jsonStream, "r", "utf-8") as fp:
                # https://docs.python.org/3.3/library/json.html?highlight=json#json-to-py-table
                #https://www.daniweb.com/programming/software-development/threads/497014/
                #                                        attributeerror-str-object-has-no-attribute-keys
                jsonDatas = json.load(fp, object_pairs_hook=lambda obj : obj)
            return jsonDatas
        except FileNotFoundError as e:
            print(e)
            return False
        except ValueError as e:
            print(e)
            return False

    def extractRaw(self, functionExtractRaw):
        """
        Decorator of extractRaw.
        @Parameters : functionExtractRaw = extractRaw function it-self.
        @Return : the yield of closure extractRawReal.
        """
        def extractRawReal(listArgs):
            """
            The really be runned generator datas extractor.
            @Parameters : listArgs = extractRaw arguments them-self.
            @Return : yield the extracted element.
            """
            for element in listArgs:
                yield element
        return extractRawReal


    def extractValueFrom(self, key, jsonDatas):
        print("Données provenant de pjsonRead")
        print(type(jsonDatas))


if __name__ == "__main__":
    help(ClasspJSONProcessing)
