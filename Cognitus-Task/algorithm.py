import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
# from sklearn import cross_validation

from sklearn.model_selection import train_test_split


from sklearn.svm import SVC
from sklearn.metrics import precision_score, accuracy_score, recall_score
import redis

redis_client=redis.StrictRedis(host='localhost', port=6379, db=0)

def create_data(file):
    df = pd.read_excel(file)
    return df['text'].tolist(), df['label'].tolist()


#feature extraction - creating a tf-idf matrix
def tfidf(data, ma = 0.6, mi = 0.0001):
    tfidf_vectorize = TfidfVectorizer()
    tfidf_data = tfidf_vectorize.fit_transform(data)
    return tfidf_data, tfidf_vectorize


#SVM classifier
def test_SVM(x_train, x_test, y_train, y_test):
    SVM = SVC(kernel = 'linear', probability=True)
    SVMClassifier = SVM.fit(x_train, y_train)
    predictions = SVMClassifier.predict(x_test)
    a = accuracy_score(y_test, predictions)
    p = precision_score(y_test, predictions, average = 'weighted')
    r = recall_score(y_test, predictions, average = 'weighted')
    return SVMClassifier, a, p, r



def dump_model(model, file_output,name):
    model_dmp=pickle.dumps(model)
    redis_client.set(name,model_dmp) 

def load_model(key):
    return pickle.loads(redis_client.get(key))
    
	
	
# # GET DATA
# text, label = test_read_sql()

# # TRAIN
# training, vectorizer = tfidf(text)
# x_train, x_test, y_train, y_test = cross_validation.train_test_split(training, label, test_size = 0.25, random_state = 0)
# model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
# dump_model(model, 'model.pickle')
# dump_model(vectorizer, 'vectorizer.pickle')


# # PREDICTION
# model = load_model('model.pickle')
# vectorizer = load_model('vectorizer.pickle')
# user_text = "whereafter"
# tdifd = vectorizer.transform([user_text])
# result = model.predict_proba(tfidf)
# print(result)
