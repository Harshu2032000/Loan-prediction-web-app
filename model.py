import pickle

with open('loan_pred_model.pkl','wb') as file:
pickle.dump(model,file)