import requests
from bs4 import BeautifulSoup
import re
import os
import zipfile



def createZIPFile(zip_file_path):
    zip_file = "chromedriver-win64.zip"
    if not os.path.exists(zip_file_path):
        with zipfile.ZipFile(zip_file, 'w') as zipf:
            zipf.writestr("example.txt", "This is an example content for the ZIP file.")
        print(f"ZIP file created at '{zip_file_path}'.")
    else:
        print(f"ZIP file already exists at '{zip_file_path}'.")
def unzipChromeFile(zip_path,extract_to):
    print("zip path: ",zip_path," extract path:",extract_to)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Unzipped '{zip_path}' to '{extract_to}'.")
def deleteZipFile(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"File '{file_path}' does not exist.")



json_url = "https://googlechromelabs.github.io/chrome-for-testing/"
response = requests.get(json_url)
if response.status_code == 200:
    json_data = response.text
    soup = BeautifulSoup(json_data, 'html.parser')
    sections = soup.find_all('p')
    for i, section in enumerate(sections, start=1):
        section_text = section.get_text()
        print("current paragraph: ",section_text)
        if "Version:" in section.get_text():
            pattern = r"Version: ([0-9.]*)"
            matches = re.findall(pattern, section_text)
            if matches:
                print("url: https://storage.googleapis.com/chrome-for-testing-public/"+str(matches[0])+str("/win64/chromedriver-win64.zip"))
                google_api_url =  "https://storage.googleapis.com/chrome-for-testing-public/"+str(matches[0])+str("/win64/chromedriver-win64.zip")
                response = requests.get(google_api_url, stream=True)
                home_dir = os.path.expanduser("~")
                chrome_dir = home_dir + str("\\Desktop\\selenium-java\\drivers\\chrome-"+str(matches[0]))
                if not os.path.exists(chrome_dir):
                    os.makedirs(chrome_dir)
                    print(f"Folder created at '{chrome_dir}'.")
                else:
                    print(f"Folder already exists at '{chrome_dir}'.")
                zip_file_path = os.path.join(chrome_dir,"chromedriver-win64.zip")
                createZIPFile(zip_file_path)
                if response.status_code == 200:
                    with open(zip_file_path, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=1024):
                            file.write(chunk)
                    print(f"chrome file downloaded to {zip_file_path}.")
                    unzipChromeFile(zip_file_path,chrome_dir)
                    deleteZipFile(zip_file_path)
                    print("chome file operation completed")
                    break
                else:
                    print(f"Failed to download chrome file. Status code: {response.status_code}")
                    break
else:
    print("Failed to retrieve the JSON data. Status code:", response.status_code)

















#https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.91/win64/chromedriver-win64.zip