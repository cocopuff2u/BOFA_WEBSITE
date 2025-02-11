import os
import subprocess
import filecmp
from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%B %d, %Y %I:%M %p'
)

def pull_latest_raw_files():
    repo_url = "https://github.com/cocopuff2u/BOFA.git"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = base_dir
    images_dir = os.path.join(target_dir, "images")

    logging.info("Starting the pull process.")

    clone_dir = os.path.join(base_dir, "temp_clone")
    if os.path.exists(clone_dir):
        logging.info(f"Removing existing clone directory: {clone_dir}")
        subprocess.run(["rm", "-rf", clone_dir])

    logging.info(f"Cloning repository from {repo_url} to {clone_dir}")
    subprocess.run(["git", "clone", repo_url, clone_dir])
    subprocess.run(["git", "-C", clone_dir, "checkout", "main"])
    subprocess.run(["git", "-C", clone_dir, "pull", "origin", "main"])

    browser_folders = [
        "latest_chrome_files",
        "latest_edge_files",
        "latest_firefox_files",
        "latest_safari_files"
    ]

    os.makedirs(images_dir, exist_ok=True)
    
    # Copy browser-specific files
    for browser_folder in browser_folders:
        browser_dir = os.path.join(target_dir, browser_folder)
        os.makedirs(browser_dir, exist_ok=True)
        source_dir = os.path.join(clone_dir, browser_folder)
        
        if os.path.exists(source_dir):
            logging.info(f"Copying files from {browser_folder}")
            for item in os.listdir(source_dir):
                if item != "README.md":
                    src = os.path.join(source_dir, item)
                    dst = os.path.join(browser_dir, item)
                    if not os.path.exists(dst) or not filecmp.cmp(src, dst, shallow=False):
                        logging.info(f"Updating {dst} with {src}")
                        subprocess.run(["cp", src, dst])

    # Copy images
    logging.info(f"Copying images to {images_dir}")
    images_src_dir = os.path.join(clone_dir, ".github", "images")
    if os.path.exists(images_src_dir):
        for item in os.listdir(images_src_dir):
            src = os.path.join(images_src_dir, item)
            dst = os.path.join(images_dir, item)
            if not os.path.exists(dst) or not filecmp.cmp(src, dst, shallow=False):
                logging.info(f"Updating {dst} with {src}")
                subprocess.run(["cp", src, dst])

    # Copy images to docs/public/images/
    docs_images_dir = os.path.join(base_dir, "..", "docs", "public", "images")
    os.makedirs(docs_images_dir, exist_ok=True)
    logging.info(f"Copying images to {docs_images_dir}")
    for item in os.listdir(images_dir):
        src = os.path.join(images_dir, item)
        dst = os.path.join(docs_images_dir, item)
        if not os.path.exists(dst) or not filecmp.cmp(src, dst, shallow=False):
            logging.info(f"Updating {dst} with {src}")
            subprocess.run(["cp", "-r", src, dst])

    with open(os.path.join(target_dir, "pull_info.txt"), "w") as f:
        pull_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"Last pulled: {pull_time}\n")
        f.write(f"Source: {repo_url}\n")
        logging.info(f"Recorded pull information at {pull_time}")

    subprocess.run(["rm", "-rf", clone_dir])
    logging.info("Removed temporary clone directory.")

if __name__ == "__main__":
    pull_latest_raw_files()
