
#Library
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 1)
#n_neighbors is number of neighbor in the training set

knn.fit(X_train, y_train)