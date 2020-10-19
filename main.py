from humiolib import HumioIngestClient
import os



def log_convert(log_folder):
    """This function will convert log file to array"""

    messages = []
    try:
        for root, dir, files in os.walk(log_folder):
            for log_file in files:
                if log_file.endswith(".log"):
                    with open(f"{log_folder}\\{log_file}", "r") as file:
                        for line in file:
                            messages.append(line)
        return messages

    except:
        print("File not found")


def humio_upload(log_folder, base_url, user_token):
    """This function will work in Humio cloud. There are total 2 base url found one is for USA and anothet is for EU
        like 'https://cloud.us.humio.com' and 'https://cloud.humio.com' link must be excluded with slash at the end

        token: token can be found in settings > ingest > Api token"""

    client = HumioIngestClient(base_url=base_url, ingest_token=user_token)
    logs = log_convert(log_folder)
    client.ingest_messages(logs)


humio_upload(log_folder="E:\\green valley\\flog",
             base_url="https://cloud.us.humio.com",
             user_token="92a5febd-6b94-4ca1-8df8-8158f63e0809")









