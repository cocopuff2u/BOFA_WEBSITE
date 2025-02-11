import xml.etree.ElementTree as ET
from datetime import datetime
import pytz
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_cve_history_xml(file_path):
    logging.info(f"Parsing XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("XML file parsed successfully")

    # Extract last_scan_date
    last_scan_date = root.find("last_scan_date").text.strip()
    logging.info(f"XML last_scan_date: {last_scan_date}")

    # Extract update details
    updates = []
    for update in root.findall("Update"):
        version = update.find("Version").text.strip().replace("Version ", "")
        update_info = {
            "date": update.find("Date").text.strip(),
            "version": version,
            "security_updates": []
        }
        for app in update.find("SecurityUpdates").findall("Application"):
            app_info = {
                "name": app.find("Name").text.strip(),
                "cves": []
            }
            cve_elements = app.findall("CVE")
            url_elements = app.findall("URL")
            for cve, url in zip(cve_elements, url_elements):
                app_info["cves"].append({
                    "cve": cve.text.strip(),
                    "url": url.text.strip()
                })
            update_info["security_updates"].append(app_info)
        updates.append(update_info)
        # logging.debug(f"Extracted update: {update_info}") # Uncomment to see all update details

    return last_scan_date, updates

def generate_readme_content(last_scan_date, updates):
    logging.info("Generating standalone_cve_history_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""---
editLink: false
lastUpdated: false
---
# <img src="/images/Microsoft_Logo_512px.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Standalone CVE History

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{last_scan_date}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/mac_standalone_cve_history.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/mac_standalone_cve_history.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/mac_standalone_cve_history.json)
 (Automatically Updated every 2 hours)_</span>

| Version | Date | Application | CVE |
|---------|------|-------------|-----|
"""
    for update in updates:
        for app in update["security_updates"]:
            app_name = app["name"] if app["name"] != "N/A" else "&nbsp;"
            cve_list = []
            for cve_info in app["cves"]:
                if cve_info['url'] != "N/A":
                    cve_list.append(f"[{cve_info['cve']}]({cve_info['url']})")
                else:
                    cve_list.append(cve_info['cve'] if cve_info['cve'] != "N/A" else "&nbsp;")
            cve_str = ", ".join(cve_list) if cve_list else "&nbsp;"
            content += f"| {update['version']} | {update['date']} | {app_name} | {cve_str} |\n"

    content += """
> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    logging.info("standalone_cve_history content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"standalone_cve_history.md has been overwritten.")

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/mac_standalone_cve_history.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/standalone_apps/standalone_cve_history_en.md"

    # Parse the XML and generate content
    last_scan_date, updates = parse_cve_history_xml(xml_file_path)

    readme_content = generate_readme_content(last_scan_date, updates)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)