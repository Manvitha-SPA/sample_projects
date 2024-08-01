from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver.common.by import By
import os
from datetime import datetime
# Initialize the WebDriver
def get_images(url):


    wd = webdriver.Chrome()

    # URL of the webpage you want to scrape

    # Open the webpage
    wd.get(url)

    restaurant_name = wd.find_element(By.TAG_NAME,'h1').text

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

    folder_name = f"{restaurant_name}_{timestamp}"

    folder_path = os.path.join(os.getcwd(), folder_name)
    os.makedirs(folder_path, exist_ok=True)


    go_to_photos = WebDriverWait(wd, 2).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Photos"))
    )
    go_to_photos.click()


    wd.execute_script(f"window.scrollTo(0, window.scrollY +200 )")

    # Wait for the "Load more" button to be present (maximum wait time: 10 seconds)
    load_more_button = WebDriverWait(wd, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-s1isp7-5.eisbVA"))
    )

    # Click the "Load more" button
    load_more_button.click()



    # Wait for the page to load (you may need to adjust the wait time)
    wd.implicitly_wait(10)

    # Get the page source after clicking "Load more"
    page_source = wd.page_source



    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")




    image_elements = soup.find_all("img")
    image_urls = [img["src"] for img in image_elements]


    # Print the first 10 image URLs
    def get_image():
        images_info = {}
        for i, img_url in enumerate(image_urls[:12], start=1):
            image_url = img_url.split('?')
            images_info[i] = image_url[0]

        return images_info

    images = get_image()
    images_id = []
    image_values = []
    for id in images:
        images_id.append(id)
    for url in images:
        if images[url] not in image_values:
            image_values.append(images[url])
        
    for i, image_url in enumerate(image_values[2:], start=1):
        if image_url:
            # Construct the full file path including the folder and image filename
            filename = os.path.join(folder_path, f'image_{i}.jpg')

            # Download and save the image in the specified folder
            urllib.request.urlretrieve(image_url, filename)
            print(f'Downloaded {filename}')



    # Close the WebDriver
    wd.quit()

