# JSHP Bot Branding

Addon Odoo 19 đổi tên bot hệ thống thành **JSHPBot**, phụ thuộc `mail_bot`.

## Phạm vi

- Đổi tên contact `base.partner_root`; tài khoản `base.user_root`, tác giả
  trong chatter, Discuss và danh sách gợi ý @mention dùng cùng contact này.
- Đổi `@OdooBot` trong câu trả lời onboarding mới thành `@JSHPBot` sau khi
  dịch, giữ nguyên HTML và cơ chế onboarding chuẩn.
- Đổi nhãn trạng thái thành `JSHPBot Status`, có bản dịch tiếng Việt.
- Áp lại tên khi nâng cấp addon, kể cả khi contact gốc có `noupdate`.
- Khi gỡ addon, trả tên về `OdooBot` nếu tên hiện tại vẫn là `JSHPBot`.
  Tên tùy chỉnh có trước lúc cài sẽ không được lưu lại.

- Trang đăng nhập dùng logo công ty theo cơ chế chuẩn Odoo (`/web/binary/company_logo`).
  Đổi logo trong cấu hình công ty sẽ cập nhật các vị trí dùng logo công ty,
  bao gồm báo cáo/hóa đơn theo cấu hình chuẩn.
- Favicon và ảnh JSHPBot dùng file logo mặc định trong module, độc lập với
  logo công ty.
- Lưu ảnh bot cũ khi cài/nâng cấp lần đầu; gỡ addon sẽ khôi phục ảnh đó
  nếu ảnh bot vẫn là ảnh addon đã áp dụng.

Không sửa mã nguồn Odoo, ID, login hoặc quyền truy cập.
Không thay nội dung tin nhắn đã lưu, tên addon chuẩn trong Apps, nội dung
mẹo email của `digest`, hoặc chữ Odoo khác. Tên tác giả của tin nhắn cũ
vẫn đổi theo contact hệ thống.

## Cài đặt / nâng cấp

Thêm thư mục `jshp-branding` vào `addons_path` trong cấu hình, khởi động lại
Odoo và cập nhật danh sách Apps. Bỏ bộ lọc Apps rồi tìm **JSHP Bot Branding**.
Hoặc dùng Python environment đang chạy Odoo:

```bash
python odoo-bin -c <config> -d <database> -i jshp_bot_branding --stop-after-init
# Nâng cấp:
python odoo-bin -c <config> -d <database> -u jshp_bot_branding --stop-after-init
```

Tải lại trình duyệt sau khi cài. Module không tự cài vào database đang chạy.

## Kiểm thử

Chỉ chạy trên database test:

```bash
python odoo-bin -c <config> -d <db_test> -i jshp_bot_branding \
  --test-enable --test-tags=/jshp_bot_branding --stop-after-init \
  --max-cron-threads=0 --http-port=18549
```

Kiểm tra log có `0 failed, 0 error(s) of 5 tests`.

## Changelog

### 1.1.1

- Bỏ logo cố định trên trang đăng nhập; dùng lại logo công ty của Odoo.
- Favicon và ảnh JSHPBot tiếp tục dùng logo mặc định của module.
- Trước đăng nhập, Odoo chọn logo theo database/công ty mặc định; chưa có
  ngữ cảnh công ty đang chọn của người dùng.

### 1.1.0

- Thêm logo JSHP trên trang đăng nhập, favicon và ảnh bot.
- Giữ file PNG gốc 180×180 nền trong suốt.
- Kế thừa `web.login_layout` và `web.layout`; không đổi logo công ty trên
  hóa đơn/báo cáo, logo website riêng hoặc trang quản lý database.
- Khi nâng cấp, tên và ảnh bot được áp lại. Sau khi cập nhật, khởi động lại
  Odoo và tải lại trình duyệt; favicon có thể cần xóa cache.

### 1.0.0

- Đổi tên bot, nhãn trạng thái và hướng dẫn @mention sang JSHPBot.
