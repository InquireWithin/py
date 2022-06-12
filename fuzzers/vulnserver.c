
//NOTICE: This file was not written by me. it is an older version of stephenbradshaw's vulnserver.c (https://github.com/stephenbradshaw/vulnserver/)

#define WIN32_LEAN_AND_MEAN

#include <windows.h>
#include <WinSock2.h>
#include <ws2tcpip.h>
#include <stdlib.h>
#include <stdio.h>

#define DEFAULT_BUFLEN 4096
#define DEFAULT_PORT "9999"

#pragma comment (lib, "Ws2_32.lib")

void cap_func(char* Input);
void pet_func(char* Input);
void sun_func(char* Input);
void zip_func(char* Input);
DWORD WINAPI ConnectionHandler(LPVOID CSocket);


int main(int argc, char* argv[]) {
	char PortNumber[6];

	strncpy(PortNumber, DEFAULT_PORT, 6);

	printf("Starting vulnserver version 2\n");
	
	WSADATA wsaData;
	SOCKET ListenSocket = INVALID_SOCKET,
		ClientSocket = INVALID_SOCKET;
	struct addrinfo* result = NULL, hints;
	int Result;
	struct sockaddr_in ClientAddress;
	int ClientAddressL = sizeof(ClientAddress);

	Result = WSAStartup(MAKEWORD(2, 2), &wsaData);
	if (Result != 0) {
		printf("WSAStartup failed with error: %d\n", Result);
		return 1;
	}

	ZeroMemory(&hints, sizeof(hints));
	hints.ai_family = AF_INET;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_protocol = IPPROTO_TCP;
	hints.ai_flags = AI_PASSIVE;

	Result = getaddrinfo(NULL, PortNumber, &hints, &result);
	if (Result != 0) {
		printf("Getaddrinfo failed with error: %d\n", Result);
		WSACleanup();
		return 1;
	}

	ListenSocket = socket(result->ai_family, result->ai_socktype, result->ai_protocol);
	if (ListenSocket == INVALID_SOCKET) {
		printf("Socket failed with error: %ld\n", WSAGetLastError());
		freeaddrinfo(result);
		WSACleanup();
		return 1;
	}

	Result = bind(ListenSocket, result->ai_addr, (int)result->ai_addrlen);
	if (Result == SOCKET_ERROR) {
		printf("Bind failed with error: %d\n", WSAGetLastError());
		closesocket(ListenSocket);
		WSACleanup();
		return 1;
	}

	freeaddrinfo(result);

	Result = listen(ListenSocket, SOMAXCONN);
	if (Result == SOCKET_ERROR) {
		printf("Listen failed with error: %d\n", WSAGetLastError());
		closesocket(ListenSocket);
		WSACleanup();
		return 1;
	}

	while (ListenSocket) {
		printf("Waiting for client connections...\n");

		ClientSocket = accept(ListenSocket, (SOCKADDR*)&ClientAddress, &ClientAddressL);
		if (ClientSocket == INVALID_SOCKET) {
			printf("Accept failed with error: %d\n", WSAGetLastError());
			closesocket(ListenSocket);
			WSACleanup();
			return 1;
		}

		printf("Received a client connection from %s:%u\n", inet_ntoa(ClientAddress.sin_addr), htons(ClientAddress.sin_port));
		CreateThread(0, 0, ConnectionHandler, (LPVOID)ClientSocket, 0, 0);

	}

	closesocket(ListenSocket);
	WSACleanup();

	return 0;
}


void sun_func(char* Input) {
	char Buffer[2000];
	strcpy_s(Buffer, Input, 2000);
}

void cap_func(char* Input) {
	char Buffer[1999];
	strcpy(Buffer, Input);
}

void pet_func(char* Input) {
	char Buffer[1521];
	strcpy(Buffer, Input);
}

void zip_func(char* Input) {
	char Buffer[1000];
	strncpy(Buffer, Input, 800);
}


DWORD WINAPI ConnectionHandler(LPVOID CSocket) {
	int RecvBufLen = DEFAULT_BUFLEN;
	char* RecvBuf = malloc(DEFAULT_BUFLEN);
	char BigEmpty[1000];
	char* ZipBuf = malloc(1024);
	int Result, SendResult, i, k;
	memset(BigEmpty, 0, 1000);
	memset(RecvBuf, 0, DEFAULT_BUFLEN);
	SOCKET Client = (SOCKET)CSocket;
	SendResult = send(Client, "Welcome to Vulnerable Server! Enter HELP for help.\n", 51, 0);
	if (SendResult == SOCKET_ERROR) {
		printf("Send failed with error: %d\n", WSAGetLastError());
		closesocket(Client);
		return 1;
	}
	while (CSocket) {
		Result = recv(Client, RecvBuf, RecvBufLen, 0);
		if (Result > 0) {
			
			if (strncmp(RecvBuf, "HELP", 4) == 0) {
				const char ValidCommands[251] = "Valid Commands:\nHELP\nSUN [sun_value]\nPET [pet_value]\nCAP [cap_value]\nZIP [zip_value]\nEXIT\n";
				SendResult = send(Client, ValidCommands, sizeof(ValidCommands), 0);
			}
			else if (strncmp(RecvBuf, "SUN ", 4) == 0) {
				char* SunBuf = malloc(3000);
				memset(SunBuf, 0, 3000);
				if ((char)RecvBuf[4] == '/') {
					strncpy(SunBuf, RecvBuf, 3000);
					sun_func(SunBuf);
				}

				memset(SunBuf, 0, 3000);
				SendResult = send(Client, "SUN COMPLETE\n", 14, 0);
			}
			else if (strncmp(RecvBuf, "CAP ", 4) == 0) {
				char* CapBuf = malloc(2000);
				memset(CapBuf, 0, 2000);
				if ((char)RecvBuf[4] == '*') {
					strncpy(CapBuf, RecvBuf, 2000);
					cap_func(CapBuf);
				}

				memset(CapBuf, 0, 2000);
				SendResult = send(Client, "CAP COMPLETE\n", 14, 0);
			}

			else if (strncmp(RecvBuf, "PET ", 4) == 0) {
				char* PetBuf = malloc(3000);
				memset(PetBuf, 0, 3000);
				if ((char)RecvBuf[4] == '%') {
					strncpy(PetBuf, RecvBuf, 3000);
					pet_func(PetBuf);
				}
				
				memset(PetBuf, 0, 3000);
				SendResult = send(Client, "PET COMPLETE\n", 14, 0);
			}
			
			else if (strncmp(RecvBuf, "ZIP ", 4) == 0) {
				char* ZipBuf = malloc(3000);
				memset(ZipBuf, 0, 3000);
				if ((char)RecvBuf[4] == '$') {
					strncpy(ZipBuf, RecvBuf, 3000);
					zip_func(ZipBuf);
				}

				memset(ZipBuf, 0, 3000);
				SendResult = send(Client, "ZIP COMPLETE\n", 14, 0);
			}
			
			else if (strncmp(RecvBuf, "EXIT", 4) == 0) {
				SendResult = send(Client, "GOODBYE\n", 8, 0);
				printf("Connection closing...\n");
				closesocket(Client);
				return 0;
			}
			else {
				SendResult = send(Client, "UNKNOWN COMMAND\n", 16, 0);
			}
			if (SendResult == SOCKET_ERROR) {
				printf("Send failed with error: %d\n", WSAGetLastError());
				closesocket(Client);
				return 1;
			}
		}
		else if (Result == 0) {
			printf("Connection closing...\n");
			closesocket(Client);
			return 0;
		}
		else {
			printf("Recv failed with error: %d\n", WSAGetLastError());
			closesocket(Client);
			return 1;
		}

	}
}

