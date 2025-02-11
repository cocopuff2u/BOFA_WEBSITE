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

    content = f"""---
editLink: false
lastUpdated: false
---
# <img src="/images/Microsoft_Logo_512px.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Standalone Update History

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{last_scan_date}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_update_history.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_update_history.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_update_history.json)
 (Automatically Updated every 2 hours)_</span>

<table class="shrink-table">
  <thead>
    <tr>
      <th>Version</th>
      <th>Business</th>
      <th>Suite</th>
      <th>Word</th>
      <th>Excel</th>
      <th>PowerPoint</th>
      <th>Outlook</th>
      <th>OneNote</th>
    </tr>
  </thead>
  <tbody>
"""
    for release in releases:
        content += f"    <tr>\n"
        content += f"      <td>{release['version']}<br><span class='extra-small'>{release['date']}</span></td>\n"
        content += f"      <td>archived</td>\n" if release['businesspro_suite_download'] == "archived" else f"      <td><a href=\"{release['businesspro_suite_download']}\">Business</a></td>\n" if release['businesspro_suite_download'] else f"      <td>&nbsp;</td>\n"
        content += f"      <td>archived</td>\n" if release['suite_download'] == "archived" else f"      <td><a href=\"{release['suite_download']}\">Suite</a></td>\n" if release['suite_download'] else f"      <td>&nbsp;</td>\n"
        content += f"      <td>archived</td>\n" if release['word_update'] == "archived" else f"      <td><a href=\"{release['word_update']}\">Word</a></td>\n" if release['word_update'] else f"      <td>&nbsp;</td>\n"
        content += f"      <td>archived</td>\n" if release['excel_update'] == "archived" else f"      <td><a href=\"{release['excel_update']}\">Excel</a></td>\n" if release['excel_update'] else f"      <td>&nbsp;</td>\n"
        content += f"      <td>archived</td>\n" if release['powerpoint_update'] == "archived" else f"      <td><a href=\"{release['powerpoint_update']}\">PowerPoint</a></td>\n" if release['powerpoint_update'] else f"      <td>&nbsp;</td>\n"
        content += f"      <td>archived</td>\n" if release['outlook_update'] == "archived" else f"      <td><a href=\"{release['outlook_update']}\">Outlook</a></td>\n" if release['outlook_update'] else f"      <td>&nbsp;</td>\n"
        content += f"      <td>archived</td>\n" if release['onenote_update'] == "archived" else f"      <td><a href=\"{release['onenote_update']}\">OneNote</a></td>\n" if release['onenote_update'] else f"      <td>&nbsp;</td>\n"
        content += f"    </tr>\n"

    content += """
  </tbody>
</table>
"""
    content += """
> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    logging.info("standalone_update_history content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"standalone_update_history.md has been overwritten.")

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_standalone_update_history.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/standalone_apps/standalone_update_history_en.md"

    # Parse the XML and generate content
    last_scan_date, releases = parse_update_history_xml(xml_file_path)

    readme_content = generate_readme_content(last_scan_date, releases)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)