from bs4 import BeautifulSoup
import requests
import os
import re

def clean_filename(title):
    """Nettoie le titre pour en faire un nom de fichier valide."""
    title = re.sub(r'[\\/*?:"<>|]', "", title)  # Retire les caractères interdits
    title = re.sub(r'\s+', '_', title)           # Remplace les espaces par des underscores
    return title.strip()[:100]                   # Coupe à 100 caractères max

def scrape_page(url):
    """Scrape une page et extrait son titre et son contenu."""
    try:
        HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'} # Pour éviter l'erreur 403
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        
        title = soup.title.string.strip() if soup.title else "Titre_non_disponible"
        
        article_content = ""
        article_tags = soup.find_all("p", class_=lambda x: x and "article__paragraph" in x.lower())
        if not article_tags:
            article_tags = soup.find_all("p")
        
        for tag in article_tags:
            article_content += tag.get_text(separator=" ", strip=True) + "\n"
        
        if not article_content.strip():
            article_content = "Contenu non disponible"
        
        print(f"Scrapé : {url}\nTitre : {title}\n---\n")
        return title, article_content
    except Exception as e:
        print(f"Erreur lors du scraping de {url} : {e}")
        return None, None

def scrape_from_file(file_path, output_dir):
    """Lit les URLs depuis un fichier et sauvegarde chaque article dans un fichier individuel."""
    try:
        os.makedirs(output_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas
        
        with open(file_path, "r", encoding="utf-8") as file:
            urls = [url.strip() for url in file.readlines() if url.strip()]
        
        for idx, url in enumerate(urls, start=1):
            title, content = scrape_page(url)
            if title and content:
                safe_title = clean_filename(title)
                filename = f"{idx:03d}_{safe_title}.txt"
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "w", encoding="utf-8") as output:
                    output.write(f"{title}\n\n{content}")
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier {file_path} : {e}")

# Configuration des fichiers
input_file = "articles-sport.txt"
output_dir = "articles_sport"

# Exécution du scraping
scrape_from_file(input_file, output_dir)

print(f"Scraping terminé, articles enregistrés dans le dossier '{output_dir}'")