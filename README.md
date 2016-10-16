2 ways to read a .json files through one interface cJSONprocessInterface.py

One way, the datas come in one-block in memory, using the python3 json library (__cpJSONprocessing.py).
The second way,the datas come iteratively from the file, using the ijson library (__ciJSONprocessing.py) : https://pypi.python.org/pypi/ijson/

First read and parse a json's datas file or other with jsonRead().
The result can be proccess with the functions below.

The values which can be extracted :
  - all the datas as list format from the json's datas with extractRaw()
  - all the keys only from a json's datas with extractOnlyKey()
  - only one value form its giving key with extractValueFrom()
  - several values from the list of their keys with extractSeveralFrom()

