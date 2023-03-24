# 0x0B. SSH

Secure Shell (SSH) is a cryptographic network protocol that provides secure encrypted communication between two untrusted hosts over an insecure network. SSH is widely used for remote server administration, file transfers, and tunneling network services. In this article, we will discuss SSH essentials, including working with SSH servers, clients, and keys.

## SSH Servers

An SSH server is a software application that runs on a remote computer and allows secure, encrypted connections over the network. The most popular SSH server implementation is OpenSSH, which is available for many operating systems, including Linux, macOS, and Windows.

To set up an SSH server, you need to install the OpenSSH package on your remote computer and configure it to allow SSH connections. By default, OpenSSH listens on port 22, but you can change this to any other port.

Once you have set up the SSH server, you can use an SSH client to connect to it and access its resources.

## SSH Clients

An SSH client is a software application that runs on your local computer and allows you to connect to an SSH server securely. The most popular SSH client implementations are OpenSSH (which is also used as an SSH server) and PuTTY (Windows only).

To connect to an SSH server, you need to know its IP address or hostname and have valid login credentials (username and password or SSH key).

To connect to an SSH server using OpenSSH, you can use the following command in a terminal:
```
ssh username@hostname
```

This will prompt you for your password (if using password authentication) or use your SSH key to authenticate automatically.

If you are using PuTTY, you need to enter the server's IP address or hostname, select the SSH protocol, and enter your login credentials in the appropriate fields.

## SSH Keys
SSH keys are a secure way of authenticating to an SSH server without using a password. An SSH key consists of a public key and a private key. The public key is stored on the SSH server, while the private key is stored on your local computer.

To generate an SSH key pair using OpenSSH, you can use the following command:
```
ssh-keygen -t rsa -b 4096
```
This will generate a 4096-bit RSA key pair and store the private key in ~/.ssh/id_rsa and the public key in ~/.ssh/id_rsa.pub.

You can then copy the public key to the SSH server using the following command:
```
ssh-copy-id username@hostname
```
This will prompt you for your password (if using password authentication) and copy the public key to the remote server's authorized_keys file, allowing you to authenticate without a password.

To use an SSH key with PuTTY, you need to convert the OpenSSH key format to the PuTTY key format using the PuTTYgen tool.

In conclusion, SSH is a secure and widely used protocol for remote server administration and file transfers. By setting up an SSH server and using an SSH client with SSH keys, you can securely access your remote resources without exposing your passwords to the network. 
