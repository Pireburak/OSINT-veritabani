# QLineSec
import whois
import dns.resolver
import requests
import socket
from colorama import Fore, Style, init

# Renklendirmeyi başlat
init(autoreset=True)

class OSINTHelper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_ip_address(self, domain):
        """Domain'in IP adresini çözer."""
        try:
            ip = socket.gethostbyname(domain)
            print(f"\n{Fore.CYAN}[*] IP Adresi Çözümlendi: {ip}{Style.RESET_ALL}")
            return ip
        except Exception as e:
            print(f"{Fore.RED}[!] IP çözümlenemedi: {e}")
            return None

    def get_whois_info(self, domain):
        """Domain kayıt bilgilerini (WHOIS) getirir."""
        print(f"\n{Fore.YELLOW}[!] {domain} için WHOIS sorgusu yapılıyor...{Style.RESET_ALL}")
        try:
            w = whois.whois(domain)
            print(f"{Fore.GREEN}[+] Kayıt Operatörü: {w.registrar}")
            print(f"{Fore.GREEN}[+] Oluşturulma Tarihi: {w.creation_date}")
            print(f"{Fore.GREEN}[+] Bitiş Tarihi: {w.expiration_date}")
            if w.emails:
                print(f"{Fore.GREEN}[+] İletişim E-postaları: {w.emails}")
        except Exception as e:
            print(f"{Fore.RED}[-] WHOIS bilgisi alınamadı: {e}")

    def get_dns_records(self, domain):
        """DNS kayıtlarını (A, MX, NS, TXT) tarar."""
        print(f"\n{Fore.YELLOW}[!] DNS Kayıtları Taranıyor...{Style.RESET_ALL}")
        record_types = ['A', 'MX', 'NS', 'TXT']
        
        for record in record_types:
            try:
                answers = dns.resolver.resolve(domain, record)
                for rdata in answers:
                    print(f"{Fore.BLUE}[+] {record} Kaydı: {rdata.to_text()}{Style.RESET_ALL}")
            except:
                pass # Kayıt yoksa hata vermeden geç

    def get_geolocation(self, ip):
        """IP adresinin coğrafi konumunu bulur (Ücretsiz API kullanarak)."""
        print(f"\n{Fore.YELLOW}[!] Coğrafi Konum Analizi Yapılıyor...{Style.RESET_ALL}")
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}").json()
            if response['status'] == 'success':
                print(f"{Fore.MAGENTA}[+] Ülke: {response['country']}")
                print(f"{Fore.MAGENTA}[+] Şehir: {response['city']}")
                print(f"{Fore.MAGENTA}[+] ISP: {response['isp']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] Konum bulunamadı.")
        except Exception as e:
            print(f"{Fore.RED}[-] API hatası: {e}")

    def scan_http_headers(self, domain):
        """Web sunucusunun HTTP başlıklarını analiz eder (Server, Teknolojiler vb.)."""
        print(f"\n{Fore.YELLOW}[!] HTTP Başlık Analizi (Web Recon) Başlatıldı...{Style.RESET_ALL}")
        target_url = f"http://{domain}"
        try:
            response = requests.get(target_url, headers=self.headers, timeout=5)
            headers = response.headers
            
            # Kritik başlıkları kontrol et
            keys_to_check = ['Server', 'X-Powered-By', 'X-AspNet-Version', 'Set-Cookie']
            
            for key in keys_to_check:
                if key in headers:
                    print(f"{Fore.GREEN}[+] {key}: {headers[key]}{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}[-] Web sunucusuna erişilemedi: {e}")

def main():
    print(f"{Fore.MAGENTA}=== OSINT-Helper-Project v1.0 ==={Style.RESET_ALL}")
    print(f"{Fore.WHITE}Uyarı: Bu araç sadece eğitim ve yasal analiz amaçlıdır.\n")
    
    scanner = OSINTHelper()
    
    # Kullanıcıdan hedef domain alınır
    target_domain = input(f"{Fore.CYAN}Hedef Domain (Örn: google.com): {Style.RESET_ALL}").strip()
    
    # "http://" veya "https://" varsa temizle
    target_domain = target_domain.replace("https://", "").replace("http://", "").split('/')[0]

    if target_domain:
        # 1. IP Çözümleme
        target_ip = scanner.get_ip_address(target_domain)
        
        # 2. WHOIS Sorgusu
        scanner.get_whois_info(target_domain)
        
        # 3. DNS Enum
        scanner.get_dns_records(target_domain)
        
        # 4. GeoIP (Eğer IP çözüldüyse)
        if target_ip:
            scanner.get_geolocation(target_ip)
            
        # 5. HTTP Header Analizi
        choice = input(f"\n{Fore.BLUE}Web Sunucu Analizi (HTTP Headers) yapılsın mı? (E/H): {Style.RESET_ALL}")
        if choice.lower() == 'e':
            scanner.scan_http_headers(target_domain)
    else:
        print("Geçersiz domain girişi.")

if __name__ == "__main__":
    main()
