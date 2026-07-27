# PCS-politically-correct-scraper
A project to collect candidate provided information consistently and compare it against other trusted sources when possible

## Project Architecture
The information and results from the previous step will feed into the other

Sources -> Crawler -> Content Storage/Extraction -> Normalization/Validation -> Report

* Sources: Where the candidate information will originate from
* Crawler: Will get raw HTML content from the sources, it contain the selenium/bs4+requests driver 
* Content Storage: store raw content obtained from crawler
* Content Extraction: Extract relevant information from storage
* Normalization: Compare and contrast data from each candidate and organize it for consistency purposes
* Validation: Check data against verified sources for accuracy, when possible
* Report: Format and export data to interested parties

## Environment Information
Visual Studio Code info:
* Version: 1.130.0 (user setup)
* Commit: 1b6a188127eeaf9194f945eb6eb89a657e93c54c
* Date: 2026-07-22T14:55:04Z
* Electron: 42.6.0
* ElectronBuildId: 14623276
* Chromium: 148.0.7778.280
* Node.js: 24.18.0
* V8: 14.8.178.38-electron.0
* OS: Windows_NT x64 10.0.26200

Development Language Python 3.14

Sources Referenced: [Insert Link](https://www.google.com/)