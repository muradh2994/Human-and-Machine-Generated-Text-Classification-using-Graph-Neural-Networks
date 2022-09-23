DATA GENERATION:

	1) Download the shakespeare data from kaggle link:
	https://www.kaggle.com/datasets/kingburrito666/shakespeare-plays
	2) Run shakespeare500 notebook to transform the dataset into 500 documents where each contains 500 words. save file as human_shakespeare.csv
	3) Run GPT_2_to_generate_text.ipynb file to generate text using GPT2 model. Import happytransformer library to execute this file.Save the model in json format
	4) Run GPT_Neo_to_generate_text.ipynb file to generate text using GPT Neo model. Import happytransformer library to execute this file.Save the model in json format
	5) Run LSTM_pytorch.ipynb file to generate text using Lstm model. Save file in csv format
	6) Now combine all the generated data into one file. Run Preprocess.ipynb to make a balanced dataset of each 500 documents and assign model name label. Save the dataset humanvsAI.csv
	

TextGCN:
	
	1) Run tensorflow_textGCN.ipynb file to execute the TextGCN model.
	2) Install the tensorflow 1.15 version as this code is not suitable for tensorflow 2.x versions
	3) clone the github repository and download nltk library.
	4) Run the prepare_data.py file with our humanvsai dataset to convert data in a required format for the model. Data is split into train and test using 70:30 ratio 
	5) Run remove_words.py file with our dataset name to remove the stopwords and other preprocess task
	6) Run build_graph.py with our dataset name to create a large graph for our corpus
	7) Now train and evaluate the model by running train.py with our dataset name.
	8) Interpret the output by running visualize.py file. 

BertGCN:
	
	1) Run bertGCN_RoBertaGCN.ipynb file in BertGCN folder to execute the BertGCN model.\
	2) Clone the github repository
	3) Download all the dependencies using requirement.txt file
	4) Additionally, install correct versions of dgl and pytorch ignite library
	5) Again prepare_data.py present in TextGCN model is used here aswell.  
	6) Run build_graph.py with our dataset name to create a large graph for our corpus.
	7) Fine tune the bert model by running it for 3 epoch using finetune_bert.py file
	8) train and evaluate the BertGCN using train_bert_gcn.py file.
	9) control the tradeoff between Bert and BertGCN using the -m value.

RoBERTaGCN:
	
	1) Same bertGCN_RoBertaGCN.ipynb is used to exceute this model.
	2) Preprocessing is carried out in similar manner to BertGCN.
	3) Run the finetune_bert.py file by mentioning the bert initializer as 'roberta-base'
	4) Train and evaluate the model by running the train_bert_gcn.py file and mention the bert initializer as 'roberta-base'.
	5) make sure the checkpoint is changed to 'roberta-base_humanvsai'
	6) control the tradeoff between RoBERTa and RoBERTaGCN using the -m value.

RoBERTa classification:
	
	1) Run Roberta_classification.ipynb file in the RoBERTa Classification folder to execute the model
	2) Install the tokenizer and transformers from huggingface
	3) Import all the necessar libraries
	4) set max_len, batch size and epoch for the model
	5) split train and test data into 70:30 ratio
	6) valiadation data is considered as 10% of train data
	7) RoBERTa representations are classified using a Keras neural network.
	8) Model is trained and evaluated successfully
	