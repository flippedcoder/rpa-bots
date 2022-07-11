import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# read data (https://www.kaggle.com/datasets/aryashah2k/datasets-in-hr-analytics-applied-ai?resource=download&select=employee_course_ratings.csv)
employee_attrition_df = pd.read_csv("employee_attrition.csv")
employee_course_ratings_df = pd.read_csv("employee_course_ratings.csv")

# break data into train and test datasets
train_ds = employee_attrition_df.sample(frac=0.8, random_state=25)
test_ds = employee_attrition_df.drop(train_ds.index)

# get the value we want to predict from the train dataset
attrition_label = train_ds[7]
modified_train_ds = train_ds.drop(attrition_label)

# build model
model = RandomForestClassifier(
    n_estimators=300, min_samples_split=75, n_jobs=2, random_state=20220622
)

model.fit(modified_train_ds, attrition_label)

# make predictions with new data
test_prediction = model.predict(test_ds)

print(test_prediction)

# get the list into the right format

# send an email
receiver = "test@gmail.com"
body = "Check out the updated spreadsheet and let me know what you think."

yag = yagmail.SMTP("my@gmail.com")
yag.send(to=receiver, subject="That spreadsheet has been updated", contents=body)