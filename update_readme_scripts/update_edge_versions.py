import xml.etree.ElementTree as ET
import os
from datetime import datetime
from pytz import timezone

def read_edge_xml_value(root, channel, field):
    """Read value from Edge XML for specific channel and field"""
    try:
        for version in root.findall('Version'):
            if version.find('Channel').text == channel:
                return version.find(field).text
        return "N/A"
    except Exception as e:
        print(f"Error processing channel {channel}: {str(e)}")
        return "N/A"

def get_edge_data(xml_path):
    """Get all Edge channel data"""
    data = {}
    channel_mapping = {
        'current': 'stable',
        'beta': 'beta',
        'dev': 'dev',
        'canary': 'canary'
    }
    
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        for xml_channel, script_channel in channel_mapping.items():
            version = read_edge_xml_value(root, xml_channel, 'Version')
            location = read_edge_xml_value(root, xml_channel, 'Location')
            date = read_edge_xml_value(root, xml_channel, 'Date')
            
            # Parse and format the date to "Month Date, Year"
            try:
                parsed_date = datetime.strptime(date, "%B %d, %Y %I:%M %p %Z")
                formatted_date = parsed_date.strftime("%B %d, %Y")
            except ValueError:
                formatted_date = "N/A"
            
            data[f'{script_channel}_version'] = version
            data[f'{script_channel}_download'] = location
            data[f'{script_channel}_date'] = formatted_date
        
        return data
    except Exception as e:
        print(f"Error processing XML: {str(e)}")
        return {k: "N/A" for k in ['stable_version', 'stable_download', 'beta_version', 'beta_download', 
                                  'dev_version', 'dev_download', 'canary_version', 'canary_download']}

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

def generate_edge_markdown():
    base_path = os.path.dirname(os.path.dirname(__file__))
    xml_path = os.path.join(base_path, 'repo_raw_data/latest_edge_files/edge_latest_versions.xml')
    
    last_updated = get_last_updated(xml_path)

    content = """---
editLink: false
lastUpdated: false
---

# <img src="/images/edge.png" style="height: 40px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Microsoft Edge Browser Versions

<span class="extra-small">All links below direct to the official browser vendor. The links provided will always download the latest available version as of the last scan update.</span>

<span class="extra-small">_Last Updated: <code style="color : mediumseagreen">{}</code> [**_Raw XML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_edge_files/edge_latest_versions.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_edge_files/edge_latest_versions.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_edge_files/edge_latest_versions.json) (Automatically Updated every hour)_</span>

| **Browser** | **CFBundle Version** | **CFBundle Identifier** | **Download** |
|------------|-------------------|---------------------|------------|
| **Edge** <br><a href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel" style="text-decoration: none;"><small>_Release Notes_</small></a> <br><br>Last Update:<br>`{stable_date}` | `{stable_version}` | `com.microsoft.edgemac` | <a href="{stable_download}"><img src="/images/edge.png" alt="Download Edge" width="80"></a> |
| **Edge** <sup>Beta</sup> <br><a href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-beta-channel" style="text-decoration: none;"><small>_Release Notes_</small></a> <br><br>Last Update:<br>`{beta_date}` | `{beta_version}` | `com.microsoft.edgemac.beta` | <a href="{beta_download}"><img src="/images/edge_beta.png" alt="Download Edge Beta" width="80"></a> |
| **Edge** <sup>Dev</sup> <br><a href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-dev-channel" style="text-decoration: none;"><small>_Release Notes_</small></a> <br><br>Last Update:<br>`{dev_date}` | `{dev_version}` | `com.microsoft.edgemac.dev` | <a href="{dev_download}"><img src="/images/edge_dev.png" alt="Download Edge Dev" width="80"></a> |
| **Edge** <sup>Canary</sup> <br><br>Last Update:<br>`{canary_date}` | `{canary_version}` | `com.microsoft.edgemac.canary` | <a href="{canary_download}"><img src="/images/edge_canary.png" alt="Download Edge Canary" width="80"></a> |

---

# Browser Settings Management

View your current browser policies and explore available policy options:

### <img src="/images/edge.png" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Microsoft Edge
1. **View Current Policies**: Enter `edge://policy` in your address bar to see active policies
2. **Available Options**: [Microsoft Edge Enterprise Documentation](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies)

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    data = get_edge_data(xml_path)
    content = content.format(last_updated, **data)

    output_dir = os.path.join(base_path, 'docs', 'microsoft_edge')
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, 'latest_versions.md'), 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    generate_edge_markdown()