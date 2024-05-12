import streamlit as st

from transformers import pipeline

def load_llm(model_name):
    
    summarizer = pipeline("summarization", model=model_name)
    
    return summarizer
    
model_name = "Falconsai/text_summarization"

texts = {"":"",
         "A Study in Scarlet":"In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there, I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon. The regiment was stationed in India at the time, and before I could join it, the second Afghan war had broken out. On landing at Bombay, I learned that my corps had advanced through the passes, and was already deep in the enemy's country. I followed, however, with many other officers who were in the same situation as myself, and succeeded in reaching Candahar in safety, where I found my regiment, and at once entered upon my new duties. The campaign brought honours and promotion to many, but for me it had nothing but misfortune and disaster. I was removed from my brigade and attached to the Berkshires, with whom I served at the fatal battle of Maiwand. There I was struck on the shoulder by a Jezail bullet, which shattered the bone and grazed the subclavian artery. I should have fallen into the hands of the murderous Ghazis had it not been for the devotion and courage shown by Murray, my orderly, who threw me across a pack-horse, and succeeded in bringing me safely to the British lines. Worn with pain, and weak from the prolonged hardships which I had undergone, I was removed, with a great train of wounded sufferers, to the base hospital at Peshawar. Here I rallied, and had already improved so far as to be able to walk about the wards, and even to bask a little upon the verandah, when I was struck down by enteric fever, that curse of our Indian possessions.",
         "Twenty Thousand Leagues under the Sea":"The year 1866 was signalised by a remarkable incident, a mysterious and puzzling phenomenon, which doubtless no one has yet forgotten. Not to mention rumours which agitated the maritime population and excited the public mind, even in the interior of continents, seafaring men were particularly excited. Merchants, common sailors, captains of vessels, skippers, both of Europe and America, naval officers of all countries, and the Governments of several states on the two continents, were deeply interested in the matter. For some time past, vessels had been met by 'an enormous thing,' a long object, spindle-shaped, occasionally phosphorescent, and infinitely larger and more rapid in its movements than a whale. The facts relating to this apparition (entered in various log-books) agreed in most respects as to the shape of the object or creature in question, the untiring rapidity of its movements, its surprising power of locomotion, and the peculiar life with which it seemed endowed. If it was a cetacean, it surpassed in size all those hitherto classified in science. Taking into consideration the mean of observations made at divers times,—rejecting the timid estimate of those who assigned to this object a length of two hundred feet, equally with the exaggerated opinions which set it down as a mile in width and three in length,—we might fairly conclude that this mysterious being surpassed greatly all dimensions admitted by the ichthyologists of the day, if it existed at all. And that it did exist was an undeniable fact; and, with that tendency which disposes the human mind in favour of the marvellous, we can understand the excitement produced in the entire world by this supernatural apparition. As to classing it in the list of fables, the idea was out of the question. On the 20th of July, 1866, the steamer Governor Higginson, of the Calcutta and Burnach Steam Navigation Company, had met this moving mass five miles off the east coast of Australia. Captain Baker thought at first that he was in the presence of an unknown sandbank; he even prepared to determine its exact position, when two columns of water, projected by the inexplicable object, shot with a hissing noise a hundred and fifty feet up into the air. Now, unless the sandbank had been submitted to the intermittent eruption of a geyser, the Governor Higginson had to do neither more nor less than with an aquatic mammal, unknown till then, which threw up from its blow-holes columns of water mixed with air and vapour."
         "Pride and prejudice":"It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighborhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters. 'My dear Mr. Bennet,' said his lady to him one day, 'have you heard that Netherfield Park is let at last?' Mr. Bennet replied that he had not. 'But it is,' returned she, 'for Mrs. Long has just been here, and she told me all about it.' Mr. Bennet made no answer. 'Do you not want to know who has taken it?' cried his wife, impatiently. 'You want to tell me, and I have no objection to hearing it.' This was invitation enough. 'Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise-and-four to see the place, and was so much delighted with it that he agreed with Mr. Morris immediately; that he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week.' 'What is his name?' 'Bingley.' 'Is he married or single?' 'Oh, single, my dear, to be sure! A single man of large fortune—four or five thousand a year. What a fine thing for our girls!' 'How so? How can it affect them?' 'My dear Mr. Bennet,' replied his wife, 'how can you be so tiresome? You must know that I am thinking of his marrying one of them.' 'Is that his design in settling here?' 'Design? nonsense, how can you talk so! But it is very likely that he may fall in love with one of them, and therefore you must visit him as soon as he comes."
        }
         
# Page title 
st.set_page_config(page_title='🧩 Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.title('Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.markdown('*Lucía Méndez López - lmendez31786@alumnos.uemc.es*')

st.sidebar.divider()

option = st.sidebar.selectbox(
    "Textos de referencia para resumir",
    ("", "A Study in Scarlet", "Twenty Thousand Leagues under the Sea"))

st.header('🧩 Applicación para resumen de textos 🧩')

col1, col2 = st.columns(2)

# Text input
col1.subheader('Introduce tu texto aquí')
txt_input = col1.text_area('', texts[option], height=400)

# Form to accept user's text input for summarization
result = []
with st.form('summarize_form', clear_on_submit=False):
    submitted = st.form_submit_button('Submit')
    #if submitted and openai_api_key.startswith('sk-'):
    if submitted:
        with st.spinner('Transformando 🤘'):
            summarizer = load_llm(model_name)
            response = summarizer(txt_input, max_length=300, min_length=30, do_sample=True)
            resumen = response[0]['summary_text']
            result.append(resumen)

if len(result):
    col2.subheader('Tu texto resumido aquí')
    col2.info(result[0])
