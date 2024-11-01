import pandas as pd
import numpy as np

TRAIN_FILE_PATH_FORMAT = "./datasets/{}.train.csv"
TEST_FILE_PATH_FORMAT = "./datasets/{}.test.csv"
SPEC_FILE_PATH_FORMAT = "./dataset_specs/{}.txt"

def load_raw_data(name):
    r_train = pd.read_csv(TRAIN_FILE_PATH_FORMAT.format(name))
    r_test = pd.read_csv(TEST_FILE_PATH_FORMAT.format(name))
    return r_train, r_test

def read_spec_file(fn):
    with open(fn) as sf:
        line = sf.readlines()
        assert len(line) == 1
        line = line[0].strip()
        assert line.endswith(" ~ .")
        line = line.removesuffix(" ~ .")
    return line

def load_yname(name):
    return read_spec_file(SPEC_FILE_PATH_FORMAT.format(name))

def get_x_y_matrices(ds, yname): 
    y_col = ds[yname]
    y_col = np.array(y_col)
    y_col = np.squeeze(y_col)
    
    df_str = list(ds.select_dtypes(exclude=[np.number]).columns)
    assert yname not in df_str
    for c in df_str:
        ds[c] = pd.Categorical(ds[c])
    x_mat = ds.loc[:, ds.columns != yname]
    assert ds.shape[1] - 1 == x_mat.shape[1]
    
    return x_mat, y_col

def load_dataset(name):
    r_train, r_test = load_raw_data(name)
    yname = load_yname(name)
    
    X_train, y_train = get_x_y_matrices(r_train, yname)
    X_test, y_test = get_x_y_matrices(r_test, yname)
    
    return X_train, y_train, X_test, y_test