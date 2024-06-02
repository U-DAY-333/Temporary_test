import re

def get_tokens(file_path):
    def read_log_file(file_path):
        with open(file_path, 'r') as file:
            logs = file.readlines()
        return logs

    def preprocess_logs(logs):
        # Tokenize each log entry into words
        tokenized_logs = [re.findall(r'\b\w+\b', log.lower()) for log in logs]
        return tokenized_logs


    logs = read_log_file(file_path)
    tokenized_logs = preprocess_logs(logs)

    # Print the first few tokenized logs
    return tokenized_logs

file_path = "C:/Users/sashinag/OneDrive - Cisco/Desktop/log_test.txt"
tokens = get_tokens(file_path)

#sfnbkdsahv ,avdsjd ncjsa nckal an
