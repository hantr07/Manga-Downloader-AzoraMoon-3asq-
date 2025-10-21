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
