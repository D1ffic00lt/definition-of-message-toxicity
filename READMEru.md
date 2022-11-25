# Модель машинного обучения для определения токсичности
[![Code Size](https://img.shields.io/github/languages/code-size/D1ffic00lt/definition-of-message-toxicity)](https://github.com/D1ffic00lt/definition-of-message-toxicity)
 
[English](README.md) | [Русский](READMEru.md) | [Español](READMEes.md)
 
Данная модель предназначена для определения уровня токсичности предложений на русском и английском языках.
## Описание файлов и папок
Имя файла или папки  | Содержимое файла или папки
----------------|----------------------
[EnglishToxicModel](EnglishToxicModel) | Папка с кодом для создания модели для английских слов
[EnglishToxicModel/EnglishModel.bf](EnglishToxicModel/EnglishModel.bf) | Окончательная модель для английского языка
[EnglishToxicModel/EnglishVectorizer.bf](EnglishToxicModel/EnglishVectorizer.bf) | Окончательный векторизатор для английского языка
[EnglishToxicModel/EnglishToxicModel.ipynb](EnglishToxicModel/EnglishToxicModel.ipynb) | Блокнот для обучения модели
[EnglishToxicModel/labeledEN.csv](EnglishToxicModel/labeledEN.csv) | Данные для обучения
[RussianToxicModel](RussianToxicModel) | Папка с кодом для создания модели для изучения русских слов
[RussianToxicModel/RussianModel.bf](RussianToxicModel/RussianModel.bf) | Окончательная модель для русского языка
[RussianToxicModel/RussianVectorizer.bf](RussianToxicModel/RussianVectorizer.bf) | Окончательный векторизатор для русского языка
[RussianToxicModel/RussianToxicModel.ipynb](RussianToxicModel/RussianToxicModel.ipynb) | Блокнот для обучения модели
[RussianToxicModel/labeledEN.csv](RussianToxicModel/labeledEN.csv) | Данные для обучения
[ModelLibrary](ModelLibrary) | Папка с готовым кодом модели
[ModelLibrary/models](ModelLibrary/models) | Папка с моделями и векторизаторами
[ModelLibrary/models/EnglishModel.bf](ModelLibrary/models/EnglishModel.bf) | Английская модель
[ModelLibrary/models/RussianModel.bf](ModelLibrary/models/RussianModel.bf) | Русская модель
[ModelLibrary/models/EnglishVectorizer.bf](ModelLibrary/models/EnglishVectorizer.bf) | Английский векторизатор
[ModelLibrary/models/RussianVectorizer.bf](ModelLibrary/models/RussianVectorizer.bf) | Русский векторизатор
[ModelLibrary/predict.py](ModelLibrary/predict.py) | Код предиктора токсичности
[requirements.txt](requirements.txt) | Файл библиотеки

# Пример использования программы
```Python
import pickle
from ModelLibrary.predict import get_toxicity

with open("ModelLibrary/models/EnglishModel.bf", "rb") as EnglishModel,
        open("ModelLibrary/models/RussianModel.bf", "rb") as RussianModel:
    models_ = [pickle.load(RussianModel), pickle.load(EnglishModel)]

with open("ModelLibrary/models/RussianVectorizer.bf", "rb") as RussianVectorizer,
        open("ModelLibrary/models/EnglishVectorizer.bf", "rb") as EnglishVectorizer:
    vectorizers_ = [pickle.load(RussianVectorizer), pickle.load(EnglishVectorizer)]

print(get_toxicity("ПРИВЕТ КАК ДЕЛА?", models=models_, vectorizers=vectorizers_))

```

# Более простой способ использования программы
Мною был написан и опубликован код для модуля PyPi
## Установка

`pip install toxicityclassifier`

[PyPi](https://pypi.org/project/toxicityclassifier/) |
[Source](https://github.com/D1ffic00lt/toxicity-classification-module) |
[Releases](https://github.com/D1ffic00lt/toxicity-classification-module/releases)
## Пример использования
```python
from toxicityclassifier import *

classifier = ToxicityClassificator()

print(classifier.predict(text))          # (0 или 1, вероятность)
print(classifier.get_probability(text))  # вероятность
print(classifier.classify(text))         # 0 или 1
```

## Веса
Вес для классификации (если вероятность >= weight => 1, иначе 0)
```python
classifier.weight = 0.5
```
\
Вес для определения языка (английский или русский)

если процент русского языка >= language_weight, то используется русская модель, иначе английская
```python
classifier.language_weight = 0.5
```
