import socket
import time

# 配置发送端和接收端的IP和端口
sender_host = "192.168.1.5"
sender_port = 49280

receiver_host = "192.168.1.6"
receiver_port = 49280

def create_connection(host, port):
    """创建并返回一个连接到指定主机和端口的socket对象"""
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            print(f"成功连接到 {host}:{port}")
            return s
        except (socket.error, ConnectionRefusedError) as e:
            print(f"连接到 {host}:{port} 失败，错误: {e}，正在重试...")
            time.sleep(5)  # 等待5秒后重试

def main():
    """主程序逻辑"""
    while True:  # 无限循环以确保程序持续运行
        try:
            print("正在尝试连接到发送端和接收端...")
            sender_s = create_connection(sender_host, sender_port)
            receiver_s = create_connection(receiver_host, receiver_port)
            
            print("连接成功，开始数据传输...")
            
            while True:
                # 接收数据
                data = sender_s.recv(1500)
                if not data:
                    print("没有接收到数据，连接可能已关闭。")
                    break
                
                print("接收到的数据：", data.decode())
                
                # 处理数据
                cleaned_data = data.replace(b"NOTIFY ", b"")
                if cleaned_data:
                    cleaned_data += b"\n"
                    receiver_s.sendall(cleaned_data)
        
        except (socket.error, ConnectionResetError) as e:
            print(f"连接中断，错误: {e}，重新尝试连接...")
        
        except KeyboardInterrupt:
            print("程序被用户中断")
            break
        
        finally:
            # 确保在异常或退出时关闭socket
            try:
                sender_s.close()
            except:
                pass
            try:
                receiver_s.close()
            except:
                pass

            print("连接已关闭，等待重新连接...")

if __name__ == "__main__":
    main()