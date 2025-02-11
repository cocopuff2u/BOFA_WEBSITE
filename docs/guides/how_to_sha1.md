# 🔐 How to Use SHA1 on macOS

## 🔎 What is a SHA1 Checksum?

SHA1 (Secure Hash Algorithm 1) is a cryptographic hash function that generates a unique string for a file. Use it to:
- ✅ Verify file integrity (detect tampering).
- 🔒 Authenticate downloads by matching checksums.

## ✍️ Generate a SHA1 Checksum

### 1️⃣ Open Terminal
- Search for **Terminal** with `Cmd + Space` (Spotlight).

### 2️⃣ Navigate to the File
- Use the `cd` command to locate your file:
  ```bash
  cd /path/to/your/file
  ```

### 3️⃣ Run the Checksum Command
- Replace `yourfile` with the file name:
  ```bash
  shasum -a 1 yourfile
  ```
- Example output:
  ```
  da39a3ee5e6b4b0d3255bfef95601890afd80709  yourfile
  ```

### 4️⃣ Compare Values
- Match the checksum from the output with the source-provided value.

## 🌐 Use SHA1 with `curl`

### 1️⃣ Download the File
- Use `curl` with the file URL:
  ```bash
  curl -O https://example.com/myfile.pkg
  ```

### 2️⃣ Generate the Checksum
- Run the SHA1 command:
  ```bash
  shasum -a 1 myfile.pkg
  ```

### 3️⃣ Verify Integrity
- Compare the generated checksum with the one provided by the source.

## 🚀 Example Workflow

1. **Download the file**:
   ```bash
   curl -O https://example.com/software.pkg
   ```
2. **Generate SHA1 checksum**:
   ```bash
   shasum -a 1 software.pkg
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
- [Understanding SHA1](https://en.wikipedia.org/wiki/SHA-1)
