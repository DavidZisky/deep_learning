def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier

    ### komentarz

    ### your code goes here!
    from sklearn import tree
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    #from sklearn.naive_bayes import GaussianNB
    #clf = tree.DecisionTreeClassifier(min_samples_split=2)
    clf = SVC(gamma=3, C=500)
    data = clf.fit(features_train, labels_train)
    return data
