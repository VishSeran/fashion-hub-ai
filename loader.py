from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

URL = "https://www.daraz.lk/fashion/?page=2&spm=a2a0e.pdp_revamp.breadcrumb.1.4f807b893c0Rnw"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=["--disable-blink-features=AutomationControlled"],
    )
    context = browser.new_context(
    user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    viewport={"width": 390, "height": 844},
    is_mobile=True,
    )
    page = context.new_page()

    page.goto(URL, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector('[data-qa-locator="product-item"]', timeout=30000)

    # scroll through the whole page to trigger lazy-loaded images
    prev_height = 0
    for _ in range(15):
        page.mouse.wheel(0, 2000)
        page.wait_for_timeout(600)  # NEEDED - gives lazy images time to load before we check height again
        height = page.evaluate("document.body.scrollHeight")
        if height == prev_height:
            break
        prev_height = height

    # after scrolling settles, wait (with a timeout guard) for images to resolve to real URLs
    try:
        page.wait_for_function(
            "document.querySelectorAll('[data-qa-locator=\"product-item\"] img').length > 0 && "
            "Array.from(document.querySelectorAll('[data-qa-locator=\"product-item\"] img'))"
            ".every(img => img.src.startsWith('http'))",
            timeout=10000,
        )
    except Exception:
        print("Warning: not all product images resolved to real URLs in time - some may still be base64 placeholders.")

    html = page.content()
    browser.close()

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())