gia_goc = [4.95, 9.95, 14.95, 19.95, 24.95]
giam = 0.6

print("| Giá gốc | Số tiền chiết khấu | Giá mới |")
print("|---------|--------------------|---------|")

i = 0
while i < len(gia_goc):
    giagoc = gia_goc[i]
    chietkhau = round( giagoc* giam, 2)
    gia_moi = round( giagoc - chietkhau, 2)
    print(f"| { giagoc} | {chietkhau} | {gia_moi} |")
    i += 1