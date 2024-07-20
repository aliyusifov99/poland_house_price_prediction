# src/data/custom_label_encoder.py
from sklearn.preprocessing import LabelEncoder
import numpy as np

class CustomLabelEncoder(LabelEncoder):
    def __init__(self):
        super().__init__()
        self.classes_ = np.array([])

    def fit(self, y):
        self.classes_ = np.append(self.classes_, np.unique(y))
        self.classes_ = np.unique(self.classes_)
        return self

    def transform(self, y):
        # For unseen labels, assign them a new label
        unseen_label = len(self.classes_)
        return np.array([self.classes_.tolist().index(x) if x in self.classes_ else unseen_label for x in y])

    def fit_transform(self, y):
        return self.fit(y).transform(y)

    def inverse_transform(self, y):
        unseen_label = len(self.classes_)
        return np.array([self.classes_[x] if x < unseen_label else 'unseen_label' for x in y])