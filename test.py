# -*- coding: utf-8 -*-
"""Copy of Detecting Malicious Url With Machine Learning In Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gsHe5AhCPVtsomlydwAfFmGJNTcXdnZ8

## Detecting Malicious URL With Machine Learning In Python
##### Credits Faizann
"""

# EDA Packages
import pandas as pd
def main():
    # Load Url Data 
    urls_data = pd.read_csv("urldata.csv")

    type(urls_data)

    urls_data.head()



    """### Data Vectorization Using TfidVectorizer
    #### Create A tokenizer
    + Split ,Remove Repetitions and "Com"
    """

    def makeTokens(f):
        tkns_BySlash = str(f.encode('utf-8')).split('/')	# make tokens after splitting by slash
        total_Tokens = []
        for i in tkns_BySlash:
            tokens = str(i).split('-')	# make tokens after splitting by dash
            tkns_ByDot = []
            for j in range(0,len(tokens)):
                temp_Tokens = str(tokens[j]).split('.')	# make tokens after splitting by dot
                tkns_ByDot = tkns_ByDot + temp_Tokens
            total_Tokens = total_Tokens + tokens + tkns_ByDot
        total_Tokens = list(set(total_Tokens))	#remove redundant tokens
        if 'com' in total_Tokens:
            total_Tokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
        return total_Tokens

    # Features and Labels
    url_list = urls_data["url"]
    y = urls_data["label"]

    # Machine Learning Packages
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split

    # Using Default Tokenizer
    #vectorizer = TfidfVectorizer()

    # Using Custom Tokenizer
    vectorizer = TfidfVectorizer(tokenizer=makeTokens)

    # Store vectors into X variable as Our XFeatures
    X = vectorizer.fit_transform(url_list)

    """#### Split into training and testing dataset 80/20 ratio"""

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model Building
    #using logistic regression
    logit = LogisticRegression()	
    logit.fit(X_train, y_train)

    # Accuracy of Our Model
    print("Accuracy ",logit.score(X_test, y_test))

    """### Predicting With Our Model"""

    X_predict = ["https://www.section.io/engineering-education/",
    "https://www.youtube.com/",
    "https://www.traversymedia.com/", 
    "https://www.kleinehundezuhause.com ", 
    "http://ttps://www.mecymiafinance.com  ",
    "	https://www.atlanticoceanicoilandgas.com "]

    X_predict = vectorizer.transform(X_predict)
    New_predict = logit.predict(X_predict)

    print(New_predict)

    # https://db.aa419.org/fakebankslist.php
    X_predict1 = ["www.buyfakebillsonlinee.blogspot.com", 
    "www.unitedairlineslogistics.com",
    "www.stonehousedelivery.com",
    "www.silkroadmeds-onlinepharmacy.com" ]

    X_predict1 = vectorizer.transform(X_predict1)
    New_predict1 = logit.predict(X_predict1)
    print(New_predict1)


def test():
    print("Hello")
test()