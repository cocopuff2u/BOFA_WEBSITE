import xml.etree.ElementTree as ET
from datetime import datetime
import pytz
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_latest_xml(file_path):
    logging.info(f"Parsing XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("XML file parsed successfully")

    # Extract last_updated
    last_updated = root.find("last_updated").text.strip()
    logging.info(f"XML last_updated: {last_updated}")

    # Extract package details
    packages = []
    for package in root.findall("package"):
        package_info = {
            "name": package.find("name").text.strip(),
            "application_name": package.find("application_name").text.strip(),
            "bundleId": package.find("bundleId").text.strip(),
            "currentVersionReleaseDate": package.find("currentVersionReleaseDate").text.strip(),
            "icon_image": package.find("icon_image").text.strip(),
            "minimumOsVersion": package.find("minimumOsVersion").text.strip(),
            "releaseNotes": package.find("releaseNotes").text.strip(),
            "version": package.find("version").text.strip(),
        }
        packages.append(package_info)
        # logging.debug(f"Extracted package: {package_info}") # Uncomment to see all package details

    return last_updated, packages

def generate_readme_content(last_updated, packages):
    logging.info("Generating appstore_latest_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""---
editLink: false
lastUpdated: false
---
# <img src="/images/App_Store_logo.png" alt="image" width="40" style="vertical-align: middle; display: inline-block;" /> MacOS App Store Latest Updates

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.json)
 (Automatically Updated every 2 hours)_</span>

| Application Name | Version | Bundle ID | Minimum OS Version | Icon |
|------------------|---------|-----------|-------------------|------|
"""
    for package in packages:
        content += f"| {package['application_name']} | `{package['version']}` | {package['bundleId']} | {package['minimumOsVersion']} | <img src='{package['icon_image']}' width='25%' height='25%' /> |\n"

    # Add comment section
    content += """
> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    logging.info("appstore_latest_readme content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"macos_appstore_current_version has been overwritten.")

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_appstore_latest.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/macos_appstore/macos_appstore_current_version.md"

    # Parse the XML and generate content
    last_updated, packages = parse_latest_xml(xml_file_path)

    readme_content = generate_readme_content(last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)