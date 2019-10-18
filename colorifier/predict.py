import pickle
from colorifier.util import hex2rgb, hsv2rgb


class Classifier(object):
    def __init__(self):
        with open("model.pkl", "rb") as f:
            self._model = pickle.load(f)

    def _transform(self, value, transform_func):
        if isinstance(value, list):
            return [transform_func(v) for v in value]
        else:
            return [transform_func(value)]

    def classify_hsv(self, hsv):
        return self.classify_rgb(self._transform(hsv, hsv2rgb))

    def classify_rgb(self, rgb):
        if isinstance(rgb, list):
            if len(rgb) > 1:
                return self._model.predict(rgb)
            else:
                return self._model.predict(rgb)[0]
        else:
            return self._model.predict([rgb])[0]

    def classify_hex(self, hex):
        return self.classify_rgb(self._transform(hex, hex2rgb))


if __name__ == '__main__':
    clf = Classifier()
    print(clf.classify_hex("#e6194b"))
    print(clf.classify_rgb((255, 0, 0)))
    print(clf.classify_hsv((0, 255, 255)))
