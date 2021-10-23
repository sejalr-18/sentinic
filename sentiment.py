import pickle
import warnings
from pathlib import Path
import sys
warnings.filterwarnings("ignore")
text =sys.argv[1];
pred=[0,0,0]

try:
    import pickle
    from pathlib import Path
    import warnings
except:
    print("modules not found")    

if Path("logistic_regression.p").exists():   
    with open("logistic_regression.p",'rb') as pickled:
        try:
            data=pickle.load(pickled)
            model=data['model']
            vectorizer=data['vectorizer']
            vector=vectorizer.transform([text])
            prediction=model.predict(vector)[0]
            pred[0]=prediction
        except:
            print("Oops!", sys.exc_info(), "occurred.")            
if Path("random_forest.p").exists():
    try:
        with open("random_forest.p",'rb') as pickled:
            data=pickle.load(pickled)
            model=data['model']
            vectorizer=data['vectorizer']
            vector=vectorizer.transform([text])
            prediction=model.predict(vector)[0]
            pred[1]=prediction
    except:
        print("Oops!", sys.exc_info(), "occurred.")            
if Path("support_vector_machine.p").exists():
    try:
        with open("support_vector_machine.p",'rb') as pickled:
            data=pickle.load(pickled)
            model=data['model']
            vectorizer=data['vectorizer']
            vector=vectorizer.transform([text])
            prediction=model.predict(vector)[0]
            pred[2]=prediction
    except:
        print("Oops!", sys.exc_info(), "occurred.")                

print(pred)    