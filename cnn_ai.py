# multivariate output multi-step 1d cnn example
from all import *
from numpy import array
from numpy import hstack
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Conv1D
from keras.layers import MaxPooling1D
# split a multivariate sequence into samples

def split_sequences(sequences, n_steps_in, n_steps_out):
    X, y = list(), list()
    for i in range(len(sequences)):
        # find the end of this pattern
        end_ix = i + n_steps_in
        out_end_ix = end_ix + n_steps_out
        # check if we are beyond the dataset
        if out_end_ix > len(sequences):
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix:out_end_ix, :]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)

def update_input(a, b, c, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out):
    
    seq1 = np.append (in_seq1[-2:], a)
    seq2 = np.append (in_seq2[-2:], b)
    seq3 = np.append (out_seq[-2:], c)
    
    x_input = np.array([seq1, seq2, seq3])
    
    in_seq1 = np.append(in_seq1, a)
    in_seq1 =  in_seq1[1:]
    in_seq2 = np.append(in_seq2, b)
    in_seq2 =  in_seq2[1:]
    out_seq = np.append(out_seq, c)
    out_seq =  out_seq[1:]
    
    in_seq1 = in_seq1.reshape((len(in_seq1), 1))
    in_seq2 = in_seq2.reshape((len(in_seq2), 1))
    out_seq = out_seq.reshape((len(out_seq), 1))
    # horizontally stack columns
    dataset = hstack((in_seq1, in_seq2, out_seq))
    # choose a number of time steps
    # convert into input/output
    X, y = split_sequences(dataset, n_steps_in, n_steps_out)
    
    
    return in_seq1, in_seq2, out_seq, x_input, X, y

# define input sequence
def prepare_cnn_model():
    in_seq1 = array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    in_seq2 = array([15, 25, 35, 45, 55, 65, 75, 85, 95])
    out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])
    model = Sequential()
    # convert to [rows, columns] structure
    in_seq1 = in_seq1.reshape((len(in_seq1), 1))
    in_seq2 = in_seq2.reshape((len(in_seq2), 1))
    out_seq = out_seq.reshape((len(out_seq), 1))
    # horizontally stack columns
    dataset = hstack((in_seq1, in_seq2, out_seq))
    # choose a number of time steps
    n_steps_in, n_steps_out = 3, 1
    # convert into input/output
    X, y = split_sequences(dataset, n_steps_in, n_steps_out)
    # flatten output
    n_output = y.shape[1] * y.shape[2]
    y = y.reshape((y.shape[0], n_output))
    # the dataset knows the number of features, e.g. 2
    n_features = X.shape[2]
    # define model

    model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=(n_steps_in, n_features)))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(50, activation='relu'))
    model.add(Dense(n_output))
    model.compile(optimizer='adam', loss='mse')
    # fit model
    return model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features
    # demonstrate prediction
def predict_value(temp, mois, model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features):
    in_seq1, in_seq2, out_seq, x_input, X, y = update_input(temp,mois,temp+mois,in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out)
    
    model.fit(X, y, epochs=100, verbose=0)
    print (f'x_input: {x_input}')
    x_input = x_input.reshape((1, n_steps_in, n_features))
    result = model.predict(x_input, verbose=0)
    print (f'Result: {result}')
    return result[0,0], result[0,1]