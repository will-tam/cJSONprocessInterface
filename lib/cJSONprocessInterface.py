# -*- coding: utf-8 -*-

# Standard libraries import.
import codecs

# Third libraries import.
import lib.__cpJSONprocessing as cpyJSONProcess
import lib.__ciJSONprocessing as ciJSONProcess

# Projet modules import.

class ClassJSONProcessInterface():
    """
    JSON various handling interface.

    Public attributes :
        self.jsonDatas = datas after parsing. It's a simple json datas OR ijson datas.
    """

    # Private attributes:
    # self.__iterate = False to read as Python JSON lib's way, True to read as iJSONlib's way.
    # self.__JSONProcess  = the JSON processing class choosed. Depend of self.__iterate.

    def __init__(self, iterate=False):
        """
        __init__ : constructeur
        @paramètres : iterate = how to read json's datas.
        @retour : none.
        """
        choice = {True : ciJSONProcess.ClassiJSONProcessing(),
                         False : cpyJSONProcess.ClasspJSONProcessing()}

        self.jsonDatas = None
        self.__iterate = iterate
        self.__JSONProcess  = choice[self.__iterate]

    def jsonRead(self, jsonStream):
        """
        Open and read the .json file.
        @Parameters : jsonStream = the .json file name or json datas stream.
        @Return : the json datas. If problem, return False.
        """
        return self.__JSONProcess.jsonRead(jsonStream)

    def extractRaw(self, jsonDatas):
        """
        Extract the datas as-is.
        @Parameters : jsonDatas = the json's datas.
        @Return : the result of the closure extractRawFake().
        """
        return self.__JSONProcess.extractRaw(jsonDatas)

    def extractOnlyKey(self, jsonDatas):
        """
        Extract only the keys.
        @Parameters : jsonDatas = the json's datas.
        @Return : the result of the closure extractRawFake().
        """
        return self.__JSONProcess.extractOnlyKey(jsonDatas)

    def extractValueFrom(self, key, jsonDatas):
        if isinstance(jsonDatas, list):
            print("Données provenant de jsonRead")
        else:
            print("Données provenant de ijsonRead")


if __name__ == "__main__":
    help(ClassJSONProcessInterface)
