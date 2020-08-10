# Predicting App Popularity

#### Description
Tried to predict the popularity of an app using certain features with a Random Forest model. 
You can play around with testing if your app will be popular at [Apple App Popularity](http://192.168.1.9:8501)

Final model F1 score was .437 and an ROC AUC score of .77.

#### Data Source
[Kaggle Apple App Dataset](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps)

#### File Contents
* App Modeling and Validation.ipynb - Test models on final dataset and see the results. 
* App Dataset Cleaning and EDA.ipynb - Imported dataset from AWS, Postgress, and then in DBeaver. Read the file in Jupyter notebook where further data cleaning and EDA was done. Created a baseline model. 
* apple_app.py - File that runs the app on StreamLit.
