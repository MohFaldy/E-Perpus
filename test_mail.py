import os
from dotenv import load_dotenv
from mailjet_rest import Client

# Muat variabel dari file .env
load_dotenv()

api_key = os.environ.get('MAILJET_API_KEY')
api_secret = os.environ.get('MAILJET_SECRET_KEY')

# PENTING: Ganti dengan email yang SUDAH ANDA VERIFIKASI di Mailjet
sender_email = os.environ.get('MAIL_SENDER_EMAIL') 

# PENTING: Ganti dengan alamat email pribadi Anda untuk menerima tes
recipient_email = "mohfaldi765@gmail.com" 

mailjet = Client(auth=(api_key, api_secret), version='v3.1')

data = {
  'Messages': [
    {
      "From": {"Email": sender_email, "Name": "Tes E-Perpus"},
      "To": [
        {"Email": recipient_email, "Name": "Penerima Tes"}
      ],
      "Subject": "Tes Kirim Email via Mailjet REST API",
      "TextPart": "Halo, jika Anda menerima ini, koneksi Mailjet berhasil!",
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())

print(f"\nSkrip selesai. Cek email di {recipient_email} (termasuk folder spam).")

