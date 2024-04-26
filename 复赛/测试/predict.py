import sys
from transformers import AutoTokenizer, AutoModelForSequenceClassification
#model和tokenizer
model = AutoModelForSequenceClassification.from_pretrained("./bm", num_labels=2)
tokenizer = AutoTokenizer.from_pretrained("./tokenizer",use_fast=True)

def predict(text,model,tokenizer):
    encodings=tokenizer(text,return_tensors="pt",padding=True,truncation=True)
    out=model(**encodings).logits
    if out[0][0]>out[0][1]:
        return 0
    else:
        return 1

while True:
    line = sys.stdin.buffer.readline().decode("utf-8","ignore")
    if not line:
        break
    line = line.strip()
    result = predict(line,model,tokenizer)
    print(f"{result}|{line}")
