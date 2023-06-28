from transformers import AutoTokenizer, AutoModelForCausalLM

class CodeGenerator:
    def __init__(self, model = 'Salesforce/codegen-2B-mono'):
        print("加载模型")
        self.tokenizer = AutoTokenizer.from_pretrained(model, cache_dir='./config', local_files_only=False)
        self.model = AutoModelForCausalLM.from_pretrained(model, cache_dir='./models', local_files_only=False)

    def predict(self, text, max_length = 5, max_token_length = 2048):
        print('进行补全', text)

        # 进行token长度的缩减
        tokens = self.tokenizer.tokenize(text)
        if len(tokens) + max_length > max_token_length:
            print("输入代码的token太长了", len(tokens))
            tokens = tokens[-(max_token_length-max_length):]
        text = self.tokenizer.convert_tokens_to_string(tokens)


        input_ids = self.tokenizer(text, return_tensors="pt").input_ids
        generated_ids = self.model.generate(input_ids, max_length=input_ids.shape[1] + max_length)
        generated_tokens = generated_ids[0][-max_length:]
        return {
            'prediction': self.tokenizer.decode(generated_tokens, skip_special_tokens=True),
            'text': text
        }
