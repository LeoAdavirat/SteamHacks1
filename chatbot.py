from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-base-seq2seq")

def generate(instruction, knowledge, dialog):
    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.9, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output

class GoDel:
    def __init__(self,user_message = "Hi!"):
        self.user_message = user_message
    def usr_response(self, user_message = "Hi!"):
        # Instruction for a chitchat task
        instruction = f'Instruction: given a dialog context, you need to response empathically.'
        # Leave the knowldge empty
        knowledge = ''
        dialog = [
            user_message
        ]
        response = generate(instruction, knowledge, dialog)
        return response