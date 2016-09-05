# -*- coding: utf-8 -*-

# Standard libraries import.
import codecs
import os

# Third libraries import.
import __cpJSONprocessing as cpyJSONProcess
import __ciJSONprocessing as ciJSONProcess

# Projet modules import.

class ClassJSONProcessInterface():
    """
    JSON various handling interface.
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
        @Return : raw-like extracted datas.
        """
        return self.__JSONProcess.extractRaw(jsonDatas)

    def extractOnlyKey(self, jsonDatas):
        """
        Extract only the keys.
        @Parameters : jsonDatas = the json's datas.
        @Return : only the keys are extracted.
        """
        return self.__JSONProcess.extractOnlyKey(jsonDatas)

    def extractValueFrom(self, key, jsonDatas):
        """
        Extract a value from a key.
        @Parameters : key = the keys to return with its datas.
                            jsonDatas = the json's datas.
        @Return : the asked key and its value.
                        If key is not exists in jsonDatas, return None.
        """
        return self.__JSONProcess.extractValueFrom(key, jsonDatas)

    def extractSeveralFrom(self, keys, jsonDatas):
        """
        Extract a values from several keys.
        @Parameters : keys = list of keys to return with their datas.
                            jsonDatas = the json's datas.
        @Return : the asked keys and their associated values.
                        If one of the "keys" is NOT exist in jsonDatas, return None.
        """
        return self.__JSONProcess.extractSeveralFrom(keys, jsonDatas)


if __name__ == "__main__":
    help(ClassJSONProcessInterface)
