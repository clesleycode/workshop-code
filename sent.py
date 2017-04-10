import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

class TweetSentiment(object): 
    # as parameters, two files of labeled data and the two labels need to be fed in. 
    def __init__ (self, file1, file2, label1, label2):
        self.data1 = self.read_data(file1, label1)
        self.data2 = self.read_data(file2, label2)
        self.training = []
        self.test = [] 

    # returns a dictionry of every sentence tokenized
    def format_sentence(self, sent):
        return({word: True for word in nltk.word_tokenize(sent)})
    
    # forms data into usable matter
    def read_data(self, filename, label):
        data = []
        with open(filename) as f:
            for i in f: 
                data.append([self.format_sentence(i), label])
        return(data)

    # splits into training and test data
    def split_data(self):
        self.training = self.data1[:int((.9)*len(self.data1))] + self.data2[:int((.9)*len(self.data2))]
        self.test = self.data1[int((.1)*len(self.data1)):] + self.data2[int((.1)*len(self.data2)):]

    # builds and returns classifier object
    def build_classifier(self):
        classifier = NaiveBayesClassifier.train(self.training)
        return(classifier)

    # calculates and prints accuracy of classifier
    def get_accuracy(self, classifier):
        print(accuracy(classifier, self.test))
