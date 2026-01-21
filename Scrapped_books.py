import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://books.toscrape.com/"


def get_page_soup(url):
    try:
        response = requests.get(url)
        return BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print("Error while loading page:", e)
        return None


def get_rating(star_tag):
    rating_word = star_tag["class"][1]

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    return rating_map.get(rating_word, 0)


def get_category(book_url):
    soup = get_page_soup(book_url)
    if soup is None:
        return ""

    breadcrumb = soup.select("ul.breadcrumb li a")
    if breadcrumb:
        return breadcrumb[-1].text.strip()

    return ""


def scrape_books():
    all_books = []

    for page in range(1, 5):
        print(f"Scraping page {page}")

        page_url = f"{URL}catalogue/page-{page}.html"
        soup = get_page_soup(page_url)

        if soup is None:
            continue

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]

            price_text = book.find("p", class_="price_color").text
            price = price_text.replace("£", "").replace("Â", "").strip()
            price = float(price)

            availability = book.find(
                "p", class_="instock availability"
            ).text.strip()

            rating = get_rating(book.find("p", class_="star-rating"))

            relative_url = book.h3.a["href"]
            book_url = URL + "catalogue/" + relative_url.replace("../", "")

            category = get_category(book_url)

            all_books.append({
                "Title": title,
                "Category": category,
                "Price": price,
                "Availability": availability,
                "Rating": rating,
                "Product URL": book_url
            })

            time.sleep(0.3)

    return all_books


def main():
    data = scrape_books()
    df = pd.DataFrame(data)
    df.to_csv("books_data.csv", index=False)
    print("Scraping completed successfully!")


if __name__ == "__main__":
    main()
