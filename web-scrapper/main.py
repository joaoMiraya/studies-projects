from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

CAMINHO_DRIVER = "./chromedriver"
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(CAMINHO_DRIVER), options=options)
palavras_chave = ['desenvolvedor', 'desenvolvimento', 'developer', 'backend', 'frontend', 'full stack', 'engenheiro de software']

sites = [
    {
        "nome": "IBM",
        "url": "https://www.ibm.com/br-pt/careers/search",
        "card_selector": ".bx--card-group__card",
        "title_selector": ".bx--card__heading",
        "link_attr": "href",
        "base_url": "https://www.ibm.com",
        "usa_data_href": False
    },
    {
        "nome": "InfoJobs",
        "url": "https://www.infojobs.com.br/vagas-de-desenvolvedor.aspx",
        "card_selector": ".js_cardLink[data-href]",
        "title_selector": "h2",
        "link_attr": "data-href",
        "base_url": "https://www.infojobs.com.br",
        "usa_data_href": True
    }
]

resultados = []

for site in sites:
    print(f"\n🔍 Raspando vagas do site: {site['nome']}")
    driver.get(site["url"])

    try:
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, site["card_selector"])))

        cards = driver.find_elements(By.CSS_SELECTOR, site["card_selector"])

        for i, card in enumerate(cards, start=1):
            try:
                titulo = card.find_element(By.CSS_SELECTOR, site["title_selector"]).text.strip().lower()
                if not any(palavra in titulo for palavra in palavras_chave):
                    continue  # pula se não for vaga de dev

                link = card.get_attribute(site["link_attr"])
                if not link and site["usa_data_href"]:
                    link = card.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                if link and not link.startswith("http"):
                    link = site["base_url"] + link

                print(f"{i}. {titulo}\n   Link: {link}")
                resultados.append({"site": site["nome"], "titulo": titulo, "link": link})

            except Exception as e:
                print(f"[!] Erro ao processar card: {e}")

    except Exception as e:
        print(f"[!] Falha ao acessar {site['nome']}: {e}")

driver.quit()

# Salvar no CSV
with open("vagas.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["site", "titulo", "link"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(resultados)
