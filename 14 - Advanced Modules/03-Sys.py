# stderr ve stdout

"""
Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman çıktı vermek ve girdi almak için şu dosyaları kullanır.

stdin : Bu standard dosya, işlemimizin (process ) kullanıcıdan input almasını sağlar.

stdout : Bu standard dosya, işlemimizin (process ) çıktı vermesini sağlar.

stderr : Bu standard dosya, işlemimizin hata mesajlarını çıktı olarak vermek için kullanılır.
"""

import sys

sys.stderr.write("Burası bir hata mesajı\n")

sys.stderr.flush() # Buffer'ı hemen yaz. 

sys.stdout.write("Burası normal çıktımız\n")