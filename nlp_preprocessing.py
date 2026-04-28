import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Ensure required NLTK resources are downloaded
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

# Sample document (collection of sentences)
documents = [
    "Data science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems.",
    "Data scientists use machine learning and statistics to extract knowledge from structured and unstructured data.",
    "Natural language processing is a subfield of artificial intelligence focused on the interaction between computers and human language."
]

print("--- Step 1: Document Preprocessing (Single Document Example) ---")
sample_text = documents[0]
print(f"Original Text: {sample_text}\n")

# 1.1 Tokenization
tokens = word_tokenize(sample_text)
print(f"Tokens: {tokens}\n")

# 1.2 POS Tagging
pos_tags = nltk.pos_tag(tokens)
print(f"POS Tags: {pos_tags}\n")

# 1.3 Stop-word Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in stop_words and w.isalnum()]
print(f"Filtered Tokens (Stop-words & Punctuation removed): {filtered_tokens}\n")

# 1.4 Stemming
ps = PorterStemmer()
stemmed_tokens = [ps.stem(w) for w in filtered_tokens]
print(f"Stemmed Tokens: {stemmed_tokens}\n")

# 1.5 Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
print(f"Lemmatized Tokens: {lemmatized_tokens}\n")


print("--- Step 2: TF-IDF Vectorization (Full Corpus) ---")
# Initializing TF-IDF Vectorizer
# We can include preprocessing steps like stop-words directly in the vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names (tokens)
feature_names = vectorizer.get_feature_names_out()

# Displaying TF-IDF values in a readable DataFrame
df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
print("TF-IDF Matrix (Sparse representation converted to DataFrame):")
print(df_tfidf)

# Explain IDF briefly
idf = vectorizer.idf_
print("\nSome IDF values (Higher means the word is more unique to specific documents):")
for word, score in zip(feature_names[:10], idf[:10]):
    print(f"- {word}: {score:.4f}")
