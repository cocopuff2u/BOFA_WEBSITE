import xml.etree.ElementTree as ET
import os
from datetime import datetime
from pytz import timezone

def read_safari_xml_value(file_path, xpath):
    """Read value from Safari XML using xpath"""
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

def get_safari_data(xml_path):
    """Get all Safari channel data"""
    data = {}
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        # Get data for each macOS version
        for os_version in ['BigSur', 'Monterey', 'Ventura', 'Sonoma']:
            element = root.find(os_version)
            if element is not None:
                data[f'{os_version.lower()}_version'] = element.find('version').text
                data[f'{os_version.lower()}_url'] = element.find('URL').text
                data[f'{os_version.lower()}_size'] = element.find('Size').text
    except Exception as e:
        print(f"Error processing XML: {str(e)}")
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

def generate_safari_markdown():
    base_path = os.path.dirname(os.path.dirname(__file__))
    xml_path = os.path.join(base_path, 'repo_raw_data/latest_safari_files/safari_latest_versions.xml')
    
    last_updated = get_last_updated(xml_path)
    data = get_safari_data(xml_path)

    content = """---
editLink: false
lastUpdated: false
---

# <img src="/images/safari.png" style="height: 40px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Safari Browser Versions

<span class="extra-small">Safari comes pre-installed with macOS. Different versions are available for different macOS versions.</span>

<span class="extra-small">_Last Updated: <code style="color : mediumseagreen">{}</code> [**_Raw XML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_latest_versions.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_latest_versions.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_latest_versions.json) (Automatically Updated every hour)_</span>

| **macOS Version** | **Safari Version** | **Bundle Identifier** | **Size** | **Download** |
|------------------|-------------------|----------|----------|------------|
| **macOS Big Sur** | `{bigsur_version}` | com.apple.Safari | {bigsur_size} | <a href="{bigsur_url}"><img src="/images/safari.png" alt="Download Safari" width="80"></a> |
| **macOS Monterey** | `{monterey_version}` | com.apple.Safari | {monterey_size} | <a href="{monterey_url}"><img src="/images/safari.png" alt="Download Safari" width="80"></a> |
| **macOS Ventura** | `{ventura_version}` | com.apple.Safari | {ventura_size} | <a href="{ventura_url}"><img src="/images/safari.png" alt="Download Safari" width="80"></a> |
| **macOS Sonoma/Sequoia** | `{sonoma_version}` | com.apple.Safari | {sonoma_size} | <a href="{sonoma_url}"><img src="/images/safari.png" alt="Download Safari" width="80"></a> |

---

# Browser Settings Management

View your current browser policies and explore available policy options:

### <img src="/images/safari.png" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Safari
1. **View Current Policies**: Use Terminal: `sudo profiles show -type configuration`
2. **Available Options**: [Safari MDM Settings Documentation](https://support.apple.com/guide/mdm/safari-settings-mdm0780042d4/web)

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Apple. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    content = content.format(last_updated, **data)

    output_dir = os.path.join(base_path, 'docs', 'apple_safari')
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, 'latest_versions.md'), 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    generate_safari_markdown()
