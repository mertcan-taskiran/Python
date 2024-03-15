# Decorator fonksiyonu tanımlayalım
def log_kaydi(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} fonksiyonu çalışıyor...")
        return func(*args, **kwargs)
    return wrapper

# Decorator fonksiyonunu kullanarak fonksiyonları dekore edelim
@log_kaydi
def toplama(a, b):
    return a + b

@log_kaydi
def carpma(a, b):
    return a * b

# Dekore edilmiş fonksiyonu çağıralım
print(toplama(3, 5))
print(carpma(3, 5))