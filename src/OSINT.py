import feedparser
import re
from datetime import datetime
from collections import defaultdict

# --- KONFİGÜRASYON ---
# 1. Çoklu Kaynak (Multi-Source)
RSS_SOURCES = {
    "NVD (NIST)": "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss.xml",
    "Exploit-DB": "https://www.exploit-db.com/rss.xml",
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "BleepingComputer": "https://www.bleepingcomputer.com/feed/"
}

# 2. Akıllı Sınıflandırma için Anahtar Kelimeler (Basit NLP)
KEYWORDS = {
    "Web Security": ["xss", "sql injection", "csrf", "wordpress", "php", "html", "browser"],
    "Network": ["dos", "ddos", "tcp", "udp", "port", "firewall", "router", "cisco"],
    "Crypto/Ransomware": ["ransomware", "crypto", "bitcoin", "encryption", "decrypt", "wallet"],
    "Exploit/Zero-Day": ["rce", "buffer overflow", "zero-day", "0-day", "exploit", "poc"],
    "Linux/Kernel": ["linux", "kernel", "ubuntu", "redhat", "bash", "root"]
}

class CyberNewsAggregator:
    def __init__(self):
        self.news_pool = []
        self.verified_news = []

    def fetch_feeds(self):
        """RSS kaynaklarından verileri çeker."""
        print(f"[*] {len(RSS_SOURCES)} kaynaktan veri çekiliyor...")
        for source_name, url in RSS_SOURCES.items():
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries[:10]: # Her kaynaktan son 10 haberi al
                    item = {
                        "source": source_name,
                        "title": entry.title,
                        "link": entry.link,
                        "summary": getattr(entry, "summary", entry.title).lower(), # NLP için küçük harfe çevir
                        "published": getattr(entry, "published", str(datetime.now())),
                        "cve_ids": self.extract_cves(entry.title + " " + getattr(entry, "summary", "")),
                        "tags": [],
                        "impact_score": 0,
                        "confidence_score": 1 # Varsayılan güven skoru
                    }
                    self.news_pool.append(item)
            except Exception as e:
                print(f"[!] Hata ({source_name}): {e}")

    def extract_cves(self, text):
        """Metin içindeki CVE kodlarını (örn: CVE-2024-1234) regex ile bulur."""
        return list(set(re.findall(r'cve-\d{4}-\d{4,7}', text, re.IGNORECASE)))

    def process_news(self):
        """Sınıflandırma ve Puanlama işlemlerini yapar."""
        print("[*] Haberler işleniyor ve sınıflandırılıyor...")
        
        for item in self.news_pool:
            # --- Akıllı Sınıflandırma (NLP/Keyword Matching) ---
            text_to_scan = item["title"].lower() + " " + item["summary"]
            for category, words in KEYWORDS.items():
                if any(word in text_to_scan for word in words):
                    item["tags"].append(category)
            
            if not item["tags"]:
                item["tags"].append("General Info")

            # --- Puanlama (Ranking) ---
            # CVE varsa puanı artır
            if item["cve_ids"]:
                item["impact_score"] += 50
            
            # Kritik kelimeler varsa puanı artır
            if "critical" in text_to_scan: item["impact_score"] += 30
            if "high" in text_to_scan: item["impact_score"] += 20
            if "rce" in text_to_scan or "remote code execution" in text_to_scan: item["impact_score"] += 25
            
            # NVD gibi resmi kaynaklar daha güvenilirdir (Weighting)
            if "NVD" in item["source"]:
                item["impact_score"] += 10

    def cross_reference_and_verify(self):
        """
        Doğrulama: Aynı CVE veya benzer başlık birden fazla kaynakta geçiyor mu?
        Buna göre Güven Skoru (Confidence Score) oluşturur.
        """
        print("[*] Doğrulama ve Çapraz Kontrol yapılıyor...")
        
        # CVE'ye göre gruplama
        cve_map = defaultdict(list)
        unique_news = []
        seen_titles = set()

        for item in self.news_pool:
            # Eğer CVE varsa, CVE üzerinden doğrulama yap
            if item["cve_ids"]:
                for cve in item["cve_ids"]:
                    cve_map[cve].append(item)
            
            # Basit başlık kontrolü (Duplicate önleme)
            # Daha gelişmiş versiyonda 'Cosine Similarity' kullanılabilir.
            if item["title"] not in seen_titles:
                unique_news.append(item)
                seen_titles.add(item["title"])

        # CVE bazlı güven skoru artırma
        for cve, items in cve_map.items():
            if len(items) > 1: # Birden fazla kaynak aynı CVE'den bahsetmiş
                for item in unique_news:
                    if cve in item["cve_ids"]:
                        item["confidence_score"] += (len(items) - 1) * 2 # Kaynak başına puan ekle
                        item["source"] += f" (+{len(items)-1} diğer kaynak)"

        # Sonuçları önem derecesine göre sırala (High Impact en üstte)
        self.verified_news = sorted(unique_news, key=lambda x: x["impact_score"], reverse=True)

    def display_report(self):
        """Sonuçları terminale basar."""
        print("\n" + "="*60)
        print("SİBER GÜVENLİK TEHDİT RAPORU")
        print("="*60 + "\n")

        for item in self.verified_news[:15]: # En önemli 15 haberi göster
            # Renklendirme (Linux Terminal için ANSI kodları)
            color = "\033[92m" # Yeşil (Düşük)
            if item["impact_score"] > 50: color = "\033[93m" # Sarı (Orta)
            if item["impact_score"] > 80: color = "\033[91m" # Kırmızı (Kritik)
            reset = "\033[0m"

            print(f"{color}[SKOR: {item['impact_score']}] [GÜVEN: {item['confidence_score']}]{reset} {item['title']}")
            print(f"   Kaynak: {item['source']}")
            print(f"   Kategori: {', '.join(item['tags'])}")
            if item["cve_ids"]:
                print(f"   CVE ID: {', '.join(item['cve_ids'])}")
            print("-" * 60)

if __name__ == "__main__":
    bot = CyberNewsAggregator()
    bot.fetch_feeds()
    bot.process_news()
    bot.cross_reference_and_verify()
    bot.display_report()
