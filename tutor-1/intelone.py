import os
import nltk
import string
from optparse import OptionParser
from sklearn.feature_extraction.text import TfidfVectorizer

# nltk.download('punkt')


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


def normalize(text):
    return stem_tokens(
        nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


def cosine_sim(text1, text2):
    vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]


def createMap():
    text_files = {}
    value = os.listdir("poem")
    for filename in value:
        with open(os.getcwd()+"/poem/"+filename, 'rb') as f:
            text_files[filename] = f.read()
    return text_files


def get_matching_map(document_map, map_key):
    for key, val in document_map.items():
        if key == map_key:
            del document_map[key]
    return document_map


def match_documents(to_match, document_map):
    similarity_map = {}
    sorted_list = []
    with open(to_match, 'rb') as f:
        text_match_doc = f.read()
    for key, value in document_map.items():
        sorted_list.append(cosine_sim(text_match_doc, value))
        similarity_map[cosine_sim(text_match_doc, value)] = key
        sorted_list.sort(reverse=True)
    print "The documents matched in decreasing order with matching scores\n"
    for x in sorted_list:
        print "Original Doc-:", to_match,"Document matched-", similarity_map.get(x), "\tScore -:\t", x
    # for k, v in similarity_map.items():
    #     print "key--.", k, "value", v


if __name__ == '__main__':
    opt_parser = OptionParser()
    opt_parser.add_option(
        "-d", "--document", dest="documentMatch",
        help="Name of document to match with other documents",
        default=False)
    (options, args) = opt_parser.parse_args()
    document = options.documentMatch
    map_first = createMap()
    document_map = get_matching_map(map_first, document)
    match_documents(document, document_map)
# documents = [open(f) for f in text_files]
# print "\n the documents-->", documents
# tfidf = TfidfVectorizer().fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
# pairwise_similarity = tfidf * tfidf.T
# print pairwise_similarity
