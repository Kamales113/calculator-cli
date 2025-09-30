import requests
from bs4 import BeautifulSoup

def scrape_news_headlines():
    """
    Scrapes top news headlines from BBC News website
    """
    try:
        # URL of the news website (BBC News in this case)
        url = "https://www.bbc.com/news"
        
        # Send GET request to the website
        print("Fetching data from BBC News...")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract headlines - BBC uses h3 with specific class for headlines
        # You may need to adjust these selectors based on the website structure
        headlines = []
        
        # Method 1: Look for h2 tags
        h2_headlines = soup.find_all('h2')
        for h2 in h2_headlines:
            headline_text = h2.get_text().strip()
            if headline_text and len(headline_text) > 10:  # Filter out short texts
                headlines.append(headline_text)
        
        # Method 2: Look for h3 tags (common for BBC News)
        h3_headlines = soup.find_all('h3')
        for h3 in h3_headlines:
            headline_text = h3.get_text().strip()
            if headline_text and len(headline_text) > 10:  # Filter out short texts
                headlines.append(headline_text)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_headlines = []
        for headline in headlines:
            if headline not in seen:
                seen.add(headline)
                unique_headlines.append(headline)
        
        # Save to text file
        with open('news_headlines.txt', 'w', encoding='utf-8') as file:
            file.write("TOP NEWS HEADLINES\n")
            file.write("=" * 50 + "\n\n")
            for i, headline in enumerate(unique_headlines[:20], 1):  # Save top 20 headlines
                file.write(f"{i}. {headline}\n")
        
        print(f"Successfully scraped {len(unique_headlines[:20])} headlines!")
        print("Headlines saved to 'news_headlines.txt'")
        
        # Display first 5 headlines in console
        print("\nFirst 5 headlines:")
        print("-" * 30)
        for i, headline in enumerate(unique_headlines[:5], 1):
            print(f"{i}. {headline}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Alternative function for a different news website
def scrape_alternative_news():
    """
    Alternative function for CNN News (commented out as example)
    """
    try:
        url = "https://edition.cnn.com/world"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # CNN specific selectors
        headlines = []
        news_elements = soup.find_all(['h2', 'h3', 'span'], class_=lambda x: x and 'headline' in x.lower())
        
        for element in news_elements:
            text = element.get_text().strip()
            if text and len(text) > 15:
                headlines.append(text)
        
        return headlines[:15]
        
    except Exception as e:
        print(f"Error scraping alternative news: {e}")
        return []

if __name__ == "__main__":
    # Execute the main scraping function
    scrape_news_headlines()