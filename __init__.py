import os
import sys

dossier = os.path.dirname(os.path.abspath(__file__))

print(dossier)

sys.path.append(dossier)
