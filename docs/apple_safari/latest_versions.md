---
editLink: false
lastUpdated: false
---

# <img src="/images/safari.webp" style="height: 40px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Safari Browser Versions

<span class="extra-small">Safari comes pre-installed with macOS. Different versions are available for different macOS versions.</span>

<span class="extra-small">_Last Updated: <code style="color : mediumseagreen">January 28, 2026 08:18 AM EST</code> [**_Raw XML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_latest_versions.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_latest_versions.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_latest_versions.json) (Automatically Updated every hour)_</span>

| **Browser** | **Version** | **CFBundle Identifier** | **Release Notes** |
|------------|-------------------|---------------------|------------|
| **Safari** <br><br><b>Released:</b><br><em><code>December 15, 2025</code></em> | `26.3 (20623.2.2)` | `com.apple.Safari` | <div align="center"><a href="https://developer.apple.com/documentation/safari-release-notes/safari-26_3-release-notes"><img src="/images/safari.webp" alt="Safari Release Notes" width="80"></a></div> |
| **Safari** <br><br><b>Released:</b><br><em><code>July 29, 2025</code></em> | `18.6 (20621.3.11)` | `com.apple.Safari` | <div align="center"><a href="https://developer.apple.com/documentation/safari-release-notes/safari-18_6-release-notes"><img src="/images/safari.webp" alt="Safari Release Notes" width="80"></a></div> |
| **Safari** <br><br><b>Released:</b><br><em><code>July 29, 2024</code></em> | `17.6 (19618.3.11)` | `com.apple.Safari` | <div align="center"><a href="https://developer.apple.com/documentation/safari-release-notes/safari-17_6-release-notes"><img src="/images/safari.webp" alt="Safari Release Notes" width="80"></a></div> |
| **Safari** <br><br><b>Released:</b><br><em><code>July 24, 2023</code></em> | `16.6 (18615.3.12)` | `com.apple.Safari` | <div align="center"><a href="https://developer.apple.com/documentation/safari-release-notes/safari-16_6-release-notes"><img src="/images/safari.webp" alt="Safari Release Notes" width="80"></a></div> |
| **Safari** <br><br><b>Released:</b><br><em><code>July 20, 2022</code></em> | `15.6 (17613.3.9)` | `com.apple.Safari` | <div align="center"><a href="https://developer.apple.com/documentation/safari-release-notes/safari-15_6-release-notes"><img src="/images/safari.webp" alt="Safari Release Notes" width="80"></a></div> |
| **Safari** <br><br><b>Released:</b><br><em><code>April 26, 2021</code></em> | `14.1 (16611.1.21)` | `com.apple.Safari` | <div align="center"><a href="https://developer.apple.com/documentation/safari-release-notes/safari-14_1-release-notes"><img src="/images/safari.webp" alt="Safari Release Notes" width="80"></a></div> |
| **Safari** <br><br><b>Released:</b><br><em><code>March 24, 2020</code></em> | `13.1 (15609.1.20)` | `com.apple.Safari` | <div align="center"><a href="https://developer.apple.com/documentation/safari-release-notes/safari-13_1-release_notes"><img src="/images/safari.webp" alt="Safari Release Notes" width="80"></a></div> |
| **Safari** <br><br><b>Released:</b><br><em><code>March 25, 2019</code></em> | `12.1 (14607.1.40)` | `com.apple.Safari` | <div align="center"><a href="https://developer.apple.com/documentation/safari-release-notes/safari-12_1-release-notes"><img src="/images/safari.webp" alt="Safari Release Notes" width="80"></a></div> |


### Safari Technology Previews

| **Browser** | **Version** | **CFBundle Identifier** | **Download** |
|------------|-------------------|---------------------|------------|
| **Safari Technology Preview <sup>(Tahoe)</sup>**<br><small><a href="https://developer.apple.com/documentation/safari-technology-preview-release-notes">Release Notes</a></small> <br><br><b>Post Date:</b><br><em><code>January 14, 2026</code></em> | `235` | `com.apple.SafariTechnologyPreview` | <div align="center"><a href="https://secure-appldnld.apple.com/STP/047-13724-20260114-ba19b299-e1aa-4a1f-adcb-01bf838fbcff/SafariTechnologyPreview.dmg"><img src="/images/safari_technology.webp" alt="Download Safari Technology Preview <sup>(Tahoe)</sup>" width="80"></a></div> |
| **Safari Technology Preview <sup>(Sequoia)</sup>**<br><small><a href="https://developer.apple.com/documentation/safari-technology-preview-release-notes">Release Notes</a></small> <br><br><b>Post Date:</b><br><em><code>January 14, 2026</code></em> | `235` | `com.apple.SafariTechnologyPreview` | <div align="center"><a href="https://secure-appldnld.apple.com/STP/047-13739-20260114-5d6c0f76-26ef-4d2a-8f5e-96113211bbc9/SafariTechnologyPreview.dmg"><img src="/images/safari_technology.webp" alt="Download Safari Technology Preview <sup>(Sequoia)</sup>" width="80"></a></div> |



---

# Safari Updates

Safari is updated through macOS Software Update. Unlike other browsers, Safari cannot be installed standalone:

```bash
# Check for available macOS/Safari updates
softwareupdate --list

# Install all available updates (including Safari)
sudo softwareupdate --install --all

# Install Safari Technology Preview (if downloaded)
hdiutil attach SafariTechnologyPreview.dmg
sudo installer -pkg /Volumes/Safari\ Technology\ Preview/Safari\ Technology\ Preview.pkg -target /
hdiutil detach /Volumes/Safari\ Technology\ Preview
```

---

# Browser Settings Management

View your current browser policies and explore available policy options:

### <img src="/images/safari.webp" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Safari
1. **View Current Policies**: Use Terminal: `sudo profiles show -type configuration`
2. **Available Options**: [Apple Platform Deployment](https://support.apple.com/guide/deployment/)

> [!TIP]
> **Recommended:** It is advised to manage Safari settings via MDM configuration profiles using the `com.apple.Safari` preference domain.

### Example MDM Configuration Profile Keys

| Key | Type | Description |
|-----|------|-------------|
| `HomePage` | String | Sets the default homepage URL |
| `NewWindowBehavior` | Integer | Controls new window (0=Homepage, 1=Empty, 2=Same Page, 3=Bookmarks) |
| `NewTabBehavior` | Integer | Controls new tab (0=Homepage, 1=Empty, 2=Same Page, 3=Bookmarks) |
| `AutoFillPasswords` | Boolean | Enable/disable password autofill |
| `AutoFillCreditCardData` | Boolean | Enable/disable credit card autofill |
| `WebKitJavaScriptEnabled` | Boolean | Enable/disable JavaScript |
| `SafariAllowPopups` | Boolean | Allow/block popup windows |
| `ExtensionsEnabled` | Boolean | Enable/disable Safari extensions |

---

# Useful Commands

```bash
# Get installed Safari version
defaults read /Applications/Safari.app/Contents/Info.plist CFBundleShortVersionString

# Get Safari build version
defaults read /Applications/Safari.app/Contents/Info.plist CFBundleVersion

# View Safari preferences
defaults read com.apple.Safari

# Clear Safari cache (macOS 10.14 Mojave and newer)
rm -rf ~/Library/Containers/com.apple.Safari/Data/Library/Caches

# Clear Safari cache (legacy location for older macOS)
rm -rf ~/Library/Caches/com.apple.Safari

# Clear Safari history (requires closing Safari first)
rm -rf ~/Library/Safari/History.db*

# Reset Safari to defaults (caution: removes all user data)
rm -rf ~/Library/Safari
rm -rf ~/Library/Containers/com.apple.Safari
rm -rf ~/Library/Caches/com.apple.Safari
rm -rf ~/Library/Cookies/com.apple.Safari.cookies
```

---

# Additional Resources

- **Version History**: [Safari Version History](https://github.com/cocopuff2u/BOFA/blob/main/latest_safari_files/safari_all_history.xml)
- **Security Updates**: [Apple Security Updates](https://support.apple.com/en-us/HT201222)
- **Safari Release Notes**: [Safari Release Notes](https://developer.apple.com/documentation/safari-release-notes)
- **Developer Documentation**: [Safari Developer Resources](https://developer.apple.com/safari/)
- **MDM Payload Reference**: [Apple Platform Deployment](https://support.apple.com/guide/deployment/)

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Apple. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/BOFA_WEBSITE/tree/main/update_readme_scripts).
