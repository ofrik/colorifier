# Colorifier
A library to classify colors

# How to use
`from colorifier import Classifier`  
`model = Classifier()`  
`print(model.classify_hex("#e6194b"))`  
`print(model.classify_rgb((255, 0, 0)))`  
`print(model.classify_hsv((0, 255, 255)))`  
