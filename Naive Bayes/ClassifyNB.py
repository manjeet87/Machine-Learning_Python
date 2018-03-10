def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    return clf


def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score


    ### create classifier
    clf = GaussianNB() #TODO

    ### fit the classifier on the training features and labels
    clf.fit(features_train,labels_train)#TODO

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test) #TODO

    ctr =0
    for x,y in zip(pred,labels_test):
        if x==y:
            ctr+=1
    print (accuracy_score(labels_test,pred))
    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example,
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    accuracy = ctr*100.00/len(labels_test)#TODO
    return accuracy