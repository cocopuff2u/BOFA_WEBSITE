---
editLink: false
lastUpdated: false
---

# <img src="/images/chrome.webp" style="height: 40px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Chrome Browser Versions

<span class="extra-small">All links below direct to the official browser vendor. The links provided will always download the latest available version as of the last scan update.</span>

<span class="extra-small">_Last Updated: <code style="color : mediumseagreen">January 19, 2026 03:04 PM EST</code> [**_Raw XML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_chrome_files/chrome_latest_versions.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_chrome_files/chrome_latest_versions.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_chrome_files/chrome_latest_versions.json) (Automatically Updated every hour)_</span>

| **Browser** | **CFBundle Version** | **CFBundle Identifier** | **Download** |
|------------|-------------------|---------------------|------------|
| **Chrome** <br><a href="https://chromereleases.googleblog.com/" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br><small>Release Date:<br><em><code>January 13, 2026 09:27 PM EST</code></em></small> | `144.0.7559.60` | `com.google.Chrome` | <a href="https://dl.google.com/chrome/mac/stable/accept_tos%3Dhttps%253A%252F%252Fwww.google.com%252Fintl%252Fen_ph%252Fchrome%252Fterms%252F%26_and_accept_tos%3Dhttps%253A%252F%252Fpolicies.google.com%252Fterms/googlechrome.pkg"><img src="/images/chrome.webp" alt="Download Chrome" width="80"></a> |
| **Chrome** <sup>Extended Stable</sup> <br>_<sup>Requires `TargetChannel` policy; link is for Stable.</sup>_<br><br><br><small>Release Date:<br><em><code>January 15, 2026 10:42 PM EST</code></em></small> | `142.0.7444.265` | `com.google.Chrome` | <a href="https://dl.google.com/chrome/mac/stable/accept_tos%3Dhttps%253A%252F%252Fwww.google.com%252Fintl%252Fen_ph%252Fchrome%252Fterms%252F%26_and_accept_tos%3Dhttps%253A%252F%252Fpolicies.google.com%252Fterms/googlechrome.pkg"><img src="/images/chrome.webp" alt="Download Chrome" width="80"></a> |
| **Chrome** <sup>Beta</sup> <br><a href="https://chromereleases.googleblog.com/search/label/Beta%20updates" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br><small>Release Date:<br><em><code>January 14, 2026 06:23 PM EST</code></em></small> | `145.0.7632.5` | `com.google.Chrome.beta` | <a href="https://dl.google.com/chrome/mac/beta/accept_tos%3Dhttps%253A%252F%252Fwww.google.com%252Fintl%252Fen_ph%252Fchrome%252Fterms%252F%26_and_accept_tos%3Dhttps%253A%252F%252Fpolicies.google.com%252Fterms/googlechrome.pkg"><img src="/images/chrome_beta.webp" alt="Download Chrome" width="80"></a> |
| **Chrome** <sup>Dev</sup> <br><a href="https://chromereleases.googleblog.com/search/label/Dev%20updates" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br><small>Release Date:<br><em><code>January 16, 2026 05:15 PM EST</code></em></small> | `146.0.7635.0` | `com.google.Chrome.dev` | <a href="https://dl.google.com/chrome/mac/universal/dev/googlechromedev.dmg"><img src="/images/chrome_dev.webp" alt="Download Chrome" width="80"></a> |
| **Chrome** <sup>Canary</sup><br><br><small>Release Date:<br><em><code>January 19, 2026 08:58 AM EST</code></em></small> | `146.0.7643.0` | `com.google.Chrome.canary` | <a href="https://dl.google.com/chrome/mac/universal/canary/googlechromecanary.dmg"><img src="/images/chrome_canary.webp" alt="Download Chrome" width="80"></a> |
| **Chrome** <sup>Canary ASAN</sup><br><br><small>Release Date:<br><em><code>January 19, 2026 10:27 AM EST</code></em></small> | `146.0.7643.1` | `com.google.Chrome.canary` | <a href="https://dl.google.com/chrome/mac/universal/canary/googlechromecanary.dmg"><img src="/images/chrome_canary.webp" alt="Download Chrome ASAN" width="80"></a> |

---

# Silent Installation

Install Chrome silently via Terminal:

```bash
# Download and install latest stable Chrome (Universal - Intel & Apple Silicon)
curl -L -o GoogleChrome.pkg "https://dl.google.com/dl/chrome/mac/universal/stable/gcem/GoogleChrome.pkg"
sudo installer -pkg GoogleChrome.pkg -target /
```

---

# Browser Settings Management

View your current browser policies and explore available policy options:

### <img src="/images/chrome.webp" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Chrome
1. **View Current Policies**: Enter `chrome://policy` in your address bar to see active policies
2. **Available Options**: [Chrome Enterprise Policy Documentation](https://chromeenterprise.google/policies/)

### Common Configuration Keys

| Key | Type | Description |
|-----|------|-------------|
| `HomepageLocation` | String | Sets the default homepage URL |
| `RestoreOnStartup` | Integer | Controls startup behavior (1=restore, 4=URLs, 5=new tab) |
| `BookmarkBarEnabled` | Boolean | Show/hide the bookmark bar |
| `PasswordManagerEnabled` | Boolean | Enable/disable password manager |
| `DefaultSearchProviderEnabled` | Boolean | Enable default search provider |
| `AutofillAddressEnabled` | Boolean | Enable address autofill |
| `TranslateEnabled` | Boolean | Enable translation prompts |

---

# Useful Commands

```bash
# Get installed Chrome version
defaults read /Applications/Google\ Chrome.app/Contents/Info.plist CFBundleShortVersionString

# View Chrome policies via Terminal
defaults read com.google.Chrome

# Clear Chrome cache (both locations)
rm -rf ~/Library/Caches/Google/Chrome
rm -rf ~/Library/Application\ Support/Google/Chrome/Default/Cache

# Clear Chrome cookies
rm -rf ~/Library/Application\ Support/Google/Chrome/Default/Cookies

# Reset Chrome to defaults (caution: removes all user data)
rm -rf ~/Library/Application\ Support/Google/Chrome
rm -rf ~/Library/Caches/Google/Chrome
```

---

# Additional Resources

- **Version History**: [Chrome Stable Version History](https://github.com/cocopuff2u/BOFA/blob/main/latest_chrome_files/chrome_stable_history.xml)
- **Security Advisories**: [Chrome Security Blog](https://chromereleases.googleblog.com/search/label/Stable%20updates)
- **Enterprise Bundle**: [Chrome Enterprise Download](https://chromeenterprise.google/browser/download/)
- **AutoPkg Recipe**: [com.google.Chrome](https://github.com/autopkg/recipes/tree/master/GoogleChrome)

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Google. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/BOFA_WEBSITE/tree/main/update_readme_scripts).
