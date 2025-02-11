# 📱 Preconfigured Profiles

Welcome to the **Preconfigured Profiles** page! 🌐 Here, you will find a collection of ready-to-use **mobileconfig** files designed to simplify the management of Microsoft Office products on macOS devices 🍏. These profiles are crafted for seamless deployment, allowing you to efficiently configure Office settings across your enterprise environment. Whether you choose to upload the **mobileconfig** files directly to your MDM 📤 or copy the contents to create custom configurations 📝, the process is straightforward and hassle-free. ⚙️

Below, you'll find a list of available **mobileconfig** files for download. 📑

## 🔄 Microsoft AutoUpdate
**Preferences Domain: `com.microsoft.autoupdate2`** 🖥️

This section provides configuration profiles to enforce Microsoft AutoUpdate (MAU) settings for macOS. These profiles apply a global **3-day**, **7-day**, or **14-day** forced update policy for Microsoft apps such as Word, Excel, PowerPoint, and Teams.  

<img src="/images/mau_update_prompt.png" alt="MAU Prompt" style="vertical-align: middle; display: inline-block;" />

Key settings include:  
- **Update Channel:** Current 🔄  
- **Automatic Downloads:** Enabled 📥  
- **Update Initiation:** Begins after 3/7/14 days ⏳  
- **Forced Quit Countdown:** 60 minutes ⏰  
- **Update Check Frequency:** Every 360 minutes 🔍  

#### Configuration Profiles 🛠️  
- [**3-Day Forced Update**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_3day_update_v1.mobileconfig) ⏳  
- [**7-Day Forced Update**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_7day_update_v1.mobileconfig) 📅  
- [**14-Day Forced Update**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_14day_update_v1.mobileconfig) 📆  

#### Configuration Profiles (Outlook Daily) 🛠️  
- [**3-Day Forced Update (Outlook Daily)**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_3day_update_outlook_daily_v1.mobileconfig) ⏳  
- [**7-Day Forced Update (Outlook Daily)**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_7day_update_outlook_daily_v1.mobileconfig) 📅  
- [**14-Day Forced Update (Outlook Daily)**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_14day_update_outlook_daily_v1.mobileconfig) 📆  

<i><small>To download a configuration, click the link and select “Download Raw File.”</small></i> ✅

## 🔒 Data Privacy & Telemetry Control  
**Preferences Domain: `com.microsoft.Excel`, `com.microsoft.Outlook`, `com.microsoft.PowerPoint`, `com.microsoft.Word`, `com.microsoft.OneNote.mac`, `com.microsoft.Office365ServiceV2`, `com.microsoft.AutoUpdate2`** 🖥️

This section provides configuration profiles to disable telemetry data collection across various Microsoft apps like Word, Excel, PowerPoint, Outlook, OneNote, Office365Servicesv2, and MAU. The objective is to strengthen user privacy by limiting the amount of data shared with Microsoft. This is particularly recommended for [**GCC High or DoD environments**](https://learn.microsoft.com/en-us/microsoft-365-apps/deploy/deploy-microsoft-365-apps-gcc-high-dod).

Key settings include:  
- **SendAllTelemetryEnabled:** False 🚫  
- **SendCriticalTelemetryEnabled:** False 🚫  
- **SendASmileEnabled:** False 🚫  
- **AcknowledgedDataCollectionPolicy:** RequiredDataOnly 📋  

#### Configuration Profiles 🛠️  
- [**MAU User Privacy**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_user_privacy.mobileconfig) 🔒  
- [**Office365ServicesV2 User Privacy**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_office365servicesv2_user_privacy.mobileconfig) 🔒  
- [**Excel User Privacy**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_excel_user_privacy.mobileconfig) 🔒  
- [**OneNote User Privacy**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_onenote_user_privacy.mobileconfig) 🔒  
- [**Outlook User Privacy**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_outlook_user_privacy.mobileconfig) 🔒  
- [**PowerPoint User Privacy**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_powerpoint_user_privacy.mobileconfig) 🔒  
- [**Word User Privacy**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_word_user_privacy.mobileconfig) 🔒  

<i><small>To download a configuration, click the link and select “Download Raw File.”</small></i> ✅

## 📱 How a **mobileconfig** works?  
Click [here](/macos_tools/profile_breakdown) to get the breakdown and understand its structure!