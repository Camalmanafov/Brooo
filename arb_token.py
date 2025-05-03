# Bu skript .m3u faylı yaradır və daxilinə linki yazır

link = "https://proxy.canlitvplayer.com/str.yodacdn.net/arb/mono.m3u8?token=4e0daaaac4d7a14bbfd8d7a566369b111ab7d9d1-7120880603ae6eaa8a55cd0dc83d67b2-1746280210000000-1746269410000"

m3u_content = f"#EXTM3U\n#EXTINF:-1,ARB TV\n{link}"

with open("arb_token.m3u", "w") as f:
    f.write(m3u_content)

print("arb_token.m3u faylı yaradıldı.")