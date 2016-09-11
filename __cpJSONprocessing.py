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

    def  extractRaw(self, jsonDatas):
        """
        Generator : extract the datas as-is.
        @Parameters : jsonDatas = the json's datas.
        @Return : generate the raw-like extracted datas.
        """
        for data in jsonDatas:
            yield data

    def extractOnlyKey(self, jsonDatas):
        """
        Generator : extract only the keys.
        @Parameters : jsonDatas = the json's datas.
        @Return : only the keys are generated.
        """
        for datas in jsonDatas:
            keys = [k[0] for k in datas]
            yield keys

    def extractValueFrom(self, key, jsonDatas):
        """
        Generator : extract a value from a key.
        @Parameters : key = the key to return with its datas.
                            jsonDatas = the json's datas.
        @Return : generate the asked key and its value.
                        If "key" is NOT exist in jsonDatas, return None.
        """
        try:
            for datas in jsonDatas:
                yield [(k, v) for k, v in datas if k == key][0]        # Take the first element only of the list
        except IndexError:
            yield None

    def extractSeveralFrom(self, keys, jsonDatas):
        """
        Generator : extract a values from several keys.
        @Parameters : keys = list of keys to return with their datas.
                            jsonDatas = the json's datas.
        @Return : generate the asked keys and their associated values.
                        If one of the "keys" is NOT exist in jsonDatas, return None.
        """
        try:
            for datas in jsonDatas:
                data = []
                for key in keys:
                    data.append([(k, v) for k, v in datas if k == key][0])    # Take the first element only of the list
                yield data
        except IndexError:
            yield None


if __name__ == "__main__":
    help(ClasspJSONProcessing)
