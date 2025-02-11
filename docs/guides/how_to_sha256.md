# 🔐 How to Use SHA256 on macOS  

## 🔎 What is a SHA256 Checksum?  

SHA256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that generates a unique, fixed-length string for a file. Use it to:  
- ✅ Verify file integrity (detect tampering).  
- 🔒 Authenticate downloads by matching checksums.  

## ✍️ Generate a SHA256 Checksum  

### 1️⃣ Open Terminal  
- Search for **Terminal** using `Cmd + Space` (Spotlight).  

### 2️⃣ Navigate to the File  
- Use the `cd` command to locate your file:  
  ```bash
  cd /path/to/your/file
  ```  

### 3️⃣ Run the Checksum Command  
- Replace `yourfile` with the file name:  
  ```bash
  shasum -a 256 yourfile
  ```  
- Example output:  
  ```
  e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  yourfile
  ```  

### 4️⃣ Compare Values  
- Match the checksum from the output with the source-provided value.  

## 🌐 Use SHA256 with `curl`  

### 1️⃣ Download the File  
- Use `curl` with the file URL:  
  ```bash
  curl -O https://example.com/myfile.pkg
  ```  

### 2️⃣ Generate the Checksum  
- Run the SHA256 command:  
  ```bash
  shasum -a 256 myfile.pkg
  ```  

### 3️⃣ Verify Integrity  
- Compare the generated checksum with the one provided by the source.  

## 🚀 Example Workflow  

1. **Download the file**:  
   ```bash
   curl -O https://example.com/software.pkg
   ```  
2. **Generate SHA256 checksum**:  
   ```bash
   shasum -a 256 software.pkg
   ```  
3. **Compare checksum**:  
   - Provided: `abc123...`  
   - Output:  
     ```
     abc123...  software.pkg
     ```  
   - ✅ Match means the file is secure.  

### 💡 Need More Help?  
- [macOS Terminal Guide](https://support.apple.com/guide/terminal)  
- [Understanding SHA256](https://en.wikipedia.org/wiki/SHA-2)  
