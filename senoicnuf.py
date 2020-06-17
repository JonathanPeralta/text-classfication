from bs4 import BeautifulSoup
# from nltk.corpus import stopwords
import nltk
import inflect
import re
#nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('spanish'))

#nltk.download('punkt')

html = """<p>En Menorca sabemos que comprar una vivienda es una decisión muy
importante. Por eso analizamos contigo las ventajas tanto de alquilar como
de comprar.</p>
<p>Antes que nada, necesitas evaluar tu situación actual. Para ello responde estas
preguntas.</p>
<p>
1. ¿Tienes algo ahorrado para cubrir la cuota inicial?</p>
<p>2. ¿Estás seguro de la zona en la que deseas vivir?</p>
<p>3. ¿Puedes destinar 30% de tu sueldo en vivienda?</p>
<p>4. ¿Imaginas algo muy bueno para tu familia?</p>
<p>
Si has contestado que SÍ a todas,
¡muy probablemente estás LISTO PARA COMPRAR!</p><p><img src="https://menorca.pe/files/blog/imgs/razones-para-comprar-o-alquilar-una-vivienda_1_20200615180245.jpg" data-filename="infoalquilar.png" style="width: 704px;"><br></p><p>
</p>
<p>
<b>¿Qué significa comprar una propiedad?</b>
</p><ul><li>Es una muy buena inversión a largo plazo.</li>
<li>Te brindará seguridad: nadie te dirá que ya acabó tu contrato de alquiler.</li>
<li>Genera gran rentabilidad: con el paso del tiempo tu inmueble valdrá más de lo que
te costó.</li>
<li>Podrás realizar las mejoras o modificaciones que necesites.</li>
<li>¡Este es tu momento! Escogerás la casa que soñaste y será tuya por siempre.</li>
</ul><b>Alquilar</b>
<ul><li>No necesitas tener muchos ahorros: aparte del pago de garantía, no necesitas
invertir.
</li><li>Te da cierta flexibilidad: puedes moverte de un lugar a otro.</li>
<li>Tu dinero no tendrá retorno: los pagos solo cubren el mes.</li>
</ul><b>Tu sueño en Menorca</b>
<p>Si tu conclusión es que es momento de comprar, acércate a nuestros proyectos que
ofrecen grandes ventajas por sus miles de metros de áreas verdes, juegos para
niños y cascadas ornamentales. Además, te asesoraremos en todo lo que se refiere
a financiamiento, precios y ubicación. ¡Te esperamos!</p>"""

textolimpio = BeautifulSoup(html, 'html.parser').text
# print(textolimpio)



words = nltk.word_tokenize(textolimpio)
# print(words)


def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words


def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words

def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems

def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas

def normalize(words):
    # words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)
    words = remove_stopwords(words)
    return words

words = normalize(words)
print(words)