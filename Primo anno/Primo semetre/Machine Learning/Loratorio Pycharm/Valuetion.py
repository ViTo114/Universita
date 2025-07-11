import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


class ValuetioneRegressione:
    def __init__(self, yPred, y):
        self.yPred = yPred
        self.y = y
        self.matriceConfusione = self.confusionMatrix(yPred, y)


    def calcoloMetriche(self):

        return {
                  "mae" : self.mae(self)

               }


    def mae(self):
        return np.average(np.abs(self.yPred - self.y))

    def mse(self):
        return np.average((self.yPred - self.y)**2)

    def rmse(self):
        return np.average(self.mse(self.pred, self.y))

    def r2(self):

        rss = np.average((np.mean(self.y) - self.y)**2)
        rsq = np.mean((np.mean(self.y) - self.yPred)**2)

        return 1 - (rsq/rss)




class ValutazioneClassificazione:
    def __init__(self, y, yPred):
        self.y = y
        self.yPred = yPred


    def calcoloMetriche(self):
        return {
                    "prova" : "gay"
               }



    def calcoloTp(self):
        tp = 0

        for i in self.y.shape[0]:
            if self.y == 1:
                if self.yPred[i] == self.y[i]:
                    tp = tp + 1


    def calcoloTn(self):
        tn = 0

        for i in self.y.shape[0]:
            if self.y == 0:
                if self.yPred[i] == self.y[i]:
                    tn = tn + 1


    def calcolofp(self):
        fp = 0

        for i in self.y.shape[0]:
            if self.yPred[i] == 1 and self.y[i] == 0:
                fp = fp + 1


    def calcolofn(self):
        fn = 0

        for i in range(self.y.shape[0]):
            if self.yPred[i] == 0 and self.y[i] == 1:
                fn = fn + 1


    def accuracy(self):
        return (self.calcoloTn() + self.calcoloTp()) / (self.calcoloTn() + self.calcoloTp() + self.ca)