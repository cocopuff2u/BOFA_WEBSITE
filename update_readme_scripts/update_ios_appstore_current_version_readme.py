import xml.etree.ElementTree as ET
from datetime import datetime
import pytz
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_update_history_xml(file_path):
    logging.info(f"Parsing XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("XML file parsed successfully")

    # Extract last_scan_date
    last_scan_date = root.find("last_scan_date").text.strip()
    logging.info(f"XML last_scan_date: {last_scan_date}")

    # Extract release details
    releases = []
    for release in root.findall("release"):
        if release.find("archive").text.strip().lower() == "true":
            release_info = {
                "date": release.find("date").text.strip(),
                "version": release.find("version").text.strip(),
                "businesspro_suite_download": "archived",
                "suite_download": "archived",
                "word_update": "archived",
                "excel_update": "archived",
                "powerpoint_update": "archived",
                "outlook_update": "archived",
                "onenote_update": "archived",
            }
        else:
            release_info = {
                "date": release.find("date").text.strip(),
                "version": release.find("version").text.strip(),
                "businesspro_suite_download": release.find("businesspro_suite_download").text.strip() if release.find("businesspro_suite_download") is not None else "",
                "suite_download": release.find("suite_download").text.strip() if release.find("suite_download") is not None else "",
                "word_update": release.find("word_update").text.strip() if release.find("word_update") is not None else "",
                "excel_update": release.find("excel_update").text.strip() if release.find("excel_update") is not None else "",
                "powerpoint_update": release.find("powerpoint_update").text.strip() if release.find("powerpoint_update") is not None else "",
                "outlook_update": release.find("outlook_update").text.strip() if release.find("outlook_update") is not None else "",
                "onenote_update": release.find("onenote_update").text.strip() if release.find("onenote_update") is not None else "",
            }
        releases.append(release_info)
        # logging.debug(f"Extracted release: {release_info}") # Uncomment to see all release details

    return last_scan_date, releases

def generate_readme_content(last_scan_date, releases):
    logging.info("Generating standalone_update_history_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""
# Standalone Update History

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{last_scan_date}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.json)
 (Automatically Updated every 4 hours)_</span>

| Version | Date | BusinessPro | Suite | Word | Excel | PowerPoint | Outlook | OneNote |
|---------|------|-------------|-------|------|-------|------------|---------|---------|
"""
    for release in releases:
        content += f"| {release['version']} | {release['date']} | "
        content += f"archived | " if release['businesspro_suite_download'] == "archived" else f"[BusinessPro]({release['businesspro_suite_download']}) | " if release['businesspro_suite_download'] else " | "
        content += f"archived | " if release['suite_download'] == "archived" else f"[Suite]({release['suite_download']}) | " if release['suite_download'] else " | "
        content += f"archived | " if release['word_update'] == "archived" else f"[Word]({release['word_update']}) | " if release['word_update'] else " | "
        content += f"archived | " if release['excel_update'] == "archived" else f"[Excel]({release['excel_update']}) | " if release['excel_update'] else " | "
        content += f"archived | " if release['powerpoint_update'] == "archived" else f"[PowerPoint]({release['powerpoint_update']}) | " if release['powerpoint_update'] else " | "
        content += f"archived | " if release['outlook_update'] == "archived" else f"[Outlook]({release['outlook_update']}) | " if release['outlook_update'] else " | "
        content += f"archived | " if release['onenote_update'] == "archived" else f"[OneNote]({release['onenote_update']}) | " if release['onenote_update'] else " | "
        content += "\n"

    logging.info("standalone_update_history_readme content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"standalone_update_history_readme.md has been overwritten.")

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
# <img src="/images/App_Store_logo.png" alt="image" width="40" style="vertical-align: middle; display: inline-block;" /> iOS App Store Latest Updates

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.json)
 (Automatically Updated every 2 hours)_</span>

| Application Name | Version | Bundle ID | Minimum OS Version | Icon |
|------------------|---------|-----------|-------------------|------|
"""
    for package in packages:
        content += f"| {package['application_name']} | `{package['version']}`| {package['bundleId']} | {package['minimumOsVersion']} | <img src='{package['icon_image']}' width='75%' height='75%' /> |\n"

    content += """
> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""
    logging.info("ios_appstore_current_version content generated successfully")

    return content

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/ios_appstore_latest.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/ios_appstore/ios_appstore_current_version.md"  # Updated path to place the file inside /MOFA/docs/

    # Parse the XML and generate content
    last_updated, packages = parse_latest_xml(xml_file_path)

    readme_content = generate_readme_content(last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)