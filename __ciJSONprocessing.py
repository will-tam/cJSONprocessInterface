# -*- coding: utf-8 -*-

# Standard libraries import.
import codecs

# Third libraries import.
import ijson            # https://pypi.python.org/pypi/ijson/

# Projet modules import.

class ClassiJSONProcessing():
    """
    iJSON various handling interface.

    Public attributs :
        self.jsonDatas = datas after parsing. It's a ijson datas.
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
        Open and read the .json file in interating mode.
        @Parameters : jsonStream = the .json file name or json datas stream.
        @Return : the json datas generator. If problem, return False.
        """
        try:
            fp = codecs.open(jsonStream, "r", "utf-8")
            return ijson.parse(fp)
        except FileNotFoundError as e:
            print(e)
            return False

    def extractRaw(self, jsonDatas):
        """
        Extract the datas as-is.
        @Parameters : jsonDatas = the json's datas.
        @Return : the result of the closure extractRawFake().
        """
        key = None
        for prefix,  event, value in jsonDatas:
            if event == "start_map":
                theList = []
            elif event == "map_key":
                key = value
            elif event == "end_map":
                yield theList
            else:
                if prefix.endswith(str(key)) :
                    theList.append((key, value))

    def extractOnlyKey(self, jsonDatas):
        """
        Extract only the keys.
        @Parameters : jsonDatas = the json's datas.
        @Return : the result of the closure extractRawFake().
        """
        keys = []
        for datas in self.extractRaw(jsonDatas):        # Using of the iterative datas extraction before.
            keys = [k[0] for k in datas]
            yield keys

    def extractValueFrom(self, key, jsonDatas):
        """
        Extract a value from a key.
        @Parameters : key = the key to return with its datas.
                            jsonDatas = the json's datas.
        @Return : the result of the closure extractRawFake().
                        If "key" is NOT exist in jsonDatas, return None.
        """
        try:
            for datas in self.extractRaw(jsonDatas):
                yield [(k, v) for k, v in datas if k == key][0]        # Take the first element only of the list
        except IndexError:
            yield None

    def extractSeveralFrom(self, keys, jsonDatas):
        """
        Extract a values from several keys.
        @Parameters : keys = list of keys to return with their datas.
                            jsonDatas = the json's datas.
        @Return : the result of the closure extractRawFake().
                        If one of the "keys" is NOT exist in jsonDatas, return None.
        """
        try:
            for datas in self.extractRaw(jsonDatas):
                data = []
                for key in keys:
                    data.append([(k, v) for k, v in datas if k == key][0])    # Take the first element only of the list
                yield data
        except IndexError:
            yield None

if __name__ == "__main__":
    help(ClassiJSONProcessing)
