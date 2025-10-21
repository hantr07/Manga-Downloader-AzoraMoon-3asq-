#!/usr/bin/env python3
import sys
import os
import re
import argparse
import asyncio
import requests
from urllib.parse import urlparse
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"

# ---------------- Utils ---------------- #
def extract_chapter_number(slug: str) -> float:
    m = re.search(r"(\d+(\.\d+)?)", slug)
    if m:
        return float(m.group(1))
    return -1

# ---------------- Playwright HTML Fetch ---------------- #
async def fetch_html(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(3000)
        html = await page.content()
        await browser.close()
        return html

# ---------------- Chapter Image Extraction ---------------- #
async def fetch_chapter_images(chapter_url):
    html = await fetch_html(chapter_url)
    soup = BeautifulSoup(html, "html.parser")
    imgs = [img.get("data-src", img.get("src")).strip()
            for img in soup.select("img.wp-manga-chapter-img")]
    return imgs

def download_images(imgs, chapter_url, outdir):
    os.makedirs(outdir, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Referer": chapter_url})

    for i, url in enumerate(imgs, 1):
        ext = os.path.splitext(urlparse(url).path)[1] or ".jpg"
        fn = os.path.join(outdir, f"{i:03d}{ext}")

        if os.path.exists(fn):  # Resume support
            print(f"[{i}/{len(imgs)}] Skipping (already exists) {fn}")
            continue

        print(f"[{i}/{len(imgs)}] Downloading {url}")
        try:
            r = session.get(url, timeout=30)
            if r.status_code == 200:
                with open(fn, "wb") as f:
                    f.write(r.content)
            else:
                print("  ⚠️ Failed HTTP", r.status_code)
        except Exception as e:
            print("  ⚠️ Error:", e)

# ---------------- Series Chapter List ---------------- #
async def fetch_chapter_links(series_url):
    html = await fetch_html(series_url)
    soup = BeautifulSoup(html, "html.parser")

    # Manga title folder
    title = soup.select_one("h1")
    manga_title = title.text.strip().replace(" ", "_") if title else "Manga"

    chapters = [a["href"].strip() for a in soup.select("li.wp-manga-chapter a") if a.get("href")]
    chapters = chapters[::-1]  # oldest → newest

    chapters_with_num = []
    for chap in chapters:
        slug = os.path.basename(urlparse(chap).path.strip("/"))
        num = extract_chapter_number(slug)
        if num >= 0:
            chapters_with_num.append((num, chap))

    chapters_with_num.sort(key=lambda x: x[0])
    return manga_title, chapters_with_num

# ---------------- Main ---------------- #
async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Series or Chapter URL")
    parser.add_argument("--from", type=float, dest="from_ch", help="Start chapter number")
    parser.add_argument("--to", type=float, dest="to_ch", help="End chapter number")
    args = parser.parse_args()

    url = args.url

    if "/series/" in url and not url.rstrip("/").split("/")[-1].isdigit():
        # Series mode
        manga_title, chapters_with_num = await fetch_chapter_links(url)
        print(f"📚 Manga: {manga_title}")
        print(f"✅ Found {len(chapters_with_num)} chapters")

        if args.from_ch and args.to_ch:
            chapters_with_num = [c for c in chapters_with_num if args.from_ch <= c[0] <= args.to_ch]
            print(f"🔢 Filtered to {len(chapters_with_num)} chapters")

        for num, chap in chapters_with_num:
            folder = os.path.join(manga_title, os.path.basename(urlparse(chap).path.strip("/")) or f"chapter-{num}")
            if os.path.exists(folder) and os.listdir(folder):
                print(f"⏭ Skipping {folder} (already downloaded)")
                continue
            print(f"\n=== Downloading chapter {num}: {chap} ===")
            imgs = await fetch_chapter_images(chap)
            print(f"  Found {len(imgs)} images")
            download_images(imgs, chap, folder)

    else:
        # Single chapter
        html = await fetch_html(url)
        soup = BeautifulSoup(html, "html.parser")
        title = soup.select_one("h1")
        manga_title = title.text.strip().replace(" ", "_") if title else "Manga"

        print(f"📖 Fetching single chapter: {url}")
        imgs = await fetch_chapter_images(url)
        print(f"✅ Found {len(imgs)} images")
        folder = os.path.join(manga_title, os.path.basename(urlparse(url).path.strip("/")) or "chapter")
        download_images(imgs, url, folder)

if __name__ == "__main__":
    asyncio.run(main())
