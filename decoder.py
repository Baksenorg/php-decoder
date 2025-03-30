import subprocess
import os

def decode_php_file(encoded_file, output_file):
    # PHP komutunu çalıştır
    command = f'php {encoded_file}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Çıktıyı yaz
    with open(output_file, 'w') as file:
        file.write(result.stdout)

# Kullanım
encoded_file = 'encoded.php'
output_file = 'decoded.php'
decode_php_file(encoded_file, output_file)
