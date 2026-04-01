from decrypt import decrypt_num_list, your_data

def generate():
    data = decrypt_num_list(your_data, 20000)
    
    m3u = "#EXTM3U\n"
    m3u += "#EXTINF:-1,解密内容\n"
    m3u += data
    
    with open("live.m3u", "w", encoding="utf-8") as f:
        f.write(m3u)

if __name__ == "__main__":
    generate()
