package org.changyy.android;

import java.io.DataOutputStream;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;

public class SocketExample {
	public static boolean connectToTheServerAndSendAMessage(String server_ip, int server_port, int timeout, String message) {
		try {
			SocketAddress mSocketAddress = new InetSocketAddress(InetAddress.getByName(server_ip), server_port);
			Socket mSocket = new Socket();
			mSocket.connect(mSocketAddress, timeout); // timeout = 2000 (2s)
			
			DataOutputStream mDataOutputStream = new DataOutputStream(mSocket.getOutputStream());
			mDataOutputStream.write(message.getBytes());
			//mDataOutputStream.writeUTF(message);
			mDataOutputStream.close();
			
			mSocket.close();

			return true;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return false;
	}
}
