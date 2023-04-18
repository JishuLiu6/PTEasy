import io from "socket.io-client";

class SocketHandler {
  constructor(url) {
    this.socket = io(url);
  }
   // 添加静态方法用于返回单例
   static getInstance(url) {
    if (!this.instance) {
      this.instance = new SocketHandler(url);
    }
    return this.instance;
  }
}

export default SocketHandler;
