import pickle
from keras import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


if __name__ == "__main__":
    with open("data.pickle", "rb") as f:
        data = pickle.load(f)
        features_batch = data["features_batch"]
        labels = data["labels"]

    print(features_batch.shape)
    print(len(labels))

    X_train, X_test, y_train, y_test = train_test_split(features_batch, labels, test_size=0.2, random_state=0)
    print(X_train.shape)

    model = Sequential()
    model.add(Dense(256, activation='relu', input_dim=2622))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation="sigmoid"))

    model.compile(loss='binary_crossentropy',
                  optimizer='sgd',
                  metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=40, batch_size=256, verbose=1)

    y_pred = model.predict(X_test)
    y_pred_ = []
    for i in y_pred:
        y_pred_.append(int(i[0] > 0.5))

    print("accuracy:", accuracy_score(y_test, y_pred_))
    print("precision:", precision_score(y_test, y_pred_))
    print("recall:", recall_score(y_test, y_pred_))
    print("f1:", f1_score(y_test, y_pred_))
