# Adapted from Hugging Face tutorial: https://huggingface.co/docs/transformers/training

import numpy as np
import evaluate
from datasets import load_dataset
from transformers import (
    Trainer,
    TrainingArguments,
    AutoTokenizer,
    AutoModelForSequenceClassification,
)

try:
   import intel_extension_for_pytorch
except:
   print("cant't import ipex")

# Datasets
dataset = load_dataset("yelp_review_full")
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

small_train_dataset = dataset["train"].select(range(1000)).map(tokenize_function, batched=True)
small_eval_dataset = dataset["test"].select(range(1000)).map(tokenize_function, batched=True)

# Model
model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-cased", num_labels=5
)

# Metrics
metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

# Hugging Face Trainer
training_args = TrainingArguments(
    output_dir="test_trainer", evaluation_strategy="epoch", report_to="none",
    per_device_train_batch_size=8,
    ddp_backend='ccl',
    log_level="debug",
    use_ipex=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset,
    compute_metrics=compute_metrics,
)

# Start Training
trainer.train()