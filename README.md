# AutoQuiz

## Intro
This project is aimed to help students and teachers. After reading the text just pass it to my bot and it will give you a quick quiz to check your knowledge.

## Description
There are 3 types of questions which will be generated based on provided text.

- True/False (TF)
- Multiple Choice (MC)
- Fill-in-the-blank (FB)

#### Preparing dataset with "passages"
To generate quesionts and answers I needed a dataset with random stories and I've taken this ["glnmario/news-qa-summarization"](https://huggingface.co/datasets/glnmario/news-qa-summarization). I kept only one column with stories, splitted each story into shorter texts with 3-5 sentences and kept only "short_texts" which were in range between 350 and 1000 symbols. I did it to remove outliers and in the deployed version the given text to chatBOT will be splitted to passages and for each passage there will be a generated question and answer. Finally I got around 50k passages.

#### True/False
To fine-tune model for generating true/false statement about the passage I've divided dataset with passages in half. One half of passages I've used to generate true statements and another one for false statements. The statements were generated using Groq API, provider of the fastest inference models with almost no request limit if you iterate provided models... As a result I got 2 fine-tuned t5-small models for generating different types of statements.


## Deployment 
[Streamlit Cloud](https://nikitazuevblago-autoquiz-quizgui-xpgudz.streamlit.app/)

## Technologies Used

- streamlit
- transformers
- Groq API

## Result 
ChatBot for automatic quiz creation. 
