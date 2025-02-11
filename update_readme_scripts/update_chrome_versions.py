import xml.etree.ElementTree as ET
import os
from datetime import datetime
from pytz import timezone

def read_chrome_xml_value(file_path, xpath):
    """Read value from Chrome XML using xpath"""
    if not os.path.exists(file_path):
        return "N/A"
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        element = root.find(xpath)
        return element.text if element is not None else "N/A"
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return f"Error: {str(e)}"

def fetch_chrome_details(xml_path, version_path, download_path):
    """Get version and download URL for a Chrome channel"""
    version = read_chrome_xml_value(xml_path, version_path)
    download = read_chrome_xml_value(xml_path, download_path)
    return version, download

def get_chrome_data(xml_path):
    """Get all Chrome channel data"""
    data = {}
    channels = ['stable', 'beta', 'dev', 'canary']
    
    for channel in channels:
        version, download = fetch_chrome_details(
            xml_path,
            f'{channel}/version',
            f'{channel}/{"latest" if channel == "stable" else channel}_download'
        )
        data[f'{channel}_version'] = version
        data[f'{channel}_download'] = download
    
    return data

def get_last_updated(xml_path):
    """Get last_updated value from XML"""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        last_updated = root.find('last_updated')
        return last_updated.text if last_updated is not None else "N/A"
    except Exception as e:
        print(f"Error getting last_updated: {str(e)}")
        return "N/A"

def generate_chrome_markdown():
    base_path = os.path.dirname(os.path.dirname(__file__))
    xml_path = os.path.join(base_path, 'repo_raw_data/latest_chrome_files/chrome_latest_versions.xml')
    
    # Get last_updated from XML instead of current time
    last_updated = get_last_updated(xml_path)

    content = """---
editLink: false
lastUpdated: false
---

# <img src="/images/chrome.png" style="height: 40px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Chrome Browser Versions

<span class="extra-small">All links below direct to the official browser vendor. The links provided will always download the latest available version as of the last scan update.</span>

<span class="extra-small">_Last Updated: <code style="color : mediumseagreen">{}</code> [**_Raw XML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_chrome_files/chrome_latest_versions.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_chrome_files/chrome_latest_versions.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_chrome_files/chrome_latest_versions.json) (Automatically Updated every hour)_</span>

| **Browser** | **CFBundle Version** | **CFBundle Identifier** | **Download** |
|------------|-------------------|---------------------|------------|
| **Chrome** <br><a href="https://chromereleases.googleblog.com/" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{stable_version}` | `com.google.Chrome` | <a href="{stable_download}"><img src="/images/chrome.png" alt="Download Chrome" width="80"></a> |
| **Chrome** <sup>Beta</sup> <br><a href="https://chromereleases.googleblog.com/search/label/Beta%20updates" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{beta_version}` | `com.google.Chrome.beta` | <a href="{beta_download}"><img src="/images/chrome_beta.png" alt="Download Chrome" width="80"></a> |
| **Chrome** <sup>Dev</sup> <br><a href="https://chromereleases.googleblog.com/search/label/Dev%20updates" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{dev_version}` | `com.google.Chrome.dev` | <a href="{dev_download}"><img src="/images/chrome_dev.png" alt="Download Chrome" width="80"></a> |
| **Chrome** <sup>Canary</sup> | `{canary_version}` | `com.google.Chrome.canary` | <a href="{canary_download}"><img src="/images/chrome_canary.png" alt="Download Chrome" width="80"></a> |

---

# Browser Settings Management

View your current browser policies and explore available policy options:

### <img src="/images/chrome.png" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Chrome
1. **View Current Policies**: Enter `chrome://policy` in your address bar to see active policies
2. **Available Options**: [Chrome Enterprise Policy Documentation](https://chromeenterprise.google/policies/)

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Google. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    # Get data for each channel
    data = get_chrome_data(xml_path)
    
    # Format content with XML last_updated and channel data
    content = content.format(last_updated, **data)

    # Create output directory and write file
    output_dir = os.path.join(base_path, 'docs', 'google_chrome')
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, 'latest_versions.md'), 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    generate_chrome_markdown()
