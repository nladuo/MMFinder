import pickle
from keras import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split


with open("data.pickle", "rb") as f:
    data = pickle.load(f)
    features_batch = data["features_batch"]
    labels = data["labels"]

print(features_batch.shape)
print(len(labels))

X_train, X_test, y_train, y_test = train_test_split(features_batch, labels, test_size=0.1, random_state=0)
print(X_train.shape)

model = Sequential()
model.add(Dense(256, activation='relu', input_dim=2622))
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


model.fit(X_train, y_train, epochs=40, batch_size=64, verbose=1)

print(model.evaluate(X_test, y_test, verbose=1))
