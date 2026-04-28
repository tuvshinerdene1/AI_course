import pandas as pd
import numpy as np
import pprint

FILE_PATH = 'loan_train.csv'
TARGET_COLUMN = 'Status'
TRAIN_SIZE = 0.7

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    if 'Dependents' in df.columns:
        df['Dependents'] = df['Dependents'].replace('3+', 3).astype(float)
    
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            mode_val = df[col].mode()
            if not mode_val.empty:
                df[col] = df[col].fillna(mode_val[0])
    
    return df

def count_errors(labels):
    if len(labels) == 0: return 0
    counts = labels.value_counts()
    majority_class_count = counts.max()
    return len(labels) - majority_class_count

def find_best_split(df, target_col):
    best_error = 1.0
    best_params = None
    total_samples = len(df)

    features = [c for c in df.columns if c != target_col]

    for feature in features:
        is_numerical = pd.api.types.is_numeric_dtype(df[feature])
        unique_values = df[feature].unique()

        for val in unique_values:

            if is_numerical:
                left_labels = df[df[feature] <= val][target_col]
                right_labels = df[df[feature] > val][target_col]
            else:
                left_labels = df[df[feature] == val][target_col]
                right_labels = df[df[feature] != val][target_col]
            
            if len(left_labels) == 0 or len(right_labels) == 0:
                continue

            num_errors_left = count_errors(left_labels)
            num_errors_right = count_errors(right_labels)

            current_split_error = (num_errors_left + num_errors_right)/total_samples

            if current_split_error < best_error:
                best_error = current_split_error
                best_params = {
                    'feature': feature,
                    'threshold': val,
                    'is_numerical':is_numerical
                }
    
    return best_params

def build_tree(df, target_col, depth = 0, max_depth=5):
    labels = df[target_col]

    if len(labels.unique()) == 1 or depth >= max_depth:
        return labels.mode()[0]
    
    split = find_best_split(df, target_col)

    if split is None:
        return labels.mode()[0]
    
    if split['is_numerical']:
        left_df = df[df[split['feature']] <= split['threshold']]
        right_df = df[df[split['feature']] > split['threshold']]
    else:
        left_df = df[df[split['feature']] == split['threshold']]
        right_df = df[df[split['feature']] != split['threshold']]
    
    node = {
        'feature': split['feature'],
        'threshold': split['threshold'],
        'is_numerical': split['is_numerical'],
        'left': build_tree(left_df, target_col, depth + 1, max_depth),
        'right': build_tree(right_df, target_col, depth + 1, max_depth)
    }
    return node

def predict(tree, row):
    if not isinstance(tree, dict):
        return tree
    
    val = row[tree['feature']]
    if tree['is_numerical']:
        if val <= tree['threshold']:
            return predict(tree['left'], row)
        else:
            return predict(tree['right'], row)
    
    else:
        if val == tree['threshold']:
            return predict(tree['left'], row)
        else:
            return predict(tree['right'], row)
        

if __name__ == "__main__":
    try:
        full_df = preprocess_data(FILE_PATH)

        train_df = full_df.sample(frac=TRAIN_SIZE, random_state=1)
        test_df = full_df.drop(train_df.index)

        print(f"Learning from {len(train_df)} samples ...")
        tree = build_tree(train_df, TARGET_COLUMN, max_depth=5)

        correct = 0
        for _, row in test_df.iterrows():
            if predict(tree, row) == row[TARGET_COLUMN]:
                correct += 1
        
        accuracy = (correct/ len(test_df)) * 100
        print(f"Accuracy on test set : {accuracy:.2f}%")

        print('---Tree logic---')
        pprint.pprint(tree, depth=5)
    except FileNotFoundError:
        print("csv file incorrect")
