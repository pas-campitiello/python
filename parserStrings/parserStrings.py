import re
import requests
import os

def extract_links(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(f"File Content: {content[:100]}...")  # print the first 100 characters
        pattern = r'https://static\.marathon-photos\.com/photos/Sports/2023/.*?\.jpeg'
        matches = re.findall(pattern, content, re.DOTALL)
        print(f"Found {len(matches)} matches.")  # print number of matches found
        return matches

def download_file(url, folder="downloaded_files"):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Ensure the download directory exists
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Write the content to a local file
        local_filename = os.path.join(folder, url.split('/')[-1])
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded: {url} to {local_filename}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}. Reason: {e}")

def main():
    filename = 'html.txt'
    links = extract_links(filename)
    
    for link in links:
        print(link)
        download_file(link)

if __name__ == '__main__':
    main()




