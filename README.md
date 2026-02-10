# Công cụ Cắt Video MP4 (Video Trimmer)

Một script Python đơn giản để cắt video định dạng MP4 sử dụng thư viện `moviepy`.

## Tính năng
- Cắt video nhanh chóng chỉ bằng câu lệnh.
- Hỗ trợ nhiều định dạng thời gian: giây, phút:giây (mm:ss), và giờ:phút:giây (hh:mm:ss).
- Tên file đầu ra được đặt tự động theo định dạng: `outputYYYYMMDD_HHmiSS.mp4`.

## Yêu cầu hệ thống
- Python 3.x
- Thư viện `moviepy`

## Cài đặt thư viện
Nếu bạn chưa cài đặt `moviepy`, hãy chạy lệnh sau:
```bash
pip install moviepy
```

## Cách sử dụng
Mở terminal (PowerShell hoặc CMD) trong thư mục của dự án và chạy lệnh sau:

```bash
python trim_video.py <đường_dẫn_file> <điểm_bắt_đầu> <điểm_kết_thúc>
```

### Các định dạng thời gian được hỗ trợ
1. **Theo giây**: Ví dụ `15` hoặc `15.5`
2. **Phút:Giây (mm:ss)**: Ví dụ `01:30` (1 phút 30 giây)
3. **Giờ:Phút:Giây (hh:mm:ss)**: Ví dụ `00:01:30`

### Ví dụ
- **Cắt 5 giây đầu tiên:**
  ```bash
  python trim_video.py "input\video.mp4" 0 5
  ```
- **Cắt từ phút thứ 1 đến phút thứ 2:**
  ```bash
  python trim_video.py "input\video.mp4" 01:00 02:00
  ```
- **Cắt từ phút 01:30 đến 02:30:**
  ```bash
  python trim_video.py "input\video.mp4" 01:30 02:30
  ```

## Cấu trúc thư mục
- `trim_video.py`: Script chính để thực hiện cắt video.
- `input/`: Nơi chứa các file video đầu vào.
- `.agent.antigravity/`: Thư mục chứa các tài liệu thiết kế và kế hoạch (Markdown).
- `.gitignore`: Cấu hình để bỏ qua các file không cần thiết khi dùng Git.
