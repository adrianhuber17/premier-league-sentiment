#!/bin/sh
chmod +x train_create_model.sh
source env/bin/activate
echo '-----cleaning training data-----'
python3 -m services.NLP.train_model.training_data_cleaner
echo '-----data is clean and ready for training model-----'
python3 -m services.NLP.train_model.training_model
echo '-----sentiment model created-----'

