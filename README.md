# jshp-branding

Bộ addon Odoo 19.0 mang nhận diện thương hiệu JSHP vào giao diện Odoo: tên, logo,
biểu tượng, màu sắc và những chỗ Odoo đang hiện thương hiệu của chính nó.

Repo này chỉ lo phần *nhận diện*. Nghiệp vụ (in tem, đồng bộ DB2, …) nằm ở
[`seapro-odoo`](../seapro-odoo); module ở đây không phụ thuộc module nghiệp vụ
nào, và module nghiệp vụ cũng không phụ thuộc ngược lại.

## Danh sách module

| Module | Mô tả |
| --- | --- |
| _(chưa có)_ | |

Thêm module mới thì thêm một dòng vào bảng này.

## Cài đặt

Thêm thư mục repo vào `addons_path`, đặt **sau** `odoo/addons` để module ở đây
kế thừa được module chuẩn:

```ini
[options]
addons_path = /home/trung-tuan/odoo/19.0/odoo/addons,
              /home/trung-tuan/odoo/19.0/jshp-branding,
              /home/trung-tuan/odoo/19.0/seapro-odoo
```

Rồi cài module như mọi addon khác:

```bash
cd /home/trung-tuan/odoo/19.0/odoo
./odoo-bin -c <file_cau_hinh> -d <database> -i <ten_module> --stop-after-init
```

Ảnh, logo và chuỗi đưa vào bằng file XML có `noupdate="1"` sẽ **không** được làm
mới khi chạy `-u`. Muốn áp lại thì sửa trực tiếp trong database hoặc cài lại trên
database mới.

## Chạy test

Chạy trên một database dùng riêng cho test, không dùng database đang làm việc:

```bash
cd /home/trung-tuan/odoo/19.0/odoo
./odoo-bin -c <file_cau_hinh> -d <db_test> -i <ten_module> \
  --test-enable --test-tags=/<ten_module> \
  --stop-after-init --max-cron-threads=0 --http-port=8199
```

Lệnh trả exit code 0 cả khi module không cài được, nên phải đọc log để chắc test
đã thật sự chạy.

## Quy ước

**Manifest.** Mỗi file Python mở đầu bằng dòng bản quyền chung của dự án:

```python
# Part of jshp-odoo. See LICENSE file for full copyright and licensing details.
```

`__manifest__.py` khai báo `"license": "LGPL-3"`, `"author": "NTT"`,
`"website": "https://jshp.com.vn"`, và `version` theo dạng `x.y.z`.

**Ngôn ngữ.**

- `README.md`, tài liệu trong `docs/` và changelog viết bằng tiếng Việt.
- Comment và docstring trong mã nguồn viết bằng tiếng Anh.
- Chuỗi hiển thị trên giao diện viết bằng tiếng Anh, bản dịch tiếng Việt đặt
  trong `i18n/vi_VN.po`.
- Tên model, field, method, đường dẫn và thuật ngữ kỹ thuật giữ nguyên, không dịch.

**Commit.** Dòng đầu theo dạng `[TAG] module: mô tả ngắn`, trong đó `TAG` là một
trong `ADD`, `IMP`, `FIX`, `REF`, `MOV`, `REM`, `I18N`. Ví dụ:

```
[ADD] <ten_module>: logo và tên công ty trên trang đăng nhập
```

## Giấy phép

LGPL-3.
