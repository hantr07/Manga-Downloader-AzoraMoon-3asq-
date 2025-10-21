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
| **3asq.py** | Optimized specifically for [3asq.org](https://3asq.org/) / [3asq.com](https://3asq.com) |

---

## 🧩 Requirements

### 🔧 Install dependencies
```bash
pip install -r requirements.txt
```
🌐 Install Playwright browsers
playwright install


Requires Python 3.8+

📦 Usage
🖥️ Download all chapters from a series
python azoramoonV3.py "https://azoramoon.com/series/manga-name/"


or for 3asq:

python 3asq.py "https://3asq.org/manga/manga-name/"

🔢 Download a specific range
python azoramoonV3.py "https://azoramoon.com/series/manga-name/" --from 5 --to 10

📘 Single chapter
python 3asq.py "https://3asq.org/manga/manga-name/chapter-12/"

🧾 Example Output

When you run the script, you’ll see output like this:

📚 Manga: Solo_Leveling
✅ Found 200 chapters
🔢 Filtered to 10 chapters

=== Downloading chapter 5: https://azoramoon.com/series/solo-leveling/chapter-5 ===
  Found 28 images
[1/28] Downloading https://azoramoon.com/wp-content/uploads/solo-leveling-001.jpg
[2/28] Downloading https://azoramoon.com/wp-content/uploads/solo-leveling-002.jpg
...
✅ Chapter complete: Solo_Leveling/chapter-5/


If a chapter already exists, it will automatically skip it:

⏭ Skipping chapter-4 (already exists)

🗂️ Output Structure

Downloaded chapters are organized automatically:

Manga_Title/
├── chapter-1/
│   ├── 001.jpg
│   ├── 002.jpg
│   └── ...
├── chapter-2/
│   ├── 001.jpg
│   └── ...

🧠 Notes

For educational and personal use only.

Avoid spamming requests or downloading entire sites in one go.

Works best on Madara-based WordPress manga readers.
