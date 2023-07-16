# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# class GoDel:
#     def __init__(self, dialog):
#         self.dialog = dialog
#     def usr_response(dialog):
#             # encode the new user input, add the eos_token and return a tensor in Pytorch
#         new_user_input_ids = tokenizer.encode(dialog[0] + tokenizer.eos_token, return_tensors='pt')

#         # append the new user input tokens to the chat history
#         bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

#         # generated a response while limiting the total chat history to 1000 tokens, 
#         chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

#         # pretty print last ouput tokens from bot
#         response ="{}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))
#         return [dialog[0], response]

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

class DialoGPT:
    step = 0
    chat_history_ids = ''
    def __init__(self, dialog):
        self.dialog = dialog
    def user_generate(dialog):
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(dialog[0] + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([DialoGPT.chat_history_ids, new_user_input_ids], dim=-1) if DialoGPT.step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens, 
        DialoGPT.chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        # pretty print last ouput tokens from bot
        response = "DialoGPT: {}".format(tokenizer.decode(DialoGPT.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))
        DialoGPT.step +=1
        return [dialog[0],response[10:]]

# a = DialoGPT
# for i in range(10):
#     print(a.user_generate([input("user: "),'']))