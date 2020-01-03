from django.db import models
import pandas as pd
import joblib


class iris(models.Model):

    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()

    def input(self, content):
        self.sepal_length = content[0]
        self.sepal_width = content[1]
        self.petal_length = content[2]
        self.petal_width = content[3]
        self.get_species

    flowers = (
        (0 , "Iris-setosa"),
        (1 , "Iris-versicolor"),
        (2 , "Iris-virginica"),
    )
    species = models.IntegerField(choices = flowers)

    def get_species(self):
        file = open("pkl/iris_pkl.pkl","rb")
        model2 = joblib.load(file)
        self.species = model2.predict([[self.sepal_length,self.sepal_width,self.petal_length,self.petal_width]])[0]
        # print(model2.predict([[6,2.9,5,1.5],[1.2,2.4,2.5,3]]))
        file.close()
        # self.save()

# Create your models here.
