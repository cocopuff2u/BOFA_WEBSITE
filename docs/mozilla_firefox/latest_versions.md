---
editLink: false
lastUpdated: false
---

# <img src="/images/firefox.webp" style="height: 40px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Firefox Browser Versions

<span class="extra-small">All links below direct to the official browser vendor. The links provided will always download the latest available version as of the last scan update.</span>

<span class="extra-small">_Last Updated: <code style="color : mediumseagreen">January 31, 2026 04:06 AM EST</code> [**_Raw XML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_firefox_files/firefox_latest_versions.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_firefox_files/firefox_latest_versions.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/BOFA/blob/main/latest_firefox_files/firefox_latest_versions.json) (Automatically Updated every hour)_</span>

| **Browser** | **CFBundle Version** | **CFBundle Identifier** | **Download** |
|------------|-------------------|---------------------|------------|
| **Firefox** <br><a href="https://www.mozilla.org/en-US/firefox/notes/" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br><small>Release Date:<br><em><code>January 27, 2026 12:00 AM EST</code></em></small> | `147.0.2` | `org.mozilla.firefox` | <a href="https://download-installer.cdn.mozilla.net/pub/firefox/releases/147.0.2/mac/en-US/Firefox%20147.0.2.pkg"><img src="/images/firefox.webp" alt="Download Firefox" width="80"></a> |
| **Firefox** <sup>ESR</sup> <br><a href="https://www.mozilla.org/en-US/firefox/organizations/notes/" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br><small>Release Date:<br><em><code>January 13, 2026 12:00 AM EST</code></em></small> | `140.7.0` | `org.mozilla.firefoxesr` | <a href="https://download-installer.cdn.mozilla.net/pub/firefox/releases/140.7.0esr/mac/en-US/Firefox%20140.7.0esr.pkg"><img src="/images/firefox.webp" alt="Download Firefox ESR" width="80"></a> |
| **Firefox** <sup>Beta</sup> <br><a href="https://www.mozilla.org/en-US/firefox/beta/notes/" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br><small>Release Date:<br><em><code>January 30, 2026 12:00 AM EST</code></em></small> | `148.0b9` | `org.mozilla.firefoxbeta` | <a href="https://download-installer.cdn.mozilla.net/pub/firefox/releases/148.0b9/mac/en-US/Firefox%20148.0b9.pkg"><img src="/images/firefox.webp" alt="Download Firefox Beta" width="80"></a> |
| **Firefox** <sup>Developer</sup> <br><a href="https://www.mozilla.org/en-US/firefox/developer/notes/" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br><small>Release Date:<br><em><code>January 30, 2026 12:00 AM EST</code></em></small> | `148.0b9` | `org.mozilla.firefox.dev` | <a href="https://download-installer.cdn.mozilla.net/pub/devedition/releases/148.0b9/mac/en-US/Firefox%20148.0b9.dmg"><img src="/images/firefox_developer.webp" alt="Download Firefox Dev" width="80"></a> |
| **Firefox** <sup>Nightly</sup><br><br><small>Release Date:<br><em><code>January 12, 2026 12:00 AM EST</code></em></small> | `149.0a1` | `org.mozilla.nightly` | <a href="https://download-installer.cdn.mozilla.net/pub/firefox/nightly/latest-mozilla-central/firefox-149.0a1.en-US.mac.pkg"><img src="/images/firefox_nightly.webp" alt="Download Firefox Nightly" width="80"></a> |

---

# Silent Installation

Install Firefox silently via Terminal:

```bash
# Download latest Firefox PKG (use the direct link from the table above)
curl -L -o Firefox.pkg "https://download.mozilla.org/?product=firefox-pkg-latest-ssl&os=osx&lang=en-US"
sudo installer -pkg Firefox.pkg -target /

# Or install from DMG
curl -L -o Firefox.dmg "https://download.mozilla.org/?product=firefox-latest-ssl&os=osx&lang=en-US"
hdiutil attach Firefox.dmg -quiet
cp -R "/Volumes/Firefox/Firefox.app" /Applications/
hdiutil detach "/Volumes/Firefox" -quiet
```

---

# Browser Settings Management

View your current browser policies and explore available policy options:

### <img src="/images/firefox.webp" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Firefox
1. **View Current Policies**: Enter `about:policies` in your address bar to see active policies
2. **Available Options**: [Firefox Enterprise Policy Documentation](https://mozilla.github.io/policy-templates/)

> [!TIP]
> **Recommended:** It is advised to manage Firefox policies via MDM configuration profiles using the `org.mozilla.firefox` preference domain. This ensures settings persist across updates and can be centrally managed.

### Example policies.json (Alternative Method)

If MDM is not available, you can use a local `policies.json` file. Note that this file may be overwritten during Firefox updates.

Create the distribution folder and policies file:

```bash
sudo mkdir -p /Applications/Firefox.app/Contents/Resources/distribution
sudo nano /Applications/Firefox.app/Contents/Resources/distribution/policies.json
```

Example `policies.json` content:

```json
{
  "policies": {
    "Homepage": {
      "URL": "https://example.com",
      "Locked": true
    },
    "DisableTelemetry": true,
    "DisableFirefoxStudies": true,
    "DisablePocket": true,
    "OfferToSaveLogins": false,
    "PasswordManagerEnabled": false,
    "SearchBar": "unified"
  }
}
```

---

# Useful Commands

```bash
# Get installed Firefox version
defaults read /Applications/Firefox.app/Contents/Info.plist CFBundleShortVersionString

# View Firefox profiles
ls ~/Library/Application\ Support/Firefox/Profiles/

# View cache info (in Firefox address bar)
# about:cache

# Clear Firefox cache (both locations)
rm -rf ~/Library/Caches/Firefox
rm -rf ~/Library/Application\ Support/Firefox/Profiles/*/cache2

# Clear Firefox cookies
rm -rf ~/Library/Application\ Support/Firefox/Profiles/*/cookies.sqlite

# Open Firefox Profile Manager
/Applications/Firefox.app/Contents/MacOS/firefox -ProfileManager

# Run Firefox in safe mode
/Applications/Firefox.app/Contents/MacOS/firefox -safe-mode

# Reset Firefox profile (caution: removes all user data)
rm -rf ~/Library/Application\ Support/Firefox
rm -rf ~/Library/Caches/Firefox
```

---

# Additional Resources

- **Version History**: [Firefox Version History JSON](https://github.com/cocopuff2u/BOFA/blob/main/latest_firefox_files/firefox_latest_versions_history.json)
- **Security Advisories**: [Mozilla Security Advisories](https://www.mozilla.org/en-US/security/advisories/)
- **Enterprise Documentation**: [Firefox Enterprise](https://support.mozilla.org/en-US/products/firefox-enterprise)
- **AutoPkg Recipe**: [Firefox.munki](https://github.com/autopkg/recipes/tree/master/Mozilla)

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Mozilla. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/BOFA_WEBSITE/tree/main/update_readme_scripts).
