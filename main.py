import speedtest

st = speedtest.Speedtest()
download = st.download() / 1_000_000
upload = st.upload() / 1_000_000

print(f"⬇️  Download: {download:.2f} Мбит/с")
print(f" ⬆️  Upload: {upload:.2f} Мбит/с")