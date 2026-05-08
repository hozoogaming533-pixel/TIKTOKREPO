# HOZOO MD - TIKTOK 24/7 ULTIMATE BOT
# ROOT ACCESS MODE - FULL ONLINE 24 JAM

import requests
import re
import time
import random
import json
import uuid
import sys
import os
from datetime import datetime
from threading import Thread, Event

class TikTokUltimateBot:
    def __init__(self):
        self.session = requests.Session()
        self.setup_headers()
        self.logged_in = False
        self.phone_number = None
        self.session_id = None
        self.csrf_token = None
        self.report_threads = {}
        
    def setup_headers(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'id-ID,id;q=0.9,en;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.tiktok.com',
            'Referer': 'https://www.tiktok.com/',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }
        self.session.headers.update(self.headers)
    
    def generate_device_id(self):
        return ''.join(random.choices('0123456789abcdef', k=32))
    
    def generate_trace_id(self):
        return str(uuid.uuid4())
    
    def get_csrf_token(self):
        try:
            response = self.session.get("https://www.tiktok.com/")
            match = re.search(r'name="csrf-token" content="([^"]+)"', response.text)
            if match:
                self.csrf_token = match.group(1)
                return self.csrf_token
        except:
            pass
        for cookie in self.session.cookies:
            if cookie.name == 'csrf_token':
                self.csrf_token = cookie.value
                return self.csrf_token
        return None
    
    def login_with_otp(self, phone_number):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n" + "="*70)
        print("  🔐 HOZOO MD - TIKTOK LOGIN SYSTEM 🔐")
        print("="*70)
        print(f"\n  📞 TARGET NUMBER : {phone_number}")
        print("  🌐 STATUS       : CONNECTING...")
        print("="*70)
        
        send_url = "https://www.tiktok.com/passport/web/account/send_code/"
        payload = {
            'mobile': phone_number,
            'type': '3',
            'account_sdk_source': 'web',
            'region': 'ID',
            'aid': '1988',
            'app_name': 'tiktok_web',
            'device_id': self.generate_device_id()
        }
        
        try:
            print("\n  [*] 📤 SENDING OTP REQUEST...")
            response = self.session.post(send_url, data=payload)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 0:
                    print("  [✓] ✅ OTP CODE SENT SUCCESSFULLY!")
                    print("  [!] 📱 CHECK SMS ON YOUR PHONE:", phone_number)
                    print("\n" + "="*70)
                    otp_code = input("  [?] ENTER OTP CODE : ").strip()
                    return self.verify_otp(phone_number, otp_code)
                else:
                    print(f"  [×] ❌ FAILED: {result.get('msg', 'Unknown error')}")
                    return False
            else:
                print(f"  [×] ❌ HTTP ERROR: {response.status_code}")
                return False
        except Exception as e:
            print(f"  [×] ❌ ERROR: {e}")
            return False
    
    def verify_otp(self, phone_number, otp_code):
        verify_url = "https://www.tiktok.com/passport/web/account/login_code/"
        payload = {
            'mobile': phone_number,
            'code': otp_code,
            'type': '3',
            'aid': '1988',
            'app_name': 'tiktok_web'
        }
        
        try:
            print("\n  [*] 🔐 VERIFYING OTP...")
            response = self.session.post(verify_url, data=payload)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 0:
                    print("  [✓] ✅ LOGIN SUCCESSFUL!")
                    self.logged_in = True
                    self.phone_number = phone_number
                    self.session_id = self.session.cookies.get('sessionid', '')
                    self.get_csrf_token()
                    
                    print("\n" + "="*70)
                    print("  🎉 WELCOME TO HOZOO MD TIKTOK BOT 🎉")
                    print("="*70)
                    time.sleep(2)
                    return True
                else:
                    print(f"  [×] ❌ WRONG OTP: {result.get('msg', 'Invalid code')}")
                    return False
            else:
                print(f"  [×] ❌ HTTP ERROR: {response.status_code}")
                return False
        except Exception as e:
            print(f"  [×] ❌ ERROR: {e}")
            return False
    
    def report_with_payload(self, username, reason="spam"):
        if not self.logged_in:
            return False, "Not logged in"
        
        print(f"\n  [!] 🎯 TARGET: @{username}")
        print("  [*] ⏳ LOADING PAYLOAD...")
        time.sleep(0.5)
        
        trace_id = self.generate_trace_id()
        report_id = str(uuid.uuid4())
        timestamp = int(time.time() * 1000)
        
        report_url = "https://www.tiktok.com/api/report/v2/"
        
        payload_data = {
            'object_id': username,
            'object_type': 'user',
            'report_type': reason,
            'report_reason': 'Harassment and cyberbullying',
            'source': 'profile_page',
            'aid': '1988',
            'device_id': self.generate_device_id(),
            'report_id': report_id,
            'timestamp': timestamp,
            'trace_id': trace_id
        }
        
        headers_report = {
            'x-tt-trace-id': trace_id,
            'x-secsdk-csrf-token': self.csrf_token or self.get_csrf_token(),
            'Referer': f'https://www.tiktok.com/@{username}',
            'x-requested-with': 'XMLHttpRequest'
        }
        
        print("  [*] 📡 SENDING REPORT...")
        
        try:
            response = self.session.post(report_url, json=payload_data, headers=headers_report)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 0 or result.get('status_code') == 0:
                    print(f"  [✓] ✅ REPORT SUCCESS! @{username}")
                    return True, result
                else:
                    print(f"  [×] ❌ REPORT FAILED: {result.get('msg', 'Unknown')}")
                    return False, result
            else:
                print(f"  [×] ❌ HTTP {response.status_code}")
                return False, None
        except Exception as e:
            print(f"  [×] ❌ ERROR: {e}")
            return False, None
    
    def start_24h_report(self, username):
        if username in self.report_threads and self.report_threads[username]['running']:
            print(f"  [!] ⚠️ REPORT FOR @{username} ALREADY RUNNING!")
            return
        
        stop_event = Event()
        
        def report_loop():
            count = 0
            start_time = datetime.now()
            print(f"\n  [✓] 🚀 STARTING 24H REPORT FOR @{username}")
            print(f"  [*] ⏰ START TIME: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
            
            while not stop_event.is_set():
                count += 1
                print(f"\n  {'='*66}")
                print(f"  [📊] REPORT #{count} | TARGET: @{username}")
                print(f"  [🕐] TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"  {'='*66}")
                
                success, _ = self.report_with_payload(username, "spam")
                
                if success:
                    print(f"  [✓] ✅ REPORT #{count} SUCCESS")
                else:
                    print(f"  [×] ❌ REPORT #{count} FAILED")
                
                delay = random.randint(180, 300)
                print(f"  [*] ⏳ WAITING {delay} SECONDS...")
                
                for i in range(delay):
                    if stop_event.is_set():
                        break
                    time.sleep(1)
            
            print(f"\n  [!] 🛑 BOT STOPPED FOR @{username}")
            print(f"  [📊] TOTAL REPORTS: {count}")
        
        thread = Thread(target=report_loop)
        thread.daemon = True
        thread.start()
        
        self.report_threads[username] = {
            'thread': thread,
            'running': True,
            'stop_event': stop_event,
            'start_time': datetime.now()
        }
    
    def stop_24h_report(self, username):
        if username in self.report_threads:
            self.report_threads[username]['stop_event'].set()
            self.report_threads[username]['running'] = False
            print(f"  [✓] 🛑 REPORT STOPPED FOR @{username}")
            return True
        print(f"  [×] ❌ NO ACTIVE REPORT FOR @{username}")
        return False
    
    def unban_account(self, username):
        print(f"\n  {'='*66}")
        print(f"  [🔄] UNBAN/APPEAL FOR: @{username}")
        print(f"  {'='*66}")
        
        unban_url = "https://www.tiktok.com/api/v1/appeal/submit/"
        
        appeal_id = str(uuid.uuid4())
        payload = {
            'username': username,
            'appeal_type': 'account_unban',
            'reason': 'False banned, please review',
            'appeal_id': appeal_id,
            'timestamp': int(time.time() * 1000)
        }
        
        headers_appeal = {
            'x-tt-trace-id': self.generate_trace_id(),
            'x-secsdk-csrf-token': self.csrf_token or self.get_csrf_token(),
            'Content-Type': 'application/json'
        }
        
        print("  [*] 📡 SENDING APPEAL REQUEST...")
        
        try:
            response = self.session.post(unban_url, json=payload, headers=headers_appeal)
            
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 0:
                    print(f"  [✓] ✅ UNBAN/APPEAL SUCCESS FOR @{username}")
                    return True, result
                else:
                    print(f"  [×] ❌ APPEAL FAILED: {result.get('msg', 'Unknown')}")
                    return False, result
            else:
                print(f"  [×] ❌ HTTP {response.status_code}")
                return False, None
        except Exception as e:
            print(f"  [×] ❌ ERROR: {e}")
            return False, None
    
    def show_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""\033[1;32m
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║     ██╗  ██╗ ██████╗ ███████╗ ██████╗  ██████╗     ███╗   ███╗██████╗             ║
║     ██║  ██║██╔═══██╗██╔════╝██╔═══██╗██╔═══██╗    ████╗ ████║██╔══██╗            ║
║     ███████║██║   ██║█████╗  ██║   ██║██║   ██║    ██╔████╔██║██║  ██║            ║
║     ██╔══██║██║   ██║██╔══╝  ██║   ██║██║   ██║    ██║╚██╔╝██║██║  ██║            ║
║     ██║  ██║╚██████╔╝███████╗╚██████╔╝╚██████╔╝    ██║ ╚═╝ ██║██████╔╝            ║
║     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝     ╚═╝     ╚═╝╚═════╝             ║
║                                                                                   ║
║                     🤖 TIKTOK 24/7 ULTIMATE REPORT BOT 🤖                         ║
║                              🔥 FULL ONLINE 24 JAM 🔥                             ║
║                                                                                   ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                   ║
║  📋 COMMAND LIST:                                                                 ║
║                                                                                   ║
║     ╔═════════════════════════════════════════════════════════════════════════╗  ║
║     ║  /start        ▶  DISPLAY THIS MENU                                    ║  ║
║     ║  /report       📢  REPORT TARGET ACCOUNT (24/7 AUTO)                   ║  ║
║     ║  /unban        🔓  UNBAN/APPEAL BANNED ACCOUNT                        ║  ║
║     ║  /stop         🛑  STOP 24H REPORT FOR ACCOUNT                        ║  ║
║     ║  /status       📊  CHECK BOT STATUS & ACTIVE REPORTS                  ║  ║
║     ║  /help         ❓  SHOW THIS MENU                                     ║  ║
║     ╚═════════════════════════════════════════════════════════════════════════╝  ║
║                                                                                   ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                   ║
║  📌 EXAMPLES:                                                                     ║
║                                                                                   ║
║     /report @johndoe                                                              ║
║     /unban @janedoe                                                               ║
║     /stop @johndoe                                                                ║
║                                                                                   ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                   ║
║  ⚡ STATUS: \033[1;32m✅ ONLINE 24/7\033[1;32m                                                          ║
║  📞 PHONE: \033[1;33m{self.phone_number if self.phone_number else 'NOT LOGGED IN'}\033[1;32m                      ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
\033[0m""")
    
    def run_cli(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("""\033[1;36m
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║     ██████╗  ██████╗  ██████╗ ████████╗                         ║
║     ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝                         ║
║     ██████╔╝██║   ██║██║   ██║   ██║                            ║
║     ██╔══██╗██║   ██║██║   ██║   ██║                            ║
║     ██║  ██║╚██████╔╝╚██████╔╝   ██║                            ║
║     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝                            ║
║                                                                   ║
║              HOZOO MD - TIKTOK ULTIMATE BOT                      ║
║                   VERSION: 3.0 | ROOT EDITION                    ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
\033[0m""")
        
        print("\n\033[1;33m[!] 🔐 PLEASE LOGIN FIRST!\033[0m")
        phone = input("\n\033[1;36m📞 ENTER PHONE NUMBER (+62xxxx): \033[0m").strip()
        
        if self.login_with_otp(phone):
            print("\n\033[1;32m[✓] ✅ LOGIN SUCCESS! BOT READY 24/7!\033[0m")
            time.sleep(1.5)
        else:
            print("\n\033[1;31m[×] ❌ LOGIN FAILED! RESTART AND TRY AGAIN!\033[0m")
            return
        
        while True:
            try:
                cmd = input(f"\n\033[1;35m[ROOT@DGXEONHOZOOMD]~> \033[0m").strip().lower()
                
                if not cmd:
                    continue
                
                if cmd == '/start' or cmd == '/help':
                    self.show_menu()
                
                elif cmd.startswith('/report'):
                    parts = cmd.split(' ', 1)
                    if len(parts) > 1:
                        username = parts[1].replace('@', '')
                        print(f"\n  [?] 🎯 REPORT @{username} 24/7?")
                        print("     1. YES - Run 24 hour report")
                        print("     2. NO - Report once only")
                        choice = input("\n  Choose (1/2): ").strip()
                        if choice == "1":
                            self.start_24h_report(username)
                        else:
                            self.report_with_payload(username, "spam")
                    else:
                        print("  [×] USE: /report @username")
                
                elif cmd.startswith('/unban'):
                    parts = cmd.split(' ', 1)
                    if len(parts) > 1:
                        username = parts[1].replace('@', '')
                        self.unban_account(username)
                    else:
                        print("  [×] USE: /unban @username")
                
                elif cmd.startswith('/stop'):
                    parts = cmd.split(' ', 1)
                    if len(parts) > 1:
                        username = parts[1].replace('@', '')
                        self.stop_24h_report(username)
                    else:
                        print("  [×] USE: /stop @username")
                
                elif cmd == '/status':
                    print("\n  " + "="*60)
                    print("  📊 BOT STATUS")
                    print("  " + "="*60)
                    print(f"  🔐 LOGIN: {'✅ YES' if self.logged_in else '❌ NO'}")
                    print(f"  📞 PHONE: {self.phone_number if self.phone_number else '-'}")
                    print(f"\n  📢 ACTIVE REPORTS:")
                    if self.report_threads:
                        for username, data in self.report_threads.items():
                            if data['running']:
                                elapsed = datetime.now() - data['start_time']
                                hours = elapsed.total_seconds() / 3600
                                print(f"     ▶ @{username} - {hours:.1f} HOURS")
                    else:
                        print("     ❌ NO ACTIVE REPORTS")
                    print("  " + "="*60)
                
                elif cmd == '/exit' or cmd == '/quit':
                    print("\n  [!] 🛑 SHUTTING DOWN BOT...")
                    for username in list(self.report_threads.keys()):
                        self.stop_24h_report(username)
                    print("  [✓] GOODBYE!")
                    break
                
                else:
                    print("  [×] UNKNOWN COMMAND. TYPE /start FOR MENU")
                
            except KeyboardInterrupt:
                print("\n  [!] 🛑 BOT STOPPED...")
                for username in list(self.report_threads.keys()):
                    self.stop_24h_report(username)
                break
            except Exception as e:
                print(f"  [×] ERROR: {e}")

if __name__ == "__main__":
    bot = TikTokUltimateBot()
    bot.run_cli()
