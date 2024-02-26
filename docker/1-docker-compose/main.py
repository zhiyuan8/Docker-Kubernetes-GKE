from fastapi import FastAPI, HTTPException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from pydantic import BaseModel
import uvicorn  # Import uvicorn to run the server programmatically
from typing import Optional
import os

app = FastAPI()

class ScrawlRequest(BaseModel):
    url: str
    max_retries: Optional[int] = 3
    timeout: Optional[int] = 120

@app.post("/scrawl/")
async def scrawl_website(request: ScrawlRequest):
    response = selenium_read_webpage(
        request.url,
        request.max_retries,
        request.timeout
    )
    return {"content": response}

@app.get("/")
async def health_check():
    return {"message": "Healthy"}

def selenium_read_webpage(url, max_retries=3, timeout=120):
    # Define Chrome options
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument("--no-sandbox")

    # Use SELENIUM_URL from environment variables, with a fallback default
    selenium_grid_url = os.getenv('SELENIUM_URL', 'http://localhost:4444/wd/hub')

    attempts = 0
    while attempts < max_retries:
        try:
            # Connect to remote browser (Docker container)
            driver = webdriver.Remote(
                command_executor=selenium_grid_url, options=chrome_options
            )

            # Get the response with a timeout
            driver.get(url)
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            soup = BeautifulSoup(driver.page_source, "html.parser")
            text = soup.get_text(separator=" ", strip=True)
            driver.quit()  # Make sure to quit the driver to free resources
            return text
        except TimeoutException as e:
            print(f"TimeoutException for {url}: {e}")
            driver.quit()
            if attempts == max_retries - 1:
                return "Failed to load page within timeout limit."
        except Exception as e:
            print(f"Exception while fetching text from {url}: {e}")
            driver.quit()
            if attempts == max_retries - 1:
                return "An error occurred while loading the page."
        finally:
            attempts += 1

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)