from dotenv import load_dotenv
import os

load_dotenv() #take environment variables from .env

##MODEL INFO
MODEL_PATH = os.environ['MODEL_PATH']
BERT_NAME = os.environ['BERT_NAME']
##INFO TASK MODEL
NUM_LABEL = os.environ['NUM_LABEL']
MAX_LEN = os.environ['MAX_LEN']
##SERVER INFO
HOST = os.environ['HOST']
PORT = os.environ['PORT']
##HARWARE
DEVICE = os.environ['DEVICE']

print("------------------------------")
print("SUMMARY ENVIRONMENT VARIABLES: {}")
print("MODEL_PATH: {}".format(MODEL_PATH))
print("BERT_NAME: {}".format(BERT_NAME))
print("NUM_LABEL: {}".format(NUM_LABEL))
print("MAX_LEN: {}".format(MAX_LEN))
print("HOST: {}".format(HOST))
print("PORT: {}".format(PORT))
print("DEVICE: {}".format(DEVICE))
print("------------------------------")

