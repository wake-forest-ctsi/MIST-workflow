import os 
[os.rename(f, f.replace('.txt', '_txt.json')) for f in os.listdir('.') if not f.startswith('.')]
