from all import *
from scheduler import *
from cnn_ai import *

def timer_callback(): #set timer to 1 second
    SCH_Update()
    threading.Timer(1.0, timer_callback).start()
threading.Timer(1.0, timer_callback).start()
    

temp = 20
mois = 50
model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features = prepare_cnn_model()
while True:
    predict_temp, predict_mois = predict_value(temp, mois, model, in_seq1, in_seq2, out_seq, n_steps_in, n_steps_out, n_features)
    print (f'Predicted temp: {predict_temp}, Predicted mois: {predict_mois}')
    temp+= 5
    mois += 5
    time.sleep(2)