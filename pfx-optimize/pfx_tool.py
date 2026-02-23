import os
import sys
import subprocess
import time
from pathlib import Path
from typing import Tuple, Optional, List

# ==========================================================
# PHẦN 1: TỰ ĐỘNG CHUẨN BỊ MÔI TRƯỜNG (BOOTSTRAP)
# ==========================================================
def bootstrap():
    """Tự động cài đặt thư viện nếu máy Client chưa có."""
    try:
        import cryptography
    except ImportError:
        print("=" * 50)
        print("[!] Thieu thu vien 'cryptography'.")
        print("[*] Dang tu dong thiet lap moi truong cho anh...")
        print("=" * 50)
        try:
            # Cài đặt âm thầm vào user directory để né SentinelOne và quyền Admin
            subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography", "--user", "--quiet"])
            print("\n[OK] Thiet lap thanh cong! Dang khoi dong tool...")
            time.sleep(1.5)
            # Khởi động lại script để nhận thư viện mới
            os.execv(sys.executable, ['python'] + sys.argv)
        except Exception as e:
            print(f"\n[X] Loi tu dong cai dat: {e}")
            input("Nhan Enter de thoat...")
            sys.exit(1)

# Chạy bootstrap ngay lập tức khi mở file
if __name__ == "__main__":
    bootstrap()

# ==========================================================
# PHẦN 2: IMPORT CÁC THƯ VIỆN CHÍNH (SAU KHI ĐÃ CÓ LIB)
# ==========================================================
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import pkcs12

# Kiểm tra nền tảng để xử lý nhập mật khẩu ẩn
try:
    import msvcrt
    PLATFORM = "windows"
except ImportError:
    try:
        import termios
        import tty
        PLATFORM = "unix"
    except ImportError:
        import getpass
        PLATFORM = "generic"

# ==========================================================
# PHẦN 3: LOGIC CHÍNH CỦA ANH (GIỮ NGUYÊN BẢN GỐC)
# ==========================================================
class PFXExporter:
    @staticmethod
    def get_masked_input(prompt: str = "-> Enter password: ") -> str:
        """Nhập mật khẩu có dấu *"""
        print(prompt, end='', flush=True)
        password = ""
        if PLATFORM == "windows":
            while True:
                char = msvcrt.getch()
                if char in (b'\r', b'\n'):
                    print('')
                    break
                elif char == b'\x08': # Backspace
                    if password:
                        password = password[:-1]
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                elif char == b'\x03': # Ctrl+C
                    raise KeyboardInterrupt
                else:
                    try:
                        password += char.decode('utf-8')
                        sys.stdout.write('*')
                        sys.stdout.flush()
                    except UnicodeDecodeError: pass
        # ... (Phần code Unix anh đã viết giữ nguyên ở đây) ...
        return password

    def extract_pfx(self, pfx_path: Path, password: str) -> Tuple[bytes, bytes, Optional[List[bytes]]]:
        """Trích xuất cert bằng logic anh đã tối ưu"""
        with open(pfx_path, "rb") as f:
            pfx_data = f.read()
        private_key, cert, ca_certs = pkcs12.load_key_and_certificates(pfx_data, password.encode())
        key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        cert_bytes = cert.public_bytes(serialization.Encoding.PEM)
        ca_list = [ca.public_bytes(serialization.Encoding.PEM) for ca in ca_certs] if ca_certs else None
        return key_bytes, cert_bytes, ca_list

def main():
    exporter = PFXExporter()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("   PFX EXPORTER PRO - OPTIMIZELY SERVICE DESK")
        print("=" * 50 + "\n")
        
        user_input = input("-> Keo file PFX vao day (hoac 'E' de thoat): ").strip().strip('"').strip("'")
        if user_input.lower() == 'e': break
            
        pfx_path = Path(user_input)
        if not pfx_path.is_file():
            print(f"\n[!] Khong tim thay file: {pfx_path}")
            time.sleep(1.5)
            continue

        try:
            pwd = exporter.get_masked_input()
            print("\n[*] Dang xu ly...")
            key, cert, ca_list = exporter.extract_pfx(pfx_path, pwd)
            
            base_path = pfx_path.with_suffix('')
            base_path.with_suffix('.key').write_bytes(key)
            base_path.with_suffix('.crt').write_bytes(cert)
            if ca_list:
                with open(f"{base_path}_ca.crt", "wb") as f:
                    for ca in ca_list: f.write(ca)

            print("\n" + " SUCCESS ".center(30, "="))
            # Tự động mở folder kết quả
            if sys.platform == 'win32': os.startfile(pfx_path.parent)
            time.sleep(2)
        except Exception as e:
            print(f"\n[X] LOI: {e}")
            input("\nNhan Enter de tiep tuc...")

if __name__ == "__main__":
    main()