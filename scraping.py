import os
import requests
from bs4 import BeautifulSoup

# Dictionary of Wikipedia topics and their URLs
wiki_pages = {
    "General Culture & Heritage": "https://en.wikipedia.org/wiki/Culture_of_India",
    "Cultural Heritage of India": "https://en.wikipedia.org/wiki/Cultural_heritage_of_India",
    "History of India": "https://en.wikipedia.org/wiki/History_of_India",
    "Indian Society": "https://en.wikipedia.org/wiki/Society_of_India",
    "Demographics of India": "https://en.wikipedia.org/wiki/Demographics_of_India",
    "List of Festivals in India": "https://en.wikipedia.org/wiki/List_of_festivals_in_India",
    "Diwali": "https://en.wikipedia.org/wiki/Diwali",
    "Holi": "https://en.wikipedia.org/wiki/Holi",
    "Navratri": "https://en.wikipedia.org/wiki/Navratri",
    "Pongal": "https://en.wikipedia.org/wiki/Pongal_(festival)",
    "Raksha Bandhan": "https://en.wikipedia.org/wiki/Raksha_Bandhan",
    "Eid in India": "https://en.wikipedia.org/wiki/Eid_al-Fitr#India",
    "Christmas in India": "https://en.wikipedia.org/wiki/Christmas_in_India",
    "Onam": "https://en.wikipedia.org/wiki/Onam",
    "Indian Classical Dance": "https://en.wikipedia.org/wiki/Indian_classical_dance",
    "List of Indian Folk Dances": "https://en.wikipedia.org/wiki/List_of_Indian_folk_dances",
    "Theatre in India": "https://en.wikipedia.org/wiki/Theatre_in_India",
    "Puppetry in India": "https://en.wikipedia.org/wiki/Puppetry_in_India",
    "Kathakali": "https://en.wikipedia.org/wiki/Kathakali",
    "Bharatanatyam": "https://en.wikipedia.org/wiki/Bharatanatyam",
    "Music of India": "https://en.wikipedia.org/wiki/Music_of_India",
    "Indian Classical Music": "https://en.wikipedia.org/wiki/Indian_classical_music",
    "Hindustani Music": "https://en.wikipedia.org/wiki/Hindustani_classical_music",
    "Carnatic Music": "https://en.wikipedia.org/wiki/Carnatic_music",
    "Folk Music of India": "https://en.wikipedia.org/wiki/Folk_music_of_India",
    "Bollywood": "https://en.wikipedia.org/wiki/Bollywood",
    "Tollywood": "https://en.wikipedia.org/wiki/Tollywood_(disambiguation)",
    "Kollywood": "https://en.wikipedia.org/wiki/Tamil_cinema",
    "Sandalwood": "https://en.wikipedia.org/wiki/Kannada_cinema",
    "Indian Film Industry": "https://en.wikipedia.org/wiki/Cinema_of_India",
    "Indian Literature": "https://en.wikipedia.org/wiki/Indian_literature",
    "Sanskrit Literature": "https://en.wikipedia.org/wiki/Sanskrit_literature",
    "Tamil Literature": "https://en.wikipedia.org/wiki/Tamil_literature",
    "Hindi Literature": "https://en.wikipedia.org/wiki/Hindi_literature",
    "Bengali Literature": "https://en.wikipedia.org/wiki/Bengali_literature",
    "Languages of India": "https://en.wikipedia.org/wiki/Languages_of_India",
    "Indian Cuisine": "https://en.wikipedia.org/wiki/Indian_cuisine",
    "List of Indian Beverages": "https://en.wikipedia.org/wiki/List_of_Indian_beverages",
    "List of Indian Sweets and Desserts": "https://en.wikipedia.org/wiki/List_of_Indian_sweets_and_desserts",
    "Regional Indian Cuisines": "https://en.wikipedia.org/wiki/Regional_cuisines_of_India",
    "Street Food in India": "https://en.wikipedia.org/wiki/Street_food_of_India",
    "Vegetarianism in India": "https://en.wikipedia.org/wiki/Vegetarianism_in_India",
    "Indian Architecture": "https://en.wikipedia.org/wiki/Architecture_of_India",
    "Mughal Architecture": "https://en.wikipedia.org/wiki/Mughal_architecture",
    "Dravidian Architecture": "https://en.wikipedia.org/wiki/Dravidian_architecture",
    "Buddhist Architecture": "https://en.wikipedia.org/wiki/Buddhist_architecture",
    "Taj Mahal": "https://en.wikipedia.org/wiki/Taj_Mahal",
    "Qutub Minar": "https://en.wikipedia.org/wiki/Qutb_Minar",
    "List of World Heritage Sites in India": "https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_India",
    "Hinduism in India": "https://en.wikipedia.org/wiki/Hinduism_in_India",
    "Buddhism in India": "https://en.wikipedia.org/wiki/Buddhism_in_India",
    "Jainism in India": "https://en.wikipedia.org/wiki/Jainism_in_India",
    "Sikhism in India": "https://en.wikipedia.org/wiki/Sikhism_in_India",
    "Islam in India": "https://en.wikipedia.org/wiki/Islam_in_India",
    "Christianity in India": "https://en.wikipedia.org/wiki/Christianity_in_India",
    "Indian Philosophy": "https://en.wikipedia.org/wiki/Indian_philosophy",
    "Bhagavad Gita": "https://en.wikipedia.org/wiki/Bhagavad_Gita",
    "Vedas": "https://en.wikipedia.org/wiki/Vedas",
    "Upanishads": "https://en.wikipedia.org/wiki/Upanishads"
}

# Create directory if it doesn't exist
os.makedirs("indian_culture", exist_ok=True)

def scrape_and_save(title, url):
    """Scrape the Wikipedia page and save its content to a text file."""
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extracting text from paragraphs
        paragraphs = soup.find_all("p")
        content = "\n".join([para.get_text() for para in paragraphs if para.get_text().strip()])
        
        # Save content to a text file
        filename = f"indian_culture/{title.replace(' ', '_')}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        
        print(f"Saved: {title}")
    else:
        print(f"Failed to retrieve {title} ({url})")

# Scrape each Wikipedia page and save the content
for title, url in wiki_pages.items():
    scrape_and_save(title, url)

print("Scraping completed successfully! 🎉")
