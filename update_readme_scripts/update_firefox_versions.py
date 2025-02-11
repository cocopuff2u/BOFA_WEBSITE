import xml.etree.ElementTree as ET
import os
from datetime import datetime
from pytz import timezone

def read_firefox_xml_value(file_path, xpath):
    """Read value from Firefox XML using xpath"""
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

def get_firefox_data(xml_path):
    """Get all Firefox channel data"""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        package = root.find('package')
        
        return {
            'release_version': package.find('latest_version').text,
            'release_download': package.find('latest_download').text,
            'beta_version': package.find('latest_devel_version').text,
            'beta_download': package.find('latest_beta_download').text,
            'developer_version': package.find('devedition_version').text,
            'developer_download': package.find('devedition_download').text,
            'nightly_version': package.find('nightly_version').text,
            'nightly_download': package.find('nightly_download').text
        }
    except Exception as e:
        print(f"Error getting Firefox data: {str(e)}")
        return {
            'release_version': 'N/A',
            'release_download': '#',
            'beta_version': 'N/A',
            'beta_download': '#',
            'developer_version': 'N/A',
            'developer_download': '#',
            'nightly_version': 'N/A',
            'nightly_download': '#'
        }

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

def generate_firefox_markdown():
    base_path = os.path.dirname(os.path.dirname(__file__))
    xml_path = os.path.join(base_path, 'repo_raw_data/latest_firefox_files/firefox_latest_versions.xml')
    
    last_updated = get_last_updated(xml_path)

    content = """---
editLink: false
lastUpdated: false
---

# <img src="/images/firefox.png" style="height: 40px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Firefox Browser Versions

<span class="extra-small">All links below direct to the official browser vendor. The links provided will always download the latest available version as of the last scan update.</span>

<span class="extra-small">_Last Updated: <code style="color : mediumseagreen">{}</code> [**_Raw XML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_firefox_files/firefox_latest_versions.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_firefox_files/firefox_latest_versions.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_firefox_files/firefox_latest_versions.json) (Automatically Updated every hour)_</span>

| **Browser** | **CFBundle Version** | **CFBundle Identifier** | **Download** |
|------------|-------------------|---------------------|------------|
| **Firefox** <br><a href="https://www.mozilla.org/en-US/firefox/notes/" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{release_version}` | `org.mozilla.firefox` | <a href="{release_download}"><img src="/images/firefox.png" alt="Download Firefox" width="80"></a> |
| **Firefox** <sup>Beta</sup> <br><a href="https://www.mozilla.org/en-US/firefox/beta/notes/" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{beta_version}` | `org.mozilla.firefoxbeta` | <a href="{beta_download}"><img src="/images/firefox.png" alt="Download Firefox Beta" width="80"></a> |
| **Firefox** <sup>Developer</sup> <br><a href="https://www.mozilla.org/en-US/firefox/developer/notes/" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{developer_version}` | `org.mozilla.firefox.dev` | <a href="{developer_download}"><img src="/images/firefox_developer.png" alt="Download Firefox Dev" width="80"></a> |
| **Firefox** <sup>Nightly</sup> | `{nightly_version}` | `org.mozilla.nightly` | <a href="{nightly_download}"><img src="/images/firefox_nightly.png" alt="Download Firefox Nightly" width="80"></a> |

---

# Browser Settings Management

View your current browser policies and explore available policy options:

### <img src="/images/firefox.png" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Firefox
1. **View Current Policies**: Enter `about:policies` in your address bar to see active policies
2. **Available Options**: [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/)

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Mozilla. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    data = get_firefox_data(xml_path)
    content = content.format(last_updated, **data)

    output_dir = os.path.join(base_path, 'docs', 'mozilla_firefox')
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, 'latest_versions.md'), 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    generate_firefox_markdown()
