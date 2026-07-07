# Trafik Levhaları Algılama Sistemi (Detect Traffic Signs)

Bu proje, bilgisayar görüsü (Computer Vision) teknikleri kullanılarak trafikteki belirli uyarı ve düzenleme levhalarını gerçek zamanlı veya görsel üzerinden algılamak amacıyla geliştirilmiştir. Proje kapsamında nesne tespiti için eğitilmiş Haar Cascade (XML) modelleri ve bir Python betiği yer almaktadır.

## 🚀 Proje İçeriği

Proje klasöründe yer alan temel dosyalar ve işlevleri şu şekildedir:

*   **`levhaları algılama.py`**: OpenCV kütüphanesini kullanarak kamera görüntüsünü veya videoları işleyen, ilgili levhaları tespit edip ekranda kutu içine alan ana Python kodudur.
*   **`arac_sollamak_yasak_levhasi.xml`**: Geçme yasağı olan bölgeleri belirten levhayı algılamak için eğitilmiş cascade modeli.
*   **`demir_yolu_levhasi.xml`**: Demiryolu geçitlerini (hemzemin geçit) tespit etmek için eğitilmiş cascade modeli.
*   **`park_levhasi.xml`**: Park alanlarını ve otopark işaretlerini algılamak için eğitilmiş cascade modeli.
*   **`yaya_gecidi_levhasi.xml`**: Yaya geçitlerini tespit ederek otonom sürüş sistemlerine bilgi sağlamak amacıyla eğitilmiş cascade modeli.

## 🛠️ Kurulum ve Gereksinimler

Projeyi yerel bilgisayarınızda çalıştırmak için öncelikle gerekli kütüphanelerin yüklü olduğundan emin olun. 

1. **Depoyu bilgisayarınıza indirin:**
   ```bash
   git clone [https://github.com/schop3r/Detect-traffic-signs-.git](https://github.com/schop3r/Detect-traffic-signs-.git)
   cd Detect-traffic-signs-
