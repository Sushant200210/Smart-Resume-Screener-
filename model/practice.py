from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


text="Here is the sentence I want embeddings for."


marked_text = "[CLS]" + text + "[SEP]"
tokenized_text=tokenizer.tokenize(marked_text)
print(tokenized_text)