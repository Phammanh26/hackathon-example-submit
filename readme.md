## HACKATHON SUMMIT
- Pull image `docker pull <my-image-summited>`, 
- Setup some environment variables `export <variable-environment>=<value>`, following by:
  + BERT_NAME: name of model pretrain (ex: bert-base-multilingual-cased)
  + MODEL_PATH: path of model from "location" (ex: /fastApiProject/bert_regression.pt)
  + HOST: target host running (ex: 0.0.0.0 or 127.0.0)
  + PORT: target port running (ex: 8000)
- Run docker container: ` docker run -it -p $PORT:$PORT -v $MODEL_PATH:/trmanh29_hackathon/output -e MODEL_PATH=/trmanh29_hackathon/output/bert_regression.pt  -e HOST=$HOST  -e PORT=$PORT <my-image-summited> `
- Expose api GET: `<my-host>:<my-port>/review-solver/solve?review_sentence=<my-sentence-test>`