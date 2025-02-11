# 📂 MOFA iOS RAW Feeds

This directory `https://github.com/cocopuff2u/MOFA/tree/main/latest_raw_files` contains raw output information related to Microsoft Standalone Applications and Mac/iOS App Store applications. These outputs are generated automatically using scripts, providing MacAdmins with the latest information in various formats. This setup simplifies the process of accessing and managing app-related data provided by Microsoft.

## 🛠️ Repository Overview

- **Scripts Location**: All scripts used to retrieve and process the data are located in the `https://github.com/cocopuff2u/MOFA/tree/main/.github/actions` directory of the repository. These scripts automate the fetching and formatting of app data from Microsoft-provided feeds. The raw data is automatically updated every 4 hours using a GitHub Action, which is triggered by workflows located in the `https://github.com/cocopuff2u/MOFA/tree/main/.github/actions` directory.
- **Purpose**: The scripts collect app metadata, convert it into multiple formats, and ensure the information remains current.

## 📄 File Outputs  

This directory provides app-related data in three widely-used formats: XML, JSON, and YAML. Each format contains the same set of files for easy comparison and integration into various workflows. Below is a breakdown of the available files by format:

### 🧩 XML Files  
**Description**: XML provides structured app data, ideal for systems requiring hierarchical data representation.  s

- **[iOS AppStore Latest](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.xml)**  
  Provides the latest details about macOS standalone apps.  

### 🌐 JSON Files  
**Description**: JSON offers lightweight and easy-to-parse data, commonly used in modern development environments.  

- **[iOS AppStore Latest](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.json)**  
  Provides the latest details about macOS standalone apps.  

### ✍️ YAML Files  
**Description**: YAML offers a human-readable format, ideal for configurations and manual edits.  

- **[iOS AppStore Latest](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.yaml)**  
  Provides the latest details about macOS standalone apps.  

## 🌟 Why Multiple Formats?

The choice to provide XML, JSON, and YAML outputs ensures compatibility with a wide range of tools and systems. By supporting multiple formats, we accommodate diverse user needs:

- **XML**: Designed for enterprise applications and legacy systems.
- **JSON**: Suitable for modern development environments and APIs.
- **YAML**: Ideal for user-friendly configuration and quick manual edits.

## 📌 Usage Instructions

1. Locate the required output file in this directory.
2. Refer to the scripts in the `https://github.com/cocopuff2u/MOFA/tree/main/.github/actions` directory to understand or customize how the data is fetched and formatted.
3. Choose the format that best fits your application or integration needs.

## 🔗 Access the Latest Raw Files

You can access all the latest raw files [here](https://github.com/cocopuff2u/MOFA/tree/main/latest_raw_files).
