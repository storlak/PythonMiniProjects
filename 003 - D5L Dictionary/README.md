# 003 D5L Dictionary

![Static Badge](https://img.shields.io/badge/python-tkinter-blue?logo=python)
![Static Badge](https://img.shields.io/badge/python-pymultidictionary-blue?logo=python)
![Static Badge](https://img.shields.io/badge/IDE-VsCode-blue)
![Static Badge](https://img.shields.io/badge/D5L-Dictionary-orange)

<img src="https://hatscripts.github.io/circle-flags/flags/uk.svg" width="24"> <img src="https://hatscripts.github.io/circle-flags/flags/tr.svg" width="24"> <img src="https://hatscripts.github.io/circle-flags/flags/fr.svg" width="24"> <img src="https://hatscripts.github.io/circle-flags/flags/cn.svg" width="24"> <img src="https://hatscripts.github.io/circle-flags/flags/ru.svg" width="24">

![Views Counter](https://views-counter.vercel.app/badge?pageId=https%3A%2F%2Fgithub%2Ecom%2Fstorlak%2FPythonMiniProjects&leftColor=000000&rightColor=0adb3f&type=total&label=Viewers&style=none)

# CONTENTS

1. [Introduction](#introduction)
2. [How to Install?](#how-to-install)
3. [How to use?](#how-to-use)
4. [Roadmap](#roadmap)
5. [Known issues](#known-issues)
6. [Contact & Forum & Wiki](#contact)

---

## Introduction

D5L is a dictionary with 5 languages. It includes English, Turkish, French, Russian, and Simplified Chinese. The main goal of D5L dictionary is to find the meaning, synonym, and antonym of words in these 5 languages.

- D5L is written in Python and includes Tkinter.
- Searches meaning of words, synonyms, antonyms in English, Turkish, French, Russian, and Chinese.
- Using PyMultiDictionary as the database.
- Requirements: Tkinter, Messagebox, Pymultidictionary.
  -Use the help menu (F1) to have more information and support.

## How to Install

You can install D5L in various ways:

- Fork the repository to your GitHub and run main.py.
- Download the .exe file for Windows (coming soon!).
- Install via Flathub for Linux (coming soon!).
- Download the .deb file for Linux (coming soon!).
- Download main.py, constants.py, gui_utils.py, and menu_utils.py, and run main.py.
  - main.py for English.
  - main_fr.py for French (not functional yet).
  - main_ru.py for Russian (not functional yet).
  - main_ch.py for Chinese (not functional yet).
  - main_tr.py for Turkish (not functional yet).

Installing necessary modules:

```
pip install Pymultidictionary
```

## How to use?

🌟 Searching a Word

- Select the language you want to search first.
- Type any word in the selected language into the search boxes.
- Use "meaning," "synonym," or "antonym" to search for the meaning, synonym, or antonym of a word.
- The search button or Enter key works as well.
- Use the copy button to copy your search result.
- Use the clear button to clear the search and the result area.
- If you have any questions or suggestions, use [Disccusions](https://github.com/storlak/PythonMiniProjects/discussions).
- If the word you're looking for is not in the dictionary, the search result returns ([], ",").

🌟 Avoid the following while searching!

- Don't add "s" at the end of the word. Searches return null.
- If you're searching for a verb, don't use "to". Write "help" instead of "to help".

## Roadmap

- More languages will be added!
- Keyboard shortcuts - uick commands will be revised.
- The app will be converted to an .exe file for Windows.
- The app will be converted to Flatpak and published in the Flathub repository.
- A Deb package will be created.
- AppImage will be created.

## Known issues

- Search results in any language besides English come first with the English definition. An issue ticket has been opened to the PyMultiDictionary module. You can view it [here](https://github.com/storlak/PythonMiniProjects/issues/2).
- Tool menu items (switch language) are not functional yet.

## Contact

[![Gmail Badge](https://img.shields.io/badge/-serdartorlak-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:serdartorlak@gmail.com)](mailto:serdartorlak@gmail.com)
![Mastodon Follow](https://img.shields.io/mastodon/follow/111266776829036638?style=flat&logo=mastodon&color=blue)
[![Twitter Badge](https://img.shields.io/badge/-@serdartorlak-1ca0f1?style=flat&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/serdartorlak)](https://twitter.com/serdartorlak)
