import os
import requests

# Folder where your small images are saved
input_folder = r"Input Path"  # Example: "C:/Users/YourName/Downloads/AmazonImages"
output_folder = r"Output Path"
os.makedirs(output_folder, exist_ok=True)

base_url = "https://m.media-amazon.com/images/I/"

# Choose desired image resolution
desired_size = "_SL1500_"

# Loop through each saved file
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        # Extract image code (before ._)
        if "._" in filename:
            image_code = filename.split("._")[0]
        else:
            image_code = filename.replace(".jpg", "")

        # Build new high-res URL
        high_res_url = f"{base_url}{image_code}.{desired_size}.jpg"

        try:
            print(f"Downloading: {high_res_url}")
            response = requests.get(high_res_url, timeout=10)
            if response.status_code == 200:
                output_path = os.path.join(output_folder, filename.replace(".jpg", f"_highres.jpg"))
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                print(f"Saved: {output_path}")
            else:
                print(f"Failed to download: {high_res_url} - Status {response.status_code}")
        except Exception as e:
            print(f"Error for {high_res_url}: {e}")

print("Download completed.")
