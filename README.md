# 📚 Manga Downloader (AzoraMoon & 3asq)

A simple Python-based manga downloader for sites built with the **Madara** WordPress theme, including **AzoraMoon** and **3asq.com**.

These scripts use **Playwright** to render pages and **BeautifulSoup** to extract image links — allowing you to download full manga chapters easily.

---

## ⚙️ Features
- 🕹️ Uses Playwright (headless Chromium) for accurate page rendering  
- 🖼️ Downloads all chapter images with resume support  
- 📂 Organizes chapters automatically by manga title  
- 🧭 Supports chapter range filtering (`--from` and `--to`)  
- ⚡ Handles lazy-loaded images (`data-src` or `src`)  

---

## 📄 Files
| Script | Description |
|--------|-------------|
| **azoramoonV3.py** | General-purpose manga downloader for AzoraMoon and similar Madara-based sites |
| **3asq.py** | Optimized specifically for [3asq.org](https://3asq.org/) |

---

## 🧩 Requirements

### 🔧 Install dependencies
```bash
pip install -r requirements.txt
```

## 📦 Usage

### 🖥️ Download all chapters from a series
```bash
python azoramoonV3.py "https://azoramoon.com/series/manga-name/"
```

or for 3asq:
```bash
python 3asq.py "https://3asq.org/manga/manga-name/"
```
🔢 Download a specific range
```bash
python azoramoonV3.py "https://azoramoon.com/series/manga-name/" --from 5 --to 10
```
📘 Single chapter
```bash
python 3asq.py "https://3asq.org/manga/manga-name/chapter-12/"
```
## 🧾 Example Output

## When you run the script, you’ll see output like this:
```bash
📚 Manga: Solo_Leveling
✅ Found 200 chapters
🔢 Filtered to 10 chapters

=== Downloading chapter 5: https://azoramoon.com/series/solo-leveling/chapter-5 ===
  Found 28 images
[1/28] Downloading https://azoramoon.com/wp-content/uploads/solo-leveling-001.jpg
[2/28] Downloading https://azoramoon.com/wp-content/uploads/solo-leveling-002.jpg
...
✅ Chapter complete: Solo_Leveling/chapter-5/

