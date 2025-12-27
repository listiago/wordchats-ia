# -*- coding: utf-8 -*-

# Read the current HTML
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Comparison section - Change class names to match CSS
content = content.replace('<div class="comparison-wordchats">', '<div class="comparison-col">')
content = content.replace('<div class="comparison-competitor">', '<div class="comparison-col">')
content = content.replace('<div class="comparison-header">', '<div class="comparison-header">')

# Fix 2: Testimonials section - Change to testimonial-card-modern
content = content.replace('<div class="testimonial-card featured">', '<div class="testimonial-card-modern featured-testimonial">')
content = content.replace('<div class="testimonial-card">', '<div class="testimonial-card-modern">')
content = content.replace('<div class="testimonial-badge">Destaque</div>', '<div class="testimonial-highlight-badge"><i class="fas fa-star"></i> Destaque</div>')
content = content.replace('<div class="testimonial-stars">', '<div class="testimonial-rating">')
content = content.replace('<div class="testimonial-author">', '<div class="testimonial-author-modern">')
content = content.replace('<div class="author-info">', '<div class="testimonial-author-info">')
content = content.replace('<div class="testimonial-result">', '<div class="testimonial-results">')

# Fix 3: Pricing section - Change to .popular instead of .popular badge position
content = content.replace('<div class="pricing-card popular">', '<div class="pricing-card featured">')

# Save the fixed HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML fixed successfully!")
print("Changed:")
print("- Comparison section classes")
print("- Testimonial section classes")
print("- Pricing card classes")
print("")
print("NOTA: O seletor de conexões foi manualmente alterado de botões 1-5")
print("para o sistema +/- para corresponder ao estilo da landing original.")
