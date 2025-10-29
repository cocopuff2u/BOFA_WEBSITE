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

def parse_xml_file(file_path):
    """Parse XML file robustly, handling encoding and BOM issues."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)
    try:
        return ET.parse(file_path)
    except ET.ParseError:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        return ET.ElementTree(ET.fromstring(content))

def get_last_updated(xml_path):
    """Get last_updated value from XML (keeps original behaviour but tolerant)."""
    try:
        tree = parse_xml_file(xml_path)
        root = tree.getroot()
        last_updated = root.find('last_updated')
        return last_updated.text if last_updated is not None else "N/A"
    except Exception as e:
        print(f"Error getting last_updated: {str(e)}")
        return "N/A"

# --- New Safari release / tech preview fetch + generators ---
def fetch_all_safari_releases(xml_path):
    """Return list of all <release> dicts from the Safari XML (preserves file order)."""
    releases = []
    if not os.path.exists(xml_path):
        return releases
    try:
        tree = parse_xml_file(xml_path)
        root = tree.getroot()
        for rel in root.findall('release'):
            releases.append({
                'major_version': rel.findtext('major_version', default='N/A'),
                'full_version': rel.findtext('full_version', default='N/A'),
                'released': rel.findtext('released', default='N/A'),
                'release_notes': rel.findtext('release_notes', default='#'),
                'release_notes_url': rel.findtext('release_notes_url', default=None)
            })
    except Exception:
        pass
    return releases

def fetch_safari_tech_previews(xml_path):
    """Return a list of tech preview dicts: [{'macos','version','PostDate','URL','ReleaseNotes'}, ...]"""
    previews = []
    if not os.path.exists(xml_path):
        return previews
    try:
        tree = parse_xml_file(xml_path)
        root = tree.getroot()
        for tp in root.findall('Safari_Technology_Preview'):
            previews.append({
                'macos': tp.findtext('macos', default='N/A'),
                'version': tp.findtext('version', default='N/A'),
                'post_date': tp.findtext('PostDate', default='N/A'),
                'url': tp.findtext('URL', default='#'),
                'release_notes': tp.findtext('ReleaseNotes', default='#')
            })
    except Exception:
        pass
    return previews

def generate_safari_releases_table(base_path, xml_path):
    """Render a dedicated markdown table listing all Safari <release> entries using the same layout as other browsers."""
    releases = fetch_all_safari_releases(xml_path)
    if not releases:
        return ""
    table = "| **Browser** | **Version** | **CFBundle Identifier** | **Release Notes** |\n"
    table += "|------------|-------------------|---------------------|------------|\n"
    for r in releases:
        full_version = r['full_version']
        is_beta = 'beta' in (full_version or "").lower()
        display_base = "Safari"
        if is_beta:
            display_cell = f"{display_base} <sup>Beta</sup>"
        else:
            display_cell = f"**{display_base}**"
        version = full_version
        bundle_id = "com.apple.Safari"
        # icon filename (no leading slash) — we'll render as /images/{image}
        image = "safari.webp"

        # Prefer explicit URL node, otherwise fall back to release_notes text if it looks like a URL
        notes_url = r.get('release_notes_url') or r.get('release_notes') or '#'
        if isinstance(notes_url, str) and notes_url:
            notes_url = notes_url.strip()
            if notes_url.startswith('/'):
                notes_url = 'https://developer.apple.com' + notes_url
            elif notes_url.startswith('doc://') or notes_url == '#':
                notes_url = '#'
            # If release_notes is plain text (not a URL), don't link — fall back to '#'
            elif not notes_url.startswith('http'):
                notes_url = '#'

        # Build image link: link to notes_url if available else show N/A
        if notes_url and notes_url != '#':
            image_src = f"/images/{image}"
            note_link_html = f'<div align="center"><a href="{notes_url}"><img src="{image_src}" alt="Safari Release Notes" width="80"></a></div>'
        else:
            note_link_html = '<small>N/A</small>'

        last_updated_html = f"<br><br><b>Released:</b><br><em><code>{r['released']}</code></em>"
        table += (
            f"| {display_cell} {last_updated_html} | "
            f"`{version}` | "
            f"`{bundle_id}` | "
            f"{note_link_html} |\n"
        )
    table += "\n"
    return table

def generate_safari_tech_table(base_path, xml_path):
    """Generate a markdown table for Safari Technology Previews that matches other browser rows."""
    previews = fetch_safari_tech_previews(xml_path)
    if not previews:
        return ""
    table = "| **Browser** | **Version** | **CFBundle Identifier** | **Download** |\n"
    table += "|------------|-------------------|---------------------|------------|\n"
    for p in previews:
        display = f"Safari Technology Preview <sup>({p['macos']})</sup>"
        # Add a "Release Notes" link under the title when ReleaseNotes is an absolute URL
        release_notes_url = p.get('release_notes') or ''
        if isinstance(release_notes_url, str) and release_notes_url.startswith('http'):
            release_link_html = f'<br><small><a href="{release_notes_url}">Release Notes</a></small>'
        else:
            release_link_html = ''

        version = p['version']
        bundle_id = "com.apple.SafariTechnologyPreview"
        image = "safari_technology.webp"
        # prefer explicit download URL for tech previews
        download = p['url'] if p['url'] and p['url'] != 'N/A' else (p['release_notes'] if isinstance(p['release_notes'], str) and p['release_notes'].startswith('http') else '#')

        last_updated_html = f"<br><br><b>Post Date:</b><br><em><code>{p['post_date']}</code></em>"
        if download and download != '#':
            image_src = f"/images/{image}"
            image_html = f'<div align="center"><a href="{download}"><img src="{image_src}" alt="Download {display}" width="80"></a></div>'
        else:
            image_html = '<small>N/A</small>'

        table += (
            f"| **{display}**{release_link_html} {last_updated_html} | "
            f"`{version}` | "
            f"`{bundle_id}` | "
            f"{image_html} |\n"
        )
    table += "\n"
    return table
# --- END new Safari helpers ---

def generate_safari_markdown():
    base_path = os.path.dirname(os.path.dirname(__file__))
    xml_path = os.path.join(base_path, 'repo_raw_data/latest_safari_files/safari_latest_versions.xml')
    
    last_updated = get_last_updated(xml_path)
    data = get_safari_data(xml_path)

    # Build the front matter and intro (unchanged)
    content = """---
editLink: false
lastUpdated: false
---

# <img src="/images/safari.webp" style="height: 40px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Safari Browser Versions

<span class="extra-small">Safari comes pre-installed with macOS. Different versions are available for different macOS versions.</span>

<span class="extra-small">_Last Updated: <code style="color : mediumseagreen">{}</code> [**_Raw XML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_latest_versions.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_latest_versions.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_latest_versions.json) (Automatically Updated every hour)_</span>

""".format(last_updated)

    # Insert dedicated Safari releases table and tech preview table (formats match other browser rows)
    content += generate_safari_releases_table(base_path, xml_path)
    content += "\n### Safari Technology Previews\n\n"
    content += generate_safari_tech_table(base_path, xml_path)

    # Append the settings and informational footer from the original file
    content += """

---

# Browser Settings Management

View your current browser policies and explore available policy options:

### <img src="/images/safari.webp" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Safari
1. **View Current Policies**: Use Terminal: `sudo profiles show -type configuration`
2. **Available Options**: [Safari MDM Settings Documentation](https://support.apple.com/guide/mdm/safari-settings-mdm0780042d4/web)

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Apple. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    output_dir = os.path.join(base_path, 'docs', 'apple_safari')
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, 'latest_versions.md'), 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    generate_safari_markdown()
