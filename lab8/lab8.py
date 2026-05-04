import os
import math
import re

def tokenize(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words

def load_data_from_folder(path):
    data = []
    for label in ['spam', 'ham']:
        folder_path = os.path.join(path, label)
        for filename in os.listdir(folder_path):
            with open(os.path.join(folder_path, filename), 'r', encoding='latin-1') as f:
                words = tokenize(f.read())
                data.append((words, label))
    return data

class NaiveBayesClassifier:
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.prior_spam = 0
        self.prior_ham = 0
        self.word_counts_spam = {}
        self.word_counts_ham = {}
        self.total_words_spam = 0
        self.total_words_ham = 0
        self.vocab = set()
    
    def train(self, training_data):
        total_emails = len(training_data)
        spam_emails = [words for words, label in training_data if label =='spam']
        ham_emails = [words for words, label in training_data if label == 'ham']

        self.prior_spam = len(spam_emails) / total_emails
        self.prior_ham = len(ham_emails) / total_emails

        for words in spam_emails:
            for word in words:
                self.word_counts_spam[word] = self.word_counts_spam.get(word,0) + 1
                self.total_words_spam += 1
                self.vocab.add(word)
        
        for words in ham_emails:
            for word in words:
                self.word_counts_ham[word] = self.word_counts_ham.get(word,0)+1
                self.total_words_ham += 1
                self.vocab.add(word)

        self.n_vocab = len(self.vocab)
    
    def calculate_probability(self, word, category):
        if category == 'spam':
            word_count = self.word_counts_spam.get(word, 0)
            total_words = self.total_words_spam
        else:
            word_count = self.word_counts_ham.get(word, 0)
            total_words = self.total_words_ham

        probability = (word_count + self.alpha) / (total_words + self.alpha * self.n_vocab)
        return probability
    
    def classify(self, email_words):
        spam_score = math.log(self.prior_spam)
        ham_score = math.log(self.prior_ham)

        for word in email_words:
            if word in self.vocab:
                spam_score += math.log(self.calculate_probability(word,'spam'))
                ham_score += math.log(self.calculate_probability(word, 'ham'))
        
        if spam_score > ham_score:
            return 'spam'
        else:
            return 'ham'
        
train_path = 'spam_data/spam_data/train'
dev_path = 'spam_data/spam_data/dev'

print("Loading data")

train_set = load_data_from_folder(train_path)
dev_set = load_data_from_folder(dev_path)

print("Training Naive Bayes Classifier")
nb = NaiveBayesClassifier(alpha=1.0)
nb.train(train_set)

print("Evaluating on dev set")
# correct = 0
# for words, true_label in dev_set:
#     prediction = nb.classify(words)
#     if prediction == true_label:
#         correct += 1

# accuracy = correct / len(dev_set) * 100
# print(f"Accuracy:{accuracy:.2f}")

tp = 0
tn = 0
fp = 0
fn = 0

for words, true_label in dev_set:
    prediction = nb.classify(words)

    if prediction == 'spam' and true_label == 'spam':
        tp += 1
    elif prediction == 'ham' and true_label == 'ham':
        tn += 1
    elif prediction == 'spam' and true_label == 'ham':
        fp += 1
    elif prediction == 'ham' and true_label == 'spam':
        fn += 1

accuracy = (tp + tn) / len(dev_set)
precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

print("\n" + "="*30)
print("CONFUSION MATRIX")
print("="*30)
print(f"{'':>15} | {'Pred Spam':>10} | {'Pred Ham':>10}")
print(f"{'Actual Spam':>15} | {tp:>10} | {fn:>10}")
print(f"{'Actual Ham':>15} | {fp:>10} | {tn:>10}")
print("="*30)

print(f"Accuracy:  {accuracy*100:.2f}%")
print(f"Precision: {precision*100:.2f}%")
print(f"Recall:    {recall*100:.2f}%")
print(f"F1-Score:  {f1_score*100:.2f}%")