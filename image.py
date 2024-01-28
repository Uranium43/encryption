from flask import Flask, render_template, request, send_file
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64

app = Flask(__name__)

def derive_key(password):
    salt = b'123456'  # Change this to a random value
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    password = request.form['password']
    key = derive_key(password)

    image = request.files['image']
    image_data = image.read()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(image_data)

    with open('encrypted_image.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    return send_file('encrypted_image.enc', as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    password = request.form['password']
    key = derive_key(password)

    encrypted_image = request.files['encrypted_image']
    encrypted_data = encrypted_image.read()
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open('decrypted_image.png', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return send_file('decrypted_image.png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
