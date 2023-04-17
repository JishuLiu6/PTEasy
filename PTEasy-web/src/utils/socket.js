import {io} from "socket.io-client";

class SocketHandler {
  constructor(url) {
    this.socket = io(url);
  }

  onMessage(event, callback) {
    this.socket.on(event, (data) => {
      callback(data);
    });
  }
}

export default SocketHandler;
