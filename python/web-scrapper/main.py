from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import csv
import time
import json
from datetime import datetime
import random

# Configuração
CAMINHO_DRIVER = "./chromedriver"

def criar_driver_faang():
    """Cria driver otimizado para sites corporativos"""
    options = Options()
    
    # Configurações anti-detecção melhoradas
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # User agents rotativos
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]
    options.add_argument(f"--user-agent={random.choice(user_agents)}")
    
    # Para debug, comente a linha abaixo
    # options.add_argument("--headless")
    
    # Configurações de performance
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--window-size=1920,1080")
    
    try:
        driver = webdriver.Chrome(service=Service(CAMINHO_DRIVER), options=options)
        driver.set_page_load_timeout(60)
        driver.implicitly_wait(10)
        
        # Remove detecção de webdriver
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})")
        driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")
        
        return driver
    except Exception as e:
        print(f"❌ Erro ao criar driver: {e}")
        return None

# Configurações atualizadas das empresas FAANG
FAANG_SITES = {
    "Meta": {
        "url": "https://www.metacareers.com/jobs",
        "backup_url": "https://www.metacareers.com/jobs/?q=engineer",
        "wait_time": 10,
        "wait_selector": "div[data-testid='search-result-wrapper'], .fb-careers-job-search-results",
        "card_selector": "div[data-testid='search-result-wrapper'] a, .fb-careers-job-search-results a",
        "title_selector": "span[data-testid='job-title'], h3, .job-title",
        "location_selector": "span[data-testid='job-location'], .location",
        "base_url": "https://www.metacareers.com",
        "scroll_pause": 3
    },
    
    "Apple": {
        "url": "https://jobs.apple.com/en-br/search?location=brazil-BRA",
        "backup_url": "https://jobs.apple.com/en-us/search?search=engineer&location=brazil-BRA",
        "wait_time": 12,
        "wait_selector": "table[class*='table'] tbody tr, .job-search-results tr",
        "card_selector": "table[class*='table'] tbody tr",
        "title_selector": "a[id*='jobTitle'], td:first-child a",
        "location_selector": "td:nth-child(2)",
        "base_url": "https://jobs.apple.com",
        "scroll_pause": 2
    },
    
    "Amazon": {
        "url": "https://www.amazon.jobs/en/search?base_query=&loc_query=Brazil",
        "backup_url": "https://www.amazon.jobs/en/search?base_query=software&loc_query=Brazil",
        "wait_time": 8,
        "wait_selector": "div[data-test='job-tile'], .job-tile",
        "card_selector": "div[data-test='job-tile']",
        "title_selector": "h3[data-test='job-title'] a, h3 a",
        "location_selector": "p[data-test='job-location'], .location-and-id",
        "base_url": "https://www.amazon.jobs",
        "scroll_pause": 2
    },
    
    "Netflix": {
        "url": "https://jobs.netflix.com/search?q=&l=brazil",
        "backup_url": "https://jobs.netflix.com/search?q=engineer&l=brazil",
        "wait_time": 10,
        "wait_selector": ".job-card, .position-card, div[data-testid*='job']",
        "card_selector": ".job-card, .position-card",
        "title_selector": "h3 a, .job-title, .position-title",
        "location_selector": "span.location, .job-location",
        "base_url": "https://jobs.netflix.com",
        "scroll_pause": 3
    },
    
    "Google": {
        "url": "https://careers.google.com/jobs/results/?location=Brazil",
        "backup_url": "https://careers.google.com/jobs/results/?q=engineer&location=Brazil",
        "wait_time": 12,
        "wait_selector": ".gc-card, div[jsname], .job-tile",
        "card_selector": ".gc-card, div[jsname][role='listitem']",
        "title_selector": "h3, .gc-card__title, span[jsname]",
        "location_selector": "span[data-automation-id='job-location'], .gc-card__location",
        "base_url": "https://careers.google.com",
        "scroll_pause": 4
    }
}

# Palavras-chave técnicas expandidas
TECH_KEYWORDS = [
    # Cargos principais
    'software engineer', 'software developer', 'developer', 'engineer', 'programmer',
    'backend', 'frontend', 'full stack', 'fullstack', 'web developer',
    
    # Linguagens
    'python', 'java', 'javascript', 'typescript', 'go', 'golang', 'rust', 'c++', 'c#',
    'scala', 'kotlin', 'swift', 'php', 'ruby', 'node.js', 'nodejs',
    
    # Frameworks
    'react', 'angular', 'vue', 'django', 'spring', 'flask', 'express',
    
    # Áreas especializadas
    'machine learning', 'ml engineer', 'ai engineer', 'data engineer', 'data scientist',
    'devops', 'sre', 'cloud engineer', 'infrastructure', 'platform engineer',
    'mobile', 'ios developer', 'android developer', 'react native',
    'security engineer', 'cybersecurity', 'qa engineer', 'test engineer',
    
    # Cargos sênior
    'tech lead', 'technical lead', 'engineering manager', 'principal engineer',
    'senior developer', 'senior engineer', 'staff engineer', 'architect',
    'solution architect', 'software architect'
]

def eh_vaga_tech(texto):
    """Verifica se o texto contém palavras-chave técnicas"""
    if not texto:
        return False
    
    texto_lower = texto.lower()
    return any(keyword.lower() in texto_lower for keyword in TECH_KEYWORDS)

def aguardar_carregamento(driver, config, empresa):
    """Aguarda o carregamento da página com múltiplas estratégias"""
    print(f"⏳ Aguardando carregamento da página {empresa}...")
    
    # Aguarda inicial
    time.sleep(config['wait_time'])
    
    # Tenta aguardar pelos seletores
    try:
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, config['wait_selector'])))
        print("✅ Elementos detectados pelo seletor principal")
        return True
    except TimeoutException:
        print("⚠️ Timeout no seletor principal, tentando alternativas...")
        
        # Tenta aguardar por qualquer link ou botão
        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))
            print("✅ Página carregada (links detectados)")
            return True
        except TimeoutException:
            print("⚠️ Página pode não ter carregado completamente")
            return False

def fazer_scroll_inteligente(driver, config):
    """Faz scroll inteligente para carregar mais conteúdo"""
    print("📜 Fazendo scroll para carregar mais vagas...")
    
    altura_anterior = 0
    tentativas = 0
    max_tentativas = 5
    
    while tentativas < max_tentativas:
        # Scroll para baixo
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(config['scroll_pause'])
        
        # Verifica se a altura mudou (mais conteúdo carregou)
        altura_atual = driver.execute_script("return document.body.scrollHeight")
        
        if altura_atual == altura_anterior:
            tentativas += 1
        else:
            tentativas = 0  # Reset contador se carregou mais conteúdo
            
        altura_anterior = altura_atual
    
    print(f"📏 Scroll finalizado - Altura final: {altura_anterior}px")

def extrair_vagas_empresa(driver, empresa, config):
    """Extrai vagas de uma empresa FAANG específica"""
    print(f"\n🔍 === {empresa.upper()} ===")
    vagas = []
    
    try:
        # Tenta URL principal primeiro
        print(f"🌐 Tentativa 1 - Acessando: {config['url']}")
        driver.get(config['url'])
        
        if not aguardar_carregamento(driver, config, empresa):
            print("⚠️ Tentativa 2 - Usando URL backup...")
            driver.get(config['backup_url'])
            aguardar_carregamento(driver, config, empresa)
        
        print(f"📄 Título da página: {driver.title}")
        
        # Verifica se a página carregou corretamente
        if len(driver.page_source) < 5000:
            print("⚠️ Página muito pequena, pode não ter carregado")
            
        # Faz scroll para carregar mais vagas
        fazer_scroll_inteligente(driver, config)
        
        # Busca cards de vaga com múltiplas estratégias
        cards = []
        seletores = config['card_selector'].split(', ')
        
        for i, seletor in enumerate(seletores):
            try:
                print(f"🔍 Tentando seletor {i+1}: {seletor.strip()}")
                elementos = driver.find_elements(By.CSS_SELECTOR, seletor.strip())
                if elementos:
                    cards = elementos
                    print(f"✅ {len(cards)} elementos encontrados")
                    break
            except Exception as e:
                print(f"❌ Erro no seletor {i+1}: {str(e)[:50]}...")
                continue
        
        # Se não encontrou nada, tenta estratégias alternativas
        if not cards:
            print("🔍 Tentando estratégias alternativas...")
            estrategias = [
                "a[href*='job']",
                "div[class*='job']",
                "li[class*='job']",
                "[data-testid*='job']",
                "[data-test*='job']"
            ]
            
            for estrategia in estrategias:
                try:
                    elementos = driver.find_elements(By.CSS_SELECTOR, estrategia)
                    if elementos:
                        cards = elementos
                        print(f"✅ {len(cards)} elementos encontrados com estratégia: {estrategia}")
                        break
                except:
                    continue
        
        if not cards:
            print("❌ Nenhuma vaga encontrada")
            # Salva HTML para debug
            with open(f"debug_{empresa.lower()}_v2.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            print(f"💾 HTML salvo em debug_{empresa.lower()}_v2.html para análise")
            return vagas
        
        # Processa cada vaga
        vagas_tech = 0
        
        print(f"🔄 Processando {min(len(cards), 50)} vagas...")
        
        for i, card in enumerate(cards[:50]):  # Limita a 50 vagas
            try:
                # Extrai texto completo do card
                texto_card = card.text.strip()
                if len(texto_card) < 5:  # Skip cards vazios
                    continue
                
                # Extrai título com múltiplas estratégias
                titulo = None
                title_selectors = config['title_selector'].split(', ')
                
                for title_sel in title_selectors:
                    try:
                        title_elem = card.find_element(By.CSS_SELECTOR, title_sel.strip())
                        titulo = title_elem.text.strip()
                        if titulo and len(titulo) > 3:
                            break
                    except:
                        continue
                
                # Se não encontrou título, usa estratégias alternativas
                if not titulo:
                    try:
                        # Tenta primeiro link
                        link_elem = card.find_element(By.TAG_NAME, "a")
                        titulo = link_elem.text.strip()
                    except:
                        # Usa primeira linha do texto
                        linhas = texto_card.split('\n')
                        titulo = linhas[0] if linhas else "Título não encontrado"
                
                titulo = titulo[:150]  # Limita tamanho
                
                # Verifica se é vaga tech
                texto_completo = f"{titulo} {texto_card}".lower()
                if not eh_vaga_tech(texto_completo):
                    continue
                
                # Extrai localização
                localizacao = "Remote/Global"
                loc_selectors = config['location_selector'].split(', ')
                
                for loc_sel in loc_selectors:
                    try:
                        loc_elem = card.find_element(By.CSS_SELECTOR, loc_sel.strip())
                        loc_text = loc_elem.text.strip()
                        if loc_text and len(loc_text) > 1:
                            localizacao = loc_text
                            break
                    except:
                        continue
                
                # Extrai link
                link = config['base_url']
                try:
                    link_elem = card.find_element(By.TAG_NAME, "a")
                    href = link_elem.get_attribute("href")
                    if href:
                        if href.startswith("http"):
                            link = href
                        else:
                            link = config['base_url'] + href
                except:
                    try:
                        # Tenta o próprio card se for um link
                        href = card.get_attribute("href")
                        if href:
                            link = href if href.startswith("http") else config['base_url'] + href
                    except:
                        pass
                
                vagas_tech += 1
                print(f"  ✅ {vagas_tech}. {titulo[:80]}...")
                print(f"     📍 {localizacao}")
                
                vagas.append({
                    "empresa": empresa,
                    "titulo": titulo,
                    "localizacao": localizacao,
                    "link": link,
                    "data_busca": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                
            except Exception as e:
                print(f"⚠️ Erro ao processar vaga {i+1}: {str(e)[:50]}...")
                continue
        
        print(f"🎯 {empresa}: {vagas_tech} vagas de tecnologia encontradas")
        
    except Exception as e:
        print(f"❌ Erro geral em {empresa}: {str(e)[:100]}...")
        # Salva página de erro para debug
        try:
            with open(f"error_{empresa.lower()}.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
        except:
            pass
    
    return vagas

def salvar_resultados_faang(todas_vagas):
    """Salva resultados com informações detalhadas"""
    if not todas_vagas:
        print("⚠️ Nenhuma vaga encontrada para salvar")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    
    # Salva CSV
    try:
        filename_csv = f"vagas_faang_{timestamp}.csv"
        with open(filename_csv, "w", newline="", encoding="utf-8") as f:
            campos = ["empresa", "titulo", "localizacao", "link", "data_busca"]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(todas_vagas)
        
        print(f"\n💾 {len(todas_vagas)} vagas salvas em '{filename_csv}'")
    except Exception as e:
        print(f"❌ Erro ao salvar CSV: {e}")
    
    # Salva JSON com mais detalhes
    try:
        filename_json = f"vagas_faang_{timestamp}.json"
        with open(filename_json, "w", encoding="utf-8") as f:
            json.dump(todas_vagas, f, indent=2, ensure_ascii=False)
        print(f"💾 Dados detalhados salvos em '{filename_json}'")
    except Exception as e:
        print(f"❌ Erro ao salvar JSON: {e}")
    
    # Mostra estatísticas detalhadas
    print(f"\n📊 ESTATÍSTICAS FAANG:")
    stats = {}
    for vaga in todas_vagas:
        empresa = vaga["empresa"]
        stats[empresa] = stats.get(empresa, 0) + 1
    
    total = len(todas_vagas)
    print(f"🎯 Total de vagas: {total}")
    print("-" * 40)
    
    for empresa, count in sorted(stats.items()):
        porcentagem = (count / total) * 100 if total > 0 else 0
        print(f"  🏢 {empresa:8}: {count:3} vagas ({porcentagem:5.1f}%)")

def main():
    """Função principal para buscar vagas FAANG"""
    print("🚀 FAANG JOB SCRAPER V2 - OTIMIZADO")
    print("=" * 60)
    print("🎯 Buscando vagas de tecnologia em:")
    print("   • Meta (Facebook)")
    print("   • Apple") 
    print("   • Amazon")
    print("   • Netflix")
    print("   • Google")
    print("=" * 60)
    
    # Inicializa driver
    driver = criar_driver_faang()
    if not driver:
        print("❌ Falha ao inicializar driver")
        return
    
    todas_vagas = []
    empresas_processadas = 0
    empresas_sucesso = 0
    
    try:
        for empresa, config in FAANG_SITES.items():
            print(f"\n{'='*25} {empresas_processadas + 1}/5 {'='*25}")
            
            # Delay entre empresas para evitar bloqueios
            if empresas_processadas > 0:
                delay = random.randint(8, 15)
                print(f"⏳ Aguardando {delay}s antes da próxima empresa...")
                time.sleep(delay)
            
            vagas_empresa = extrair_vagas_empresa(driver, empresa, config)
            
            if vagas_empresa:
                todas_vagas.extend(vagas_empresa)
                empresas_sucesso += 1
                print(f"✅ {empresa} processado com sucesso!")
            else:
                print(f"⚠️ {empresa} não retornou vagas")
            
            empresas_processadas += 1
            print(f"📈 Total acumulado: {len(todas_vagas)} vagas de {empresas_sucesso} empresas")
    
    except KeyboardInterrupt:
        print("\n⚠️ Processo interrompido pelo usuário")
    
    finally:
        print("\n🔒 Fechando navegador...")
        driver.quit()
    
    # Salva e mostra resultados
    if todas_vagas:
        salvar_resultados_faang(todas_vagas)
        print(f"\n🎉 SUCESSO! {len(todas_vagas)} vagas encontradas em {empresas_sucesso}/5 empresas FAANG!")
        print(f"📄 Verifique os arquivos CSV e JSON gerados com timestamp")
    else:
        print(f"\n⚠️ Nenhuma vaga encontrada")
        print(f"💡 Dicas para debug:")
        print(f"   1. Descomente a linha --headless para ver o browser")
        print(f"   2. Verifique os arquivos debug_*.html gerados")
        print(f"   3. Alguns sites podem ter bloqueado o acesso")
        print(f"   4. Verifique sua conexão com a internet")

if __name__ == "__main__":
    main()