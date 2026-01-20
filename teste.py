import sys
print("Python:", sys.executable)

import pkg_resources
try:
    version = pkg_resources.get_distribution("Pillow").version
    print(f"Pillow versão: {version}")
    print("✅ Tudo OK!")
except:
    print("❌ Pillow não encontrado")
