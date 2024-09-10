from transformers import pipeline
import copy
import random

import nltk
nltk.download('punkt_tab')
nltk.download('punkt') 
from nltk.tokenize import sent_tokenize

def TF_QAG(text):
    false_pipe = pipeline("text2text-generation",model=r"TF\models\TF_false_QG")
    true_pipe = pipeline("text2text-generation",model=r"TF\models\TF_true_QG")

    # Divide text into passages with 3-5 sentences
    sentences = sent_tokenize(text)

    if len(sentences)>=3:
        passages = []
        sentences_left = copy.copy(sentences)
        while True:
            if len(sentences_left)>=6:
                passage = ' '.join(sentences_left[:3]).strip()
                passages.append(passage)
                sentences_left = sentences_left[3:]
            else:
                passage = ' '.join(sentences_left).strip()
                if passage!='':
                    passages.append(passage)
                break
        
        # Make a list of QAG based on number of passages
        QAG_list = []
        for passage in passages:
            # Randomly choose to create a True or False statement
            statement_type = random.choice([False, True])
            if statement_type == False:
                statement = false_pipe(passage)[0]['generated_text']
            elif statement_type == True:
                statement = true_pipe(passage)[0]['generated_text']
                
            QAG_list.append({"statement" : statement,
                                "answer" : statement_type})

        return QAG_list
    
    else:
        return None
    

# print(TF_QAG("""Kenrick Reginald Hijmans Johnson (10 September 1914 – 8 March 1941), known as Ken "Snakehips" Johnson, was a swing band-leader and dancer. He was a leading figure in black British music of the 1930s and early 1940s before his death while performing at the Café de Paris, London, when it was hit by a German bomb in the Blitz during the Second World War.

# Johnson was born in Georgetown, British Guiana (present-day Guyana). He showed some musical ability, but his early interest in a career in dancing displeased his father, who wished him to study medicine. He was educated in Britain, but instead of continuing on to university, he travelled to New York, perfecting dance moves and immersing himself in the vibrant jazz scene in Harlem. Tall and elegant, he modelled himself professionally on Cab Calloway. He returned to Britain and set up the Aristocrats (or Emperors) of Jazz, a mainly black swing band, with Leslie Thompson, a Jamaican musician. In 1937 he took control of the band through a legal loophole, resulting in the departure of Thompson and several musicians. Johnson filled the vacancies with musicians from the Caribbean; the band's popularity grew and its name changed to the West Indian Dance Orchestra.

# From 1938 the band started broadcasting on BBC Radio, recorded their first discs and appeared in an early television broadcast. Increasingly popular, they were employed as the house band at the Café de Paris, an upmarket and fashionable nightclub located in a basement premises below a cinema. A German bombing raid on London in March 1941 hit the cinema, killing at least 34 and injuring dozens more. Johnson and one of the band's saxophonists were among those killed; several other band members were injured."""))