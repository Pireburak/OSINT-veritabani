# Prompts for deepseek
"Bir domain hakkında derinlemesine teknik OSINT araştırması yap:

HEDEF DOMAIN: [example.com]

ARAŞTIRMA ADIMLARI:

1. TEMEL BİLGİ TOPLAMA:
   • WHOIS sorgusu (kayıt bilgileri)
   • DNS kayıtları (A, MX, TXT, CNAME)
   • Subdomain keşfi (subfinder, amass)
   • SSL/TLS sertifika bilgileri

2. TEKNİK ALTYAPI:
   • Hosting bilgileri (IP, hosting firması)
   • IP geçmişi ve coğrafi lokasyon
   • Kullanılan teknolojiler (Wappalyzer)
   • Port taraması (shodan.io sorgusu)

3. İÇERİK ANALİZİ:
   • Wayback Machine ile arşiv taraması
   • Robots.txt ve sitemap.xml analizi
   • Public kod depoları (GitHub, GitLab)
   • API endpoint'lerinin tespiti

4. GÜVENLİK DEĞERLENDİRMESİ:
   • Güvenlik açığı taraması
   • SSL konfigürasyon analizi
   • Email güvenlik kayıtları (SPF, DKIM, DMARC)
   • Honeypot veritabanı kontrolleri

5. İLİŞKİLİ VARLIKLAR:
   • Aynı IP'de barınan diğer siteler
   • Aynı şirkete kayıtlı diğer domainler
   • Benzer DNS yapısına sahip siteler

KULLANILACAK ARAÇLAR:
• whois, dig, nslookup
• Shodan, Censys, VirusTotal
• theHarvester, SpiderFoot
• BuiltWith, Wappalyzer"
