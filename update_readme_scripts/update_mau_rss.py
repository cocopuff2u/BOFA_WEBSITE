import xml.etree.ElementTree as ET
from datetime import datetime
import os

# Get the root directory of the project (assuming the script is inside a subfolder like '/update_readme_scripts/')
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the correct paths based on the project root
latest_xml_path = os.path.join(project_root, 'repo_raw_data', 'macos_standalone_latest.xml')
rss_xml_path = os.path.join(project_root, 'docs', 'public', 'rss_feeds', 'mau_rss.xml')

# Print the paths to verify if they are correct
print(f"Latest XML Path: {latest_xml_path}")
print(f"RSS XML Path: {rss_xml_path}")

def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# Create the latest.xml file if it doesn't exist
if not os.path.exists(latest_xml_path):
    root = ET.Element('packages')
    tree = ET.ElementTree(root)
    indent(root)
    tree.write(latest_xml_path, encoding='UTF-8', xml_declaration=True)

# Create the RSS feed file if it doesn't exist or is empty
if not os.path.exists(rss_xml_path) or os.path.getsize(rss_xml_path) == 0:
    rss = ET.Element('rss', version='2.0')
    channel = ET.SubElement(rss, 'channel')
    tree = ET.ElementTree(rss)
    indent(rss)
    tree.write(rss_xml_path, encoding='UTF-8', xml_declaration=True)

# Parse the latest.xml file
latest_tree = ET.parse(latest_xml_path)
latest_root = latest_tree.getroot()

# Extract MAU package details
mau_package = None
for package in latest_root.findall('package'):
    if package.find('name').text == 'MAU':
        mau_package = package
        break

if mau_package is None:
    raise ValueError("MAU package not found in latest.xml")

mau_short_version = mau_package.find('short_version').text
mau_update_download = mau_package.find('update_download').text
mau_last_updated = mau_package.find('last_updated').text

# Parse the RSS feed
rss_tree = ET.parse(rss_xml_path)
rss_root = rss_tree.getroot()
channel = rss_root.find('channel')

# Initialize channel-level elements if they do not exist
title = channel.find('title')
link = channel.find('link')
description = channel.find('description')
docs = channel.find('docs')

if title is None:
    title = ET.SubElement(channel, 'title')
    title.text = "MOFA - MAU RSS Feed"
if link is None:
    link = ET.SubElement(channel, 'link')
    link.text = "https://mofa.cocolabs.dev/rss_feeds/mau_rss.xml"
if description is None:
    description = ET.SubElement(channel, 'description')
    description.text = "Microsoft Office Feed for Apple - MAU RSS Feed"
if docs is None:
    docs = ET.SubElement(channel, 'docs')
    docs.text = "http://www.rssboard.org/rss-specification"

# Add the <link> element for self-referencing the feed
# Remove the unnecessary attributes (rel, type, href)
atom_link = channel.find("link[@rel='self']")
if atom_link is None:
    atom_link = ET.SubElement(channel, 'link')
    atom_link.text = "https://mofa.cocolabs.dev/rss_feeds/mau_rss.xml"

# Add the <image> element above the <item> elements
image = channel.find('image')
if image is None:
    image = ET.Element('image')
    url = ET.SubElement(image, 'url')
    url.text = "https://mofa.cocolabs.dev/images/logo_Mofa_NoBackground.png"
    title = ET.SubElement(image, 'title')
    title.text = "MOFA - MAU RSS Feed"
    link = ET.SubElement(image, 'link')
    link.text = "https://mofa.cocolabs.dev/rss_feeds/mau_rss.xml"
    first_item_index = next((i for i, elem in enumerate(channel) if elem.tag == 'item'), len(channel))
    channel.insert(first_item_index, image)

# Check if the MAU version already exists in the RSS feed
existing_version = False
for item in channel.findall('item'):
    if mau_short_version in item.find('title').text or f"Version {mau_short_version}" in item.find('description').text:
        existing_version = True
        print("MAU version already in RSS feed")
        break

# If the version is not already in the feed, add it
if not existing_version:
    new_item = ET.Element('item')
    title = ET.SubElement(new_item, 'title')
    title.text = "New Microsoft AutoUpdate Released"
    link = ET.SubElement(new_item, 'link')
    link.text = mau_update_download
    description = ET.SubElement(new_item, 'description')
    description.text = f"Version {mau_short_version}"
    pubDate = ET.SubElement(new_item, 'pubDate')
    pubDate.text = datetime.strptime(mau_last_updated, "%B %d, %Y").strftime("%a, %d %b %Y 00:00:00 +0000")
    guid = ET.SubElement(new_item, 'guid')
    guid.text = mau_update_download
    guid.set('isPermaLink', 'false')

    # Insert the new item into the RSS feed
    first_item_index = next((i for i, elem in enumerate(channel) if elem.tag == 'item'), len(channel))
    channel.insert(first_item_index, new_item)

    indent(rss_root)
    rss_tree.write(rss_xml_path, encoding='UTF-8', xml_declaration=True)
    print("RSS feed updated with new MAU version")