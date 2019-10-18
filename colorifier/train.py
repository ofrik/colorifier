import randomcolor
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from colorifier.util import hex2rgb
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle


def generate_data(colors=["blue", "green", "monochrome", "orange", "pink", "purple", "red", "yellow"],
                  max_samples_per_color=100000):
    rand_color = randomcolor.RandomColor()
    colors_data = []
    colors_labels = []
    for color in colors:
        color_data = list(set(rand_color.generate(hue=color, count=max_samples_per_color)))
        colors_data += color_data
        colors_labels += [color] * len(color_data)
    df = pd.DataFrame({"color": colors_data, "label": colors_labels})
    return df


if __name__ == '__main__':
    samples = 100000
    colors = ["blue", "green", "monochrome", "orange", "pink", "purple", "red", "yellow"]
    train_df = generate_data(colors=colors, max_samples_per_color=samples)
    train_df.drop_duplicates(subset=["color"], inplace=True)
    test_df = generate_data(max_samples_per_color=samples)
    test_df.drop_duplicates(subset=["color"], inplace=True)
    similar = set(test_df["color"]) - set(train_df["color"])
    test_df = test_df[~test_df["color"].isin(similar)]
    clf = DecisionTreeClassifier()
    print(train_df.shape)
    print(test_df.shape)
    clf.fit(list(map(lambda x: list(hex2rgb(x)), train_df["color"].values)), train_df["label"])
    pred = clf.predict(list(map(lambda x: list(hex2rgb(x)), test_df["color"].values)))
    print(f"Confusion matrix DT:\n{confusion_matrix(test_df.label,pred,labels=colors)}")
    print(f"Accuracy DT:\n{accuracy_score(test_df.label,pred)}")
    with open("model.pkl", "wb") as f:
        pickle.dump(clf, f)
