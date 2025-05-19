import requests
from bs4 import BeautifulSoup

def extract_data():
    all_data = []

    for page in range(1, 51):
        url = f"https://fashion-studio.dicoding.dev?page={page}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        cards = soup.find_all("div", class_="collection-card")
        if not cards:
            continue

        for card in cards:
            title_tag = card.find("h3", class_="product-title")
            title = title_tag.text.strip() if title_tag else "Unknown Product"

            price_tag = card.find("span", class_="price") or card.find("p", class_="price")
            price = price_tag.text.strip().replace("$", "") if price_tag else "Price Unavailable"

            rating, colors, size, gender = None, None, None, None

            p_tags = card.find_all("p")
            for p in p_tags:
                text = p.text.strip()
                if "Rating" in text:
                    rating = text
                elif "Colors" in text:
                    colors = text
                elif "Size:" in text:
                    size = text
                elif "Gender:" in text:
                    gender = text

            all_data.append({
                "title": title,
                "price": price,
                "rating": rating,
                "colors": colors,
                "size": size,
                "gender": gender
            })

    return all_data
