# ChatGpt Test Case Creator

A tool to create test cases for Azure ADO using ChatGPT.

## Purpose
The ChatGpt Test Case Creator is designed to assist users in generating test cases for Azure ADO (Azure DevOps) using ChatGPT, an AI language model. It automates the process of creating test cases based on software documentation, making it easier and more efficient for testing teams.

## Prerequisites
Before running the tool, make sure you have the following:

An account on ChatGPT
"Save ChatGPT" extension installed
Python installed
Regex module installed (you can install it using pip install regex)

## Usage
Follow these steps to use the ChatGpt Test Case Creator:

1- Install the prerequisites as mentioned above.
2- Open ChatGpt and copy the prompt from "Prompt.txt".
3- Add the relevant software documentation to the prompt. The more granular the documentation, the better the results.

*Note: You can also copy content from a text file to paste it into ChatGpt. Refer to this tutorial for more details: https://www.youtube.com/watch?v=vB8Vz7hFAQQ*

4- After finishing, click on the "Save ChatGpt" extension and save the output as a text file.
5- Open Txt_To_Csv.py and set the path for your input text file and the desired output CSV file.
6- Open the CSV file in Excel and copy the content.
7- In Azure ADO, open Test Plans and click on "Add test case using grid".

![image](https://user-images.githubusercontent.com/13317539/232628586-a6dd26a0-e9e4-4cf7-9c1c-6253ac7ccd7e.png)

8- Paste the content on the grid and save.

![image](https://user-images.githubusercontent.com/13317539/232628688-af4ff94b-50e7-49fd-98a1-f751e766f3b2.png)

## Limitations
ChatGPT is an AI assistant and may not always generate perfect results.
The accuracy of the generated test cases depends on the quality and granularity of the software documentation used as input.
Users should thoroughly review and validate the test cases before using them in their testing process.
By following these steps and considering the limitations, you can leverage the ChatGpt Test Case Creator tool to efficiently generate test cases for Azure ADO based on software documentation.
