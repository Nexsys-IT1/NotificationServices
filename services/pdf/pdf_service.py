from playwright.async_api import async_playwright


class PDFService:

    async def generate_pdf_from_html(self, html: str) -> bytes:
        if not html:
            raise ValueError("HTML content is empty")

        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.set_content(html)
            pdf = await page.pdf(format="A4")
            await browser.close()
            return pdf
