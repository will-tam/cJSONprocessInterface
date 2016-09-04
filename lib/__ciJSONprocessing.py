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
            key = None
            for prefix, event, value in listArgs:
                if event == "start_map":
                    theList = []
                elif event == "map_key":
                    key = value
                elif event == "end_map":
                    yield theList
                else:
                    if prefix.endswith(str(key)) :
                        theList.append((key, value))
        return extractRawReal


    def extractValueFrom(self, key, jsonDatas):
        """
        """
        print("Données provenant de ijsonRead")


if __name__ == "__main__":
    help(ClassiJSONProcessing)
