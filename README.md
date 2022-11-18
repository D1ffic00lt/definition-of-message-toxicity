# Machine learning model for toxicity determination
[![Code Size](https://img.shields.io/github/languages/code-size/D1ffic00lt/definition-of-message-toxicity)](https://github.com/D1ffic00lt/definition-of-message-toxicity)

[English](README.md) | [Русский](READMEru.md) | [Español](READMEes.md)

This model is designed to determine the level of toxicity of sentences in Russian and English.
## Description of files and folders
File or folder name  | Contents of a file or folder
----------------|----------------------
[EnglishToxicModel](EnglishToxicModel) | Folder with code for creating a model for learning in English words
[EnglishToxicModel/EnglishModel.bf](EnglishToxicModel/EnglishModel.bf) | Final Model for English
[EnglishToxicModel/EnglishVectorizer.bf](EnglishToxicModel/EnglishVectorizer.bf) | Final vectorizer for English
[EnglishToxicModel/EnglishToxicModel.ipynb](EnglishToxicModel/EnglishToxicModel.ipynb) | Model training notebook
[EnglishToxicModel/labeledEN.csv](EnglishToxicModel/labeledEN.csv) | Data for training
[RussianToxicModel](RussianToxicModel) | Folder with code for creating a model for learning in Russian words
[RussianToxicModel/RussianModel.bf](RussianToxicModel/RussianModel.bf) | Final Model for Russian
[RussianToxicModel/RussianVectorizer.bf](RussianToxicModel/RussianVectorizer.bf) | Final vectorizer for Russian
[RussianToxicModel/RussianToxicModel.ipynb](RussianToxicModel/RussianToxicModel.ipynb) | Model training notebook
[RussianToxicModel/labeledEN.csv](RussianToxicModel/labeledEN.csv) | Data for training
[ModelLibrary](ModelLibrary) | Folder with ready model code
[ModelLibrary/models](ModelLibrary/models) | Folder with models and vectorizers
[ModelLibrary/models/EnglishModel.bf](ModelLibrary/models/EnglishModel.bf) | English model
[ModelLibrary/models/RussianModel.bf](ModelLibrary/models/RussianModel.bf) | Russian model
[ModelLibrary/models/EnglishVectorizer.bf](ModelLibrary/models/EnglishVectorizer.bf) | English vectorizer
[ModelLibrary/models/RussianVectorizer.bf](ModelLibrary/models/RussianVectorizer.bf) | Russian vectorizer
[ModelLibrary/predict.py](ModelLibrary/predict.py) | Toxicity predictor code
[requirements.txt](requirements.txt) | Libraries file 

# An example of using the program
```Python
import pickle
from ModelLibrary.predict import get_toxicity

with open("ModelLibrary/models/EnglishModel.bf", "rb") as EnglishModel,
        open("ModelLibrary/models/RussianModel.bf", "rb") as RussianModel:
    models_ = [pickle.load(RussianModel), pickle.load(EnglishModel)]

with open("ModelLibrary/models/RussianVectorizer.bf", "rb") as RussianVectorizer,
        open("ModelLibrary/models/EnglishVectorizer.bf", "rb") as EnglishVectorizer:
    vectorizers_ = [pickle.load(RussianVectorizer), pickle.load(EnglishVectorizer)]

print(get_toxicity("ПРИВЕТ КАК ДЕЛА&", models=models_, vectorizers=vectorizers_))

```
