import pickle
import warnings
import pandas as pd;
warnings.filterwarnings("ignore")
   
with open("logistic_regression.p",'rb') as pickled:
    data=pickle.load(pickled)
    model=data['model']
    vectorizer=data['vectorizer']
    df=pd.read_csv("amazon_review.csv")
    # print(df.head())
    pred=[]
    for i in df.index:
        vector=vectorizer.transform([df['review'][i]])
        prediction=model.predict(vector)[0]
        pred.append(prediction)
    print(pred)
    df["logistic_sentiment"]=pred   
    df.to_csv("amazon_review.csv")    