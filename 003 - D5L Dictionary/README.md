# 003 D5L Dictionary

![Static Badge](https://img.shields.io/badge/python-tkinter-blue?logo=python)
![Static Badge](https://img.shields.io/badge/python-pymultidictionary-blue?logo=python)
![Static Badge](https://img.shields.io/badge/IDE-VsCode-blue)
![Static Badge](https://img.shields.io/badge/D5L-Dictionary-orange)


<img src="https://hatscripts.github.io/circle-flags/flags/uk.svg" width="24">
<img src="https://hatscripts.github.io/circle-flags/flags/tr.svg" width="24">
<img src="https://hatscripts.github.io/circle-flags/flags/fr.svg" width="24">
<img src="https://hatscripts.github.io/circle-flags/flags/cn.svg" width="24">
<img src="https://hatscripts.github.io/circle-flags/flags/ru.svg" width="24">


![Views Counter](https://views-counter.vercel.app/badge?pageId=https%3A%2F%2Fgithub%2Ecom%2Fstorlak%2FPythonMiniProjects&leftColor=000000&rightColor=0adb3f&type=total&label=Viewers&style=none)

# CONTENTS
1. [Introduction](#introduction)
2. [How to use?](#how-to-use)
3. [Roadmap](#roadmap)
4. [Known issues](#known-issues)

**********************************

## Introduction

D5L is a dictionary with 5 languages. It includes English, Turkish, French, Russian and simple Chinese.
The main goal of D5L dictionary is to find meaning, synonym and antonym of words in these 5 languages.

- D5L is written in python and includes a Tkinter.
- Searches meaning of words, synonymes, antonymes in English, Turkish, French, Russian and Chinese.
- Using PyMultiDictionary as database.
- Requirements: Tkinter, Messagebox, Pymultidictionary.
- Use help menu (F1) to contact further info.

Installing necessary modules:

```
pip install Pymultidictionary
```

## How to use?

🌟 Searching a Word

- Select first the language you want to make the search.
- Type any word in selected language in search boxes.
- Use meaning, synonym, antonym to search for the meaning, synonym or antonym of a word.
- Search button or enter key works as well.
- Use copy button to copy your search result.
- Use clear button to clear the search and the result area.
- If you have any questions or suggestions use [Disccusions](https://github.com/storlak/PythonMiniProjects/discussions)
- If the word you're looking for is not in the dictionary search result retrns ([], ",")

🌟 Avoid the following while searching!

- Don't add "s", plural in the end of the word. Search returns null.
- If you're searching a verb don't use "to". write "help" instead of "to help"

## Roadmap

- More languages to be added!
- App will be converted to .exe file for windows.
- App will be converted to flatpak and will be published in flathub repo.
- Deb package to be created.

## Known issues

- Search result in any language besides English comes first with English definition. [Issue ticket](https://github.com/storlak/PythonMiniProjects/issues/2) opened to PyMultiDictionary module.
- Tool menu items (switch language) are not functional yet.

## Contact
[![Gmail Badge](https://img.shields.io/badge/-serdartorlak-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:serdartorlak@gmail.com)](mailto:serdartorlak@gmail.com)
![Mastodon Follow](https://img.shields.io/mastodon/follow/111266776829036638?style=flat&logo=mastodon&color=blue)
[![Twitter Badge](https://img.shields.io/badge/-@serdartorlak-1ca0f1?style=flat&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/serdartorlak)](https://twitter.com/serdartorlak)


