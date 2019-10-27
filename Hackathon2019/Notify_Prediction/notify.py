from notify_run import Notify
import MySQLdb
import sys
import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
import difflib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import *
from sklearn.model_selection import *
from sklearn.externals import joblib

model_name = "rf.joblib.dat"

name_to_path = dict()
path_to_name = dict()

name_to_path["photoshop"] = "D:/Adobe PhotoShop/Adobe Photoshop CS6 (64 Bit)/Photoshop.exe"
name_to_path["picture"] = "D:/pictures"

path_to_name["D:/Adobe PhotoShop/Adobe Photoshop CS6 (64 Bit)/Photoshop.exe"] = "photoshop"
path_to_name["D:/pictures"] = "pictures"

def training():
	params = {
		'n_estimators': 1000,
		'criterion': 'entropy',
	}
	model = RandomForestClassifier(**params)

	using = []
	pre_nexts = []

	(now, pre_next) = get_data()
	using.append(now)
	pre_nexts.append(pre_next)

	model.fit(using, pre_nexts)
	joblib.dump(model, model_name)

# get data from database
def get_data():
	sql_con=MySQLdb.connect(
	    host='127.0.0.1',
	    port= 3306,
	    user='root',
	    passwd='XXXXXX',
	    db='Hackthon2019',
	    use_unicode=True,
	    charset="utf8"
	)
	sql_cur=sql_con.cursor()
	sql_cur.execute("SELECT using FROM training_data")
	using=sql_con.commit()
	sql_cur.execute("SELECT pnexts FROM training_data")
	pre_nexts=sql_con.commit()

	return (using, pre_nexts)

# train model
training()

model = joblib.load(model_name)

now_using = "photoshop"
result = model.predict(now_using)

# send message to windows computer
notify = Notify()
notify.register()
notify.send("Also open "+str(result)+"?") # should be picture