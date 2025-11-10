from app import app, mail, Message

with app.app_context():
    msg = Message(
        subject='Tes Email dari Flask',
        recipients=['farelgoo32@gmail.com'],
        body='Halo! Ini hanya tes kirim email dari Flask.'
    )
    try:
        mail.send(msg)
        print("✅ Email berhasil dikirim!")
    except Exception as e:
        print(f"❌ Gagal kirim email: {e}")
