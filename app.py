import streamlit as st

from transformers import pipeline

def load_llm(model_name):
    
    summarizer = pipeline("summarization", model=model_name)
    
    return summarizer
    
model_name = "Falconsai/text_summarization"

texts = {"":"",
         "A Study in Scarlet":"In the year 1878 I took my degree of Doctor of Medicine of the University of London, and proceeded to Netley to go through the course prescribed for surgeons in the army. Having completed my studies there, I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon. The regiment was stationed in India at the time, and before I could join it, the second Afghan war had broken out. On landing at Bombay, I learned that my corps had advanced through the passes, and was already deep in the enemy's country. I followed, however, with many other officers who were in the same situation as myself, and succeeded in reaching Candahar in safety, where I found my regiment, and at once entered upon my new duties. The campaign brought honours and promotion to many, but for me it had nothing but misfortune and disaster. I was removed from my brigade and attached to the Berkshires, with whom I served at the fatal battle of Maiwand. There I was struck on the shoulder by a Jezail bullet, which shattered the bone and grazed the subclavian artery. I should have fallen into the hands of the murderous Ghazis had it not been for the devotion and courage shown by Murray, my orderly, who threw me across a pack-horse, and succeeded in bringing me safely to the British lines. Worn with pain, and weak from the prolonged hardships which I had undergone, I was removed, with a great train of wounded sufferers, to the base hospital at Peshawar. Here I rallied, and had already improved so far as to be able to walk about the wards, and even to bask a little upon the verandah, when I was struck down by enteric fever, that curse of our Indian possessions.",
         "Twenty Thousand Leagues under the Sea":"The year 1866 was signalised by a remarkable incident, a mysterious and puzzling phenomenon, which doubtless no one has yet forgotten. Not to mention rumours which agitated the maritime population and excited the public mind, even in the interior of continents, seafaring men were particularly excited. Merchants, common sailors, captains of vessels, skippers, both of Europe and America, naval officers of all countries, and the Governments of several states on the two continents, were deeply interested in the matter. For some time past, vessels had been met by 'an enormous thing,' a long object, spindle-shaped, occasionally phosphorescent, and infinitely larger and more rapid in its movements than a whale. The facts relating to this apparition (entered in various log-books) agreed in most respects as to the shape of the object or creature in question, the untiring rapidity of its movements, its surprising power of locomotion, and the peculiar life with which it seemed endowed. If it was a cetacean, it surpassed in size all those hitherto classified in science. Taking into consideration the mean of observations made at divers times,—rejecting the timid estimate of those who assigned to this object a length of two hundred feet, equally with the exaggerated opinions which set it down as a mile in width and three in length,—we might fairly conclude that this mysterious being surpassed greatly all dimensions admitted by the ichthyologists of the day, if it existed at all. And that it did exist was an undeniable fact; and, with that tendency which disposes the human mind in favour of the marvellous, we can understand the excitement produced in the entire world by this supernatural apparition. As to classing it in the list of fables, the idea was out of the question. On the 20th of July, 1866, the steamer Governor Higginson, of the Calcutta and Burnach Steam Navigation Company, had met this moving mass five miles off the east coast of Australia. Captain Baker thought at first that he was in the presence of an unknown sandbank; he even prepared to determine its exact position, when two columns of water, projected by the inexplicable object, shot with a hissing noise a hundred and fifty feet up into the air. Now, unless the sandbank had been submitted to the intermittent eruption of a geyser, the Governor Higginson had to do neither more nor less than with an aquatic mammal, unknown till then, which threw up from its blow-holes columns of water mixed with air and vapour.",
         "The perfume":"In eighteenth-century France there lived a man who was one of the most gifted and abominable personages in an era that knew no lack of gifted and abominable personages. His story will be told here. His name was Jean-Baptiste Grenouille, and if his name-in contrast to the names of other gifted abominations, de Sade's, for instance, or Saint-Just's, Fouch?'s, Bonaparte's, etc.-has been forgotten today, it is certainly not because Grenouille fell short of those more famous blackguards when it came to arrogance, misanthropy, immorality, or, more succinctly, to wickedness, but because his gifts and his sole ambition were restricted to a domain that leaves no traces in history: to the fleeting realm of scent. In the period of which we speak, there reigned in the cities a stench barely conceivable to us modern men and women. The streets stank of manure, the courtyards of urine, the stairwells stank of moldering wood and rat droppings, the kitchens of spoiled cabbage and mutton fat; the unaired parlors stank of stale dust, the bedrooms of greasy sheets, damp featherbeds, and the pungently sweet aroma of chamber pots. The stench of sulfur rose from the chimneys, the stench of caustic lyes from the tanneries, and from the slaughterhouses came the stench of congealed blood. People stank of sweat and unwashed clothes; from their mouths came the stench of rotting teeth, from their bellies that of onions, and from their bodies, if they were no longer very young, came the stench of rancid cheese and sour milk and tumorous disease. The rivers stank, the marketplaces stank, the churches stank, it stank beneath the bridges and in the palaces. The peasant stank as did the priest, the apprentice as did his master's wife, the whole of the aristocracy stank, even the king himself stank, stank like a rank lion, and the queen like an old goat, summer and winter. For in the eighteenth century there was nothing to hinder bacteria busy at decomposition, and so there was no human activity, either constructive or destructive, no manifestation of germinating or decaying life that was not accompanied by stench.",
         "Harry Potter and the Sorcerer's Stone":"Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense. Mr. Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large mustache. Mrs. Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbors. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere. The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn’t think they could bear it if anyone found out about the Potters. Mrs. Potter was Mrs. Dursley’s sister, but they hadn’t met for several years; in fact, Mrs. Dursley pretended she didn’t have a sister, because her sister and her good-for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbors would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn’t want Dudley mixing with a child like that"
        }
         
# Page title 
st.set_page_config(page_title='🧩 Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.title('Técnicas de desarrollo de aplicaciones de Big Data')
st.sidebar.markdown('*Lucía Méndez López - lmendez31786@alumnos.uemc.es*')

st.sidebar.divider()

option = st.sidebar.selectbox(
    "Textos de referencia para resumir",
    (texts.keys()))

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
