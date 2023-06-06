from pyquery import PyQuery as pq

# HTML de ejemplo
html = '''
<html>
  <body>
    <h2>Título de ejemplo</h2>
    <p>Este es un párrafo de ejemplo.</p>
  </body>
</html>
'''

doc = pq(html)

# Seleccionar el texto del elemento h2
h2_text = doc('h2').text()

# Seleccionar el texto del elemento p
p_text = doc('p').text()

print('Texto del h2:', h2_text)
print('Texto del p:', p_text)

