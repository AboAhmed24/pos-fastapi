# POS FastAPI Printer Server

## SSL Setup with mkcert

This guide explains how to set up SSL certificates for local development using mkcert.

### Prerequisites

Install mkcert dependencies:
```bash
sudo apt update && sudo apt install -y libnss3-tools
```

### Step 1: Install mkcert

Download and install mkcert:
```bash
wget https://github.com/FiloSottile/mkcert/releases/download/v1.4.4/mkcert-v1.4.4-linux-amd64
sudo mv mkcert-v1.4.4-linux-amd64 /usr/local/bin/mkcert
sudo chmod +x /usr/local/bin/mkcert
```

### Step 2: Install Local Certificate Authority

Install the local CA in your system's trust store:
```bash
mkcert -install
```

This adds mkcert's root CA to your system's trusted certificates.

### Step 3: Generate SSL Certificates

Generate certificates for localhost and your printer server IP:
```bash
# Replace 192.168.1.39 with your actual printer server IP
mkcert localhost 127.0.0.1 192.168.1.39
```

This creates:
- `localhost+3.pem` (SSL certificate)
- `localhost+3-key.pem` (private key)

### Step 4: Rename Certificate Files

Rename the generated files to match the application expectations:
```bash
mv localhost+3.pem cert.pem
mv localhost+3-key.pem key.pem
```

### Step 5: Copy Certificates to Installation Folder

Copy the certificates to your application directory:
```bash
# Assuming your app is installed in /opt/pos-printer
sudo mkdir -p /opt/pos-printer/certs
sudo cp cert.pem /opt/pos-printer/certs/
sudo cp key.pem /opt/pos-printer/certs/
sudo cp ~/.local/share/mkcert/rootCA.pem /opt/pos-printer/certs/
```

### Step 6: Import Root CA to Browsers

For browsers to trust your local certificates, import the root CA:

#### Firefox
1. Open Firefox and go to `about:preferences#privacy`
2. Scroll down to "Certificates" and click "View Certificates"
3. Go to the "Authorities" tab
4. Click "Import..."
5. Navigate to `~/.local/share/mkcert/rootCA.pem`
6. Check "Trust this CA to identify websites"
7. Click OK and restart Firefox

#### Chrome/Chromium
1. Open Chrome and go to `chrome://settings/certificates`
2. Go to the "Authorities" tab
3. Click "Import..."
4. Navigate to `~/.local/share/mkcert/rootCA.pem`
5. Check "Trust this certificate for identifying websites"
6. Click OK and restart Chrome

### SSL Certificate Information

- **Certificate Validity**: ~2.25 years for server certificates, 10 years for CA
- **Valid Domains/IPs**: localhost, 127.0.0.1, and your specified printer IP
- **Security**: Full SSL encryption with trusted local certificates

### Troubleshooting

**Certificate not trusted in browser:**
- Ensure you've imported the root CA as described above
- Restart your browser after importing

**Connection refused:**
- Verify your printer server IP is correct in the certificate
- Check that the server is running on the correct port

**Certificate expired:**
- Regenerate certificates: `mkcert localhost 127.0.0.1 YOUR_IP`
- Replace the old cert.pem and key.pem files

### Alternative: Production SSL

For production deployments, use Let's Encrypt certificates:
```bash
sudo apt install certbot
sudo certbot certonly --standalone -d yourdomain.com
```

## Installation

## Usage

## API Documentation