import requests
from bs4 import BeautifulSoup

# Yeni və aktiv ARB TV səhifəsinin URL-si
MAIN_URL = 'https://tv.kavuntv.net/arb-tv-1/'

def fetch_m3u8_link():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(MAIN_URL, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Sayfa açıla bilmədi: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    scripts = soup.find_all("script")

    for script in scripts:
        if script.string and ".m3u8" in script.string:
            lines = script.string.splitlines()
            for line in lines:
                if ".m3u8" in line:
                    start = line.find("https://")
                    end = line.find(".m3u8") + 5
                    link = line[start:end]
                    return link
    raise Exception("m3u8 link tapılmadı.")

def save_m3u_file(m3u8_url):
    content = f"#EXTM3U\n#EXTINF:-1,ARB TV\n{m3u8_url}"
    with open("arb_tv.m3u", "w") as f:
        f.write(content)
    print("arb_tv.m3u yaradıldı və IPTV üçün hazırdır.")

if __name__ == "__main__":
    try:
        m3u8_url = fetch_m3u8_link()
        print("Tapılan m3u8:", m3u8_url)
        save_m3u_file(m3u8_url)
    except Exception as e:
        print("Xəta:", e)