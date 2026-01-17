---
editLink: false
lastUpdated: false
---

# <img src="/images/edge.webp" style="height: 40px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Microsoft Edge Browser Versions

<span class="extra-small">All links below direct to the official browser vendor. The links provided will always download the latest available version as of the last scan update.</span>

<span class="extra-small">_Last Updated: <code style="color : mediumseagreen">January 17, 2026 02:03 PM EST</code> [**_Raw XML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_edge_files/edge_latest_versions.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_edge_files/edge_latest_versions.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_edge_files/edge_latest_versions.json) (Automatically Updated every hour)_</span>

| **Browser** | **CFBundle Version** | **CFBundle Identifier** | **Download** |
|------------|-------------------|---------------------|------------|
| **Edge** <br><a href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br><small>Release Date:<br><em><code>January 16, 2026</code></em></small> | `144.0.3719.82` | `com.microsoft.edgemac` | <a href="https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/4f2967c0-d097-4ac0-92b7-15af707ac2ac/MicrosoftEdge-144.0.3719.82.pkg"><img src="/images/edge.webp" alt="Download Edge" width="80"></a> |
| **Edge** <sup>Beta</sup> <br><a href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-beta-channel" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br><small>Release Date:<br><em><code>January 16, 2026</code></em></small> | `144.0.3719.82` | `com.microsoft.edgemac.beta` | <a href="https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/60e50f99-a60c-4c5f-91fc-ffabe95a660d/MicrosoftEdgeBeta-144.0.3719.82.pkg"><img src="/images/edge_beta.webp" alt="Download Edge Beta" width="80"></a> |
| **Edge** <sup>Dev</sup><br><br><small>Release Date:<br><em><code>January 14, 2026</code></em></small> | `145.0.3789.1` | `com.microsoft.edgemac.dev` | <a href="https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/3037f199-965d-4d35-9a30-ec6fb069c016/MicrosoftEdgeDev-145.0.3789.1.pkg"><img src="/images/edge_dev.webp" alt="Download Edge Dev" width="80"></a> |
| **Edge** <sup>Canary</sup><br><br><small>Release Date:<br><em><code>January 16, 2026</code></em></small> | `146.0.3804.0` | `com.microsoft.edgemac.canary` | <a href="https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/e6cf8d4a-57ad-4c58-94c6-ce787a0551db/MicrosoftEdgeCanary-146.0.3804.0.pkg"><img src="/images/edge_canary.webp" alt="Download Edge Canary" width="80"></a> |

---

# Silent Installation

Install Edge silently via Terminal:

```bash
# Download and install latest stable Edge (Universal - Intel & Apple Silicon)
curl -L -o MicrosoftEdge.pkg "https://go.microsoft.com/fwlink/?linkid=2093504"
sudo installer -pkg MicrosoftEdge.pkg -target /
```

---

# Browser Settings Management

View your current browser policies and explore available policy options:

### <img src="/images/edge.webp" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Microsoft Edge
1. **View Current Policies**: Enter `edge://policy` in your address bar to see active policies
2. **Available Options**: [Microsoft Edge Policy Documentation](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies)

> [!TIP]
> **Recommended:** It is advised to manage Edge policies via MDM configuration profiles using the `com.microsoft.Edge` preference domain (case-sensitive).

### Common Configuration Keys

| Key | Type | Description |
|-----|------|-------------|
| `HomepageLocation` | String | Sets the default homepage URL |
| `RestoreOnStartup` | Integer | Controls startup behavior (4=URLs, 5=new tab) |
| `FavoritesBarEnabled` | Boolean | Show/hide the favorites bar |
| `PasswordManagerEnabled` | Boolean | Enable/disable password manager |
| `DefaultSearchProviderEnabled` | Boolean | Enable default search provider |
| `EdgeCollectionsEnabled` | Boolean | Enable/disable Collections feature |
| `HubsSidebarEnabled` | Boolean | Enable/disable sidebar |

---

# Useful Commands

```bash
# Get installed Edge version
defaults read /Applications/Microsoft\ Edge.app/Contents/Info.plist CFBundleShortVersionString

# View Edge policies via Terminal (note: case-sensitive)
defaults read com.microsoft.Edge

# Clear Edge cache (both locations)
rm -rf ~/Library/Caches/Microsoft\ Edge
rm -rf ~/Library/Application\ Support/Microsoft\ Edge/Default/Cache

# Clear Edge cookies
rm -rf ~/Library/Application\ Support/Microsoft\ Edge/Default/Cookies

# Reset Edge to defaults (caution: removes all user data)
rm -rf ~/Library/Application\ Support/Microsoft\ Edge
rm -rf ~/Library/Caches/Microsoft\ Edge
```

---

# Additional Resources

- **Release Notes RSS**: [Edge Release Notes RSS](https://github.com/cocopuff2u/BOFA/blob/main/latest_edge_files/edge_rss.xml)
- **Security Updates**: [Edge Security Updates](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security)
- **Enterprise Documentation**: [Microsoft Edge Enterprise Docs](https://learn.microsoft.com/en-us/deployedge/)
- **Enterprise Download**: [Edge for Business Download](https://www.microsoft.com/en-us/edge/business/download)
- **AutoPkg Recipe**: [MicrosoftEdge](https://github.com/autopkg/n8felton-recipes/tree/master/Microsoft)

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/BOFA_WEBSITE/tree/main/update_readme_scripts).
