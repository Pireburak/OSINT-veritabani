# Prompts for gemini-pro
Siber güvenlik denildiğinde akla genellikle karmaşık kodlar, firewall cihazları veya zararlı yazılımlar gelir. Ancak profesyonel bir sızma testinin (Penetration Test) veya gerçek bir siber saldırının en önemli aşaması, klavyeye dokunulmadan önceki aşamadır: Keşif (Reconnaissance).

Açık Kaynak İstihbaratı (Open Source Intelligence - OSINT), herhangi bir gizlilik ihlali yapmadan, halka açık kaynaklardan (arama motorları, sosyal medya, kayıt veritabanları vb.) yasal yollarla veri toplama ve bu verileri analiz etme sürecidir. CIA, FBI gibi devlet kurumlarından özel sektördeki siber güvenlik firmalarına kadar geniş bir yelpazede kullanılan OSINT, "hedefi tanıma" sanatıdır.
Siber saldırı zincirini tanımlayan Cyber Kill Chain modelinin ilk halkası "Keşif"tir. Bir saldırgan veya güvenlik uzmanı, hedef sistem hakkında ne kadar çok bilgiye sahipse, başarı şansı o kadar artar.

Saldırgan Açısından: Hedef şirketin hangi antivirüs programını kullandığını, çalışanların e-posta formatını (örn: ad.soyad@sirket.com) veya sunucuların işletim sistemi sürümlerini bilmek, saldırı vektörünü belirler.

Savunmacı (Blue Team) Açısından: Kurumun internete sızmış verilerini (örneğin dark web’e düşmüş şifreleri) saldırganlardan önce tespit etmek, riski minimize etmeyi sağlar.
OSINT rastgele bir "Google araması" değildir; metodolojik bir süreçtir. Bu süreç genellikle beş aşamadan oluşur:

Planlama (Planning): Hedef kim? Hangi bilgiye ihtiyacımız var? (Örn: X şirketinin VPN IP adresleri).

Toplama (Collection): Verilerin ham kaynaklardan çekilmesi.

İşleme (Processing): Toplanan verinin düzenlenmesi ve gürültüden arındırılması.

Analiz (Analysis): Veriler arasındaki bağlantıların kurulması. (Örn: Bir çalışanın LinkedIn profili ile sızdırılan bir veritabanındaki verinin eşleştirilmesi).

Raporlama (Dissemination): Bulguların eyleme dönüştürülebilir bir rapora aktarılması.
OSINT uzmanları, manuel aramaların ötesinde gelişmiş teknikler kullanırlar.



Standart kullanıcılar internetin sadece yüzeyini görür. OSINT uzmanları ise Google Dorks adı verilen gelişmiş operatörleri kullanır.

Örnek: site:hedefsite.com filetype:pdf "gizli" komutu, hedef sitedeki, içinde "gizli" kelimesi geçen PDF dosyalarını listeler.


Bir alan adının (Domain) geçmişi, hangi sunucularda barındığı ve hangi alt alan adlarına (Subdomain) sahip olduğu haritalanır.

Araçlar: VirusTotal, Whois, TheHarvester.



Web sitelerini tarayan Google'ın aksine, Shodan internete bağlı cihazları (Webcam'ler, SCADA sistemleri, sunucular) tarar. Bir kurumun güvenlik duvarının arkasında unuttuğu açık bir port, Shodan üzerinden tespit edilebilir.



İnsan faktörü, güvenliğin en zayıf halkasıdır. Çalışanların sosyal medyada paylaştığı ofis fotoğrafları (ekranda görünen kodlar, masadaki post-it notları) veya kimlik kartları, saldırganlar için altın değerindedir.



OSINT yaparken en önemli ayrım, eylemin niteliğidir:

Pasif Keşif (Yasal): Hedef sistemle doğrudan etkileşime girmeden bilgi toplamaktır. (Örn: Google'da arama yapmak, LinkedIn profiline bakmak). Bu genellikle yasaldır çünkü bilgi zaten halka açıktır.

Aktif Keşif (Riskli/Yasadışı): Hedef sisteme paket göndermek, port taraması yapmak (Nmap) veya giriş denemesi yapmak. Bu işlemler, izinsiz yapıldığında siber suç kapsamına girer.

Bir siber güvenlik uzmanı adayı, asla izin almadığı bir sisteme "Aktif" tarama yapmamalıdır. OSINT, "iz bırakmadan" bilgi toplama sanatıdır.



Dijital dünyada hiçbir veri kaybolmaz. OSINT, bu devasa veri okyanusunda anlamlı bilgi parçalarını birleştirme yeteneğidir. İster bir şirketin güvenliğini sağlamak isteyen bir analist, ister bir sızma testi uzmanı olun; teknik becerileriniz kadar araştırmacı yönünüz de güçlü olmalıdır. Unutulmamalıdır ki; en sofistike "hack" yöntemleri değil, en iyi toplanmış "istihbarat" savaşı kazandırır.
