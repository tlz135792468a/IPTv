from datetime import datetime

def generate():
    now = datetime.now()
    ts = now.strftime("%Y%m%d%H%M%S")

    common_args = f"msisdn=c2b835cf-3fe5-46ef-a43a-fd53e36d3df2&mdspid=&spid=699004&netType=0&sid=2200179315&pid=2028597139&timestamp={ts}&SecurityKey={ts}&promotionId=&mvid=2200179315&mcid=500020&playurlVersion=WX-A1-9.3.2-RELEASE&userid=&jmhm=&videocodec=h264&appCode=miguvideo_h5&bean=mgsph5&tid=h5&conFee=0&encrypt=97ce09d192e9a04485fbcf481de8c72b&sv=10012"

    channels = [
        # 央视全台
        ("CCTV-1 综合 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv1hd/50/index.m3u8?{common_args}"),
        ("CCTV-2 财经 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv2hd/50/index.m3u8?{common_args}"),
        ("CCTV-3 综艺 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv3hd/50/index.m3u8?{common_args}"),
        ("CCTV-4 中文国际 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv4hd/50/index.m3u8?{common_args}"),
        ("CCTV-4 欧视 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv4ouhd/50/index.m3u8?{common_args}"),
        ("CCTV-5 体育 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv5hd/50/index.m3u8?{common_args}"),
        ("CCTV-5+ 体育赛事 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv5phd/50/index.m3u8?{common_args}"),
        ("CCTV-6 电影 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv6hd/50/index.m3u8?{common_args}"),
        ("CCTV-7 国防军事 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv7hd/50/index.m3u8?{common_args}"),
        ("CCTV-8 电视剧 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv8hd/50/index.m3u8?{common_args}"),
        ("CCTV-9 纪录 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv9hd/50/index.m3u8?{common_args}"),
        ("CCTV-10 科教 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv10hd/50/index.m3u8?{common_args}"),
        ("CCTV-11 戏曲 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv11hd/50/index.m3u8?{common_args}"),
        ("CCTV-12 社会与法 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv12hd/50/index.m3u8?{common_args}"),
        ("CCTV-13 新闻 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv13hd/50/index.m3u8?{common_args}"),
        ("CCTV-14 少儿 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv14hd/50/index.m3u8?{common_args}"),
        ("CCTV-15 音乐 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv15hd/50/index.m3u8?{common_args}"),
        ("CCTV-16 奥林匹克 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv16hd/50/index.m3u8?{common_args}"),
        ("CCTV-17 农业农村 HD", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv17hd/50/index.m3u8?{common_args}"),
        # 央视4K
        ("CCTV-4K 超高清", f"https://hlsztemgsplive.miguvideo.com:443/migu/kailu/20200324/cctv4k/50/index.m3u8?{common_args}"),
        # 卫视全覆盖
        ("湖南卫视 HD", "https://hlsbkmgsplive.miguvideo.com/migu/kailu/hunanhd/50/index.m3u8?&HlsSubType=&encrypt="),
        ("浙江卫视 HD", "https://hlsbkmgsplive.miguvideo.com/migu/kailu/zhejianghd/50/index.m3u8?&HlsSubType=&encrypt="),
        ("江苏卫视 HD", "https://hlsbkmgsplive.miguvideo.com/migu/kailu/jiangsu/50/index.m3u8?&HlsSubType=&encrypt="),
        ("东方卫视 HD", "https://hlsbkmgsplive.miguvideo.com/migu/kailu/dongfang/50/index.m3u8?&HlsSubType=&encrypt="),
        ("北京卫视 HD", "https://hlsbkmgsplive.miguvideo.com/migu/kailu/beijing/50/index.m3u8?&HlsSubType=&encrypt="),
        ("广东卫视 HD", "https://hlsbkmgsplive.miguvideo.com/migu/kailu/gdwshd265/55/20200407/01.m3u8?&HlsSubType=&encrypt="),
    ]

    m3u_content = "#EXTM3U\n"
    txt_content = ""
    for name, url in channels:
        m3u_content += f"#EXTINF:-1,{name}\n{url}\n"
        txt_content += f"{name},{url}\n"

    with open("live.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    with open("live.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

if __name__ == "__main__":
    generate()
