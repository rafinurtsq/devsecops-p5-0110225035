def get_db_connection():
    # Simulasi koneksi dengan kredensial hardcoded (vulnerability)
    db_user = "admin"
    db_password = "password123" 
    return f"Connected as {db_user}"