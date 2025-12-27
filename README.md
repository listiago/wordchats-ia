# WordChats IA - Landing Page de Planos de Inteligência Artificial

Landing page moderna e otimizada para SEO focada nos planos de IA do WordChats para WhatsApp.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Estrutura de Arquivos](#estrutura-de-arquivos)
- [Configuração Inicial](#configuração-inicial)
- [Planos e Preços](#planos-e-preços)
- [Personalização](#personalização)
- [SEO e Performance](#seo-e-performance)
- [Deploy](#deploy)
- [Manutenção](#manutenção)

---

## 🎯 Visão Geral

Esta landing page foi desenvolvida especificamente para promover os planos de **Inteligência Artificial** do WordChats, focando em:

- **Conversão**: Design otimizado para maximizar vendas
- **SEO**: Otimizada para Google e outras ferramentas de busca
- **Performance**: HTML/CSS/JS puro - ultra rápido
- **Mobile-First**: Responsivo em todos os dispositivos

### Planos Disponíveis

1. **Starter** - R$67/mês
   - IA inteligente básica
   - Respostas automáticas de texto
   - Ideal para pequenos negócios

2. **Pro** - R$147/mês ⭐ MAIS POPULAR
   - IA avançada
   - Responde áudios automaticamente
   - Follow-up e remarketing
   - Ideal para médias empresas

3. **Business** - R$297/mês
   - IA ultra avançada
   - Remarketing completo
   - Suporte prioritário
   - Ideal para grandes volumes

### Conexões Dinâmicas

Todos os planos incluem 1 WhatsApp. Clientes podem adicionar até 4 conexões extras:
- **Preço por conexão extra**: R$69/mês
- **Máximo**: 5 conexões por plano

---

## ✨ Funcionalidades

### Recursos da IA Destacados

1. ✅ Respostas automáticas inteligentes
2. ✅ Responde áudios automaticamente (Pro/Business)
3. ✅ Resgata clientes inativos - Follow-up
4. ✅ Transfere para humano quando necessário
5. ✅ Detecta quando cliente compra
6. ✅ Envia fotos/vídeos/documentos
7. ✅ Recupera clientes antigos - Remarketing (Business)
8. ✅ Digitação realista (parece humano)
9. ✅ Fluxos de atendimento automatizados

### Recursos Técnicos

- **Sistema de Preços Dinâmico**: Calcula automaticamente o preço baseado no número de conexões
- **Seção de Comparação**: Mostra vantagens sobre concorrentes
- **FAQ Interativo**: Responde dúvidas comuns
- **Animações Suaves**: Scroll reveal e hover effects
- **Schema.org Markup**: Otimizado para rich snippets do Google
- **WhatsApp Float Button**: Botão fixo para contato direto

---

## 📁 Estrutura de Arquivos

```
landing-ia/
├── index.html          # Página principal
├── css/
│   └── style.css       # Estilos completos
├── js/
│   └── main.js         # JavaScript interativo
├── images/             # Pasta para imagens (vazia - adicione suas imagens)
└── README.md           # Esta documentação
```

---

## ⚙️ Configuração Inicial

### 1. Adicionar Links dos Planos

**IMPORTANTE**: Antes de colocar no ar, configure os links de pagamento em `js/main.js`:

```javascript
const planLinks = {
    starter: [
        'https://pay.kiwify.com.br/LINK-1-CONEXAO',  // 1 conexão
        'https://pay.kiwify.com.br/LINK-2-CONEXOES', // 2 conexões
        'https://pay.kiwify.com.br/LINK-3-CONEXOES', // 3 conexões
        'https://pay.kiwify.com.br/LINK-4-CONEXOES', // 4 conexões
        'https://pay.kiwify.com.br/LINK-5-CONEXOES'  // 5 conexões
    ],
    pro: [
        'https://pay.kiwify.com.br/LINK-1-CONEXAO',
        'https://pay.kiwify.com.br/LINK-2-CONEXOES',
        'https://pay.kiwify.com.br/LINK-3-CONEXOES',
        'https://pay.kiwify.com.br/LINK-4-CONEXOES',
        'https://pay.kiwify.com.br/LINK-5-CONEXOES'
    ],
    business: [
        'https://pay.kiwify.com.br/LINK-1-CONEXAO',
        'https://pay.kiwify.com.br/LINK-2-CONEXOES',
        'https://pay.kiwify.com.br/LINK-3-CONEXOES',
        'https://pay.kiwify.com.br/LINK-4-CONEXOES',
        'https://pay.kiwify.com.br/LINK-5-CONEXOES'
    ]
};
```

### 2. Atualizar Informações de Contato

Em `index.html`, procure e atualize:

```html
<!-- WhatsApp Float Button (linha ~782) -->
<a href="https://wa.me/5581973378920" class="whatsapp-float">

<!-- CTA Section (linha ~765) -->
<a href="https://wa.me/5581973378920?text=Olá, quero saber mais sobre os planos de IA">
```

### 3. Adicionar Imagens (Opcional)

Cole suas imagens na pasta `images/` e atualize as referências no HTML.

Sugestões de imagens:
- Logo da empresa (header)
- Screenshots do sistema
- Fotos de depoimentos
- Ícones personalizados

---

## 💰 Planos e Preços

### Estrutura de Preços

| Plano      | Preço Base | + 1 Conexão | + 2 Conexões | + 3 Conexões | + 4 Conexões |
|------------|-----------|-------------|--------------|--------------|--------------|
| Starter    | R$ 67     | R$ 136      | R$ 205       | R$ 274       | R$ 343       |
| Pro        | R$ 147    | R$ 216      | R$ 285       | R$ 354       | R$ 423       |
| Business   | R$ 297    | R$ 366      | R$ 435       | R$ 504       | R$ 573       |

**Fórmula**: `Preço Final = Preço Base + (Conexões Extras × R$69)`

### Modificar Preços

Para alterar os preços base, edite em `js/main.js`:

```javascript
const basePrices = {
    starter: 67,    // ← Mude aqui
    pro: 147,       // ← Mude aqui
    business: 297   // ← Mude aqui
};
```

Para alterar o preço por conexão extra, edite:

```javascript
const newPrice = basePrice + (extraConnections * 69); // ← Mude o 69
```

E também atualize o texto no HTML (linha ~497):

```html
<p class="connection-info">
    <i class="fas fa-info-circle"></i>
    Cada conexão adicional: <strong>+R$ 69/mês</strong> <!-- Mude aqui -->
</p>
```

---

## 🎨 Personalização

### Cores e Tema

As cores são definidas em `css/style.css` usando CSS Variables:

```css
:root {
    --primary-color: #8b5cf6;      /* Roxo principal */
    --primary-dark: #7c3aed;       /* Roxo escuro */
    --primary-light: #a78bfa;      /* Roxo claro */
    --secondary-color: #ec4899;    /* Rosa */
    --accent-color: #10b981;       /* Verde (checks) */
}
```

Para mudar o tema:
1. Substitua os valores das variáveis acima
2. As cores serão aplicadas automaticamente em toda a página

### Textos e Conteúdo

Todos os textos estão em `index.html` e são facilmente editáveis:

- **Hero Section**: Linha 85-149
- **Funcionalidades IA**: Linha 152-340
- **Comparação**: Linha 343-438
- **Planos**: Linha 441-670
- **FAQ**: Linha 673-821

### Adicionar/Remover Funcionalidades

Para adicionar uma nova funcionalidade na seção "Features AI":

```html
<div class="feature-card-ai">
    <div class="feature-icon-ai">
        <i class="fas fa-ICONE-AQUI"></i>
    </div>
    <h3>Título da Funcionalidade</h3>
    <p>Descrição breve da funcionalidade.</p>
    <ul class="feature-list">
        <li><i class="fas fa-check"></i> Benefício 1</li>
        <li><i class="fas fa-check"></i> Benefício 2</li>
        <li><i class="fas fa-check"></i> Benefício 3</li>
    </ul>
</div>
```

---

## 🚀 SEO e Performance

### Meta Tags Configuradas

✅ Title otimizado (60 caracteres)
✅ Meta description (155 caracteres)
✅ Open Graph (Facebook/LinkedIn)
✅ Twitter Cards
✅ Canonical URL
✅ Schema.org markup (SoftwareApplication)
✅ Robots meta tag

### Otimizações de Performance

- ✅ HTML/CSS/JS puro (sem frameworks pesados)
- ✅ Lazy loading de imagens
- ✅ Animações com CSS (GPU-accelerated)
- ✅ Fontes carregadas via Google Fonts (preconnect)
- ✅ Minificação recomendada para produção

### Score Esperado

- **PageSpeed**: 90-100
- **SEO**: 100
- **Acessibilidade**: 95+
- **Best Practices**: 100

### Melhorar SEO

1. **Adicione Google Analytics**:
```html
<!-- Adicione antes do </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXX');
</script>
```

2. **Adicione Facebook Pixel**:
```html
<!-- Adicione antes do </head> -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'SEU-PIXEL-ID');
fbq('track', 'PageView');
</script>
```

3. **Configure sitemap.xml**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://wordchats.com.br/planos-ia</loc>
    <lastmod>2025-01-27</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

---

## 🌐 Deploy

### Opção 1: Hospedagem Tradicional (cPanel, Hostinger, etc)

1. Faça upload de todos os arquivos via FTP
2. Aponte o domínio para a pasta
3. Configure SSL (HTTPS)
4. Teste em: `https://seudominio.com.br/planos-ia`

### Opção 2: Vercel (Recomendado - Grátis)

```bash
# Instale Vercel CLI
npm i -g vercel

# Entre na pasta do projeto
cd landing-ia

# Deploy
vercel

# Siga as instruções e pronto!
```

### Opção 3: Netlify (Grátis)

1. Acesse [netlify.com](https://netlify.com)
2. Arraste a pasta `landing-ia` para o site
3. Configure domínio personalizado
4. Pronto!

### Opção 4: GitHub Pages (Grátis)

1. Crie repositório no GitHub
2. Faça upload dos arquivos
3. Ative GitHub Pages nas configurações
4. Acesse via: `https://seuusuario.github.io/landing-ia`

---

## 🔧 Manutenção

### Atualizar Preços

1. Edite `js/main.js` → `basePrices`
2. Atualiz o HTML se necessário
3. Teste localmente
4. Faça deploy

### Adicionar Novo Plano

1. **HTML** (`index.html`):
```html
<div class="pricing-card">
    <div class="pricing-header">
        <div class="plan-icon">
            <i class="fas fa-star"></i>
        </div>
        <h3 class="plan-name">Novo Plano</h3>
        <p class="plan-subtitle">Descrição do plano</p>
        <div class="pricing-price">
            <span class="currency">R$</span>
            <span class="amount" id="price-novo">XXX</span>
            <span class="period">/mês</span>
        </div>
    </div>
    <!-- Features -->
    <a href="#" class="btn btn-primary btn-block pricing-btn" data-plan="novo">
        Assinar Novo Plano
    </a>
</div>
```

2. **JavaScript** (`js/main.js`):
```javascript
const basePrices = {
    starter: 67,
    pro: 147,
    business: 297,
    novo: 397  // ← Adicione aqui
};

const planLinks = {
    // ... planos existentes
    novo: ['#', '#', '#', '#', '#']  // ← Adicione aqui
};
```

3. **CSS**: Já está pronto, não precisa mexer!

### Testar Antes de Publicar

```bash
# Abra o arquivo diretamente no navegador
start index.html  # Windows
open index.html   # Mac
xdg-open index.html  # Linux

# Ou use um servidor local:
python -m http.server 8000
# Acesse: http://localhost:8000
```

---

## 📊 Análise de Mercado (Pesquisa Realizada)

### Concorrentes - Brasil (2025)

**Plataformas Nacionais:**
- Globalbot: Não divulga preços públicos
- SleekFlow: R$230-R$1.150/mês
- Média do mercado: R$147-R$347/mês

**Plataformas Internacionais:**
- WATI: $49-$98/mês (~R$280-R$560)
- Interakt: $49-$119/mês (~R$280-R$680)
- Respond.io: $199+/mês (~R$1.140+)

### Posicionamento WordChats IA

✅ **VANTAGEM COMPETITIVA**: Preços 40-60% mais acessíveis
✅ **Funcionalidades exclusivas**: Responde áudios, remarketing, follow-up
✅ **Target ideal**: Pequenas e médias empresas brasileiras

---

## 📞 Suporte

### Dúvidas ou Problemas?

- **WhatsApp**: (81) 97337-8920
- **Site**: https://wordchats.com.br
- **Instagram**: @wordchatss
- **YouTube**: @wordchats

---

## 📝 Checklist de Lançamento

Antes de colocar no ar, certifique-se:

- [ ] Configurou os links de pagamento em `js/main.js`
- [ ] Atualizou informações de contato (WhatsApp, redes sociais)
- [ ] Adicionou Google Analytics e Facebook Pixel
- [ ] Testou em diferentes dispositivos (mobile, tablet, desktop)
- [ ] Testou todos os botões de compra
- [ ] Configurou SSL (HTTPS)
- [ ] Testou velocidade da página (PageSpeed Insights)
- [ ] Verificou SEO (Google Search Console)
- [ ] Criou backup dos arquivos

---

## 🎨 Paleta de Cores

```
Roxo Principal: #8b5cf6
Roxo Escuro:    #7c3aed
Roxo Claro:     #a78bfa
Rosa:           #ec4899
Verde (Sucesso):#10b981
Cinza Texto:    #1f2937
Cinza Claro:    #6b7280
```

---

## 🚀 Próximos Passos Recomendados

1. **Criar variações de teste A/B**
   - Testar diferentes CTAs
   - Testar diferentes preços
   - Testar diferentes ordens de planos

2. **Adicionar depoimentos reais**
   - Fotos de clientes
   - Resultados específicos
   - Vídeos de cases de sucesso

3. **Integrar com CRM**
   - Capturar leads que não converteram
   - Remarketing automático
   - Nurturing de leads

4. **Criar blog de conteúdo**
   - Artigos sobre IA e WhatsApp
   - Tutoriais e guias
   - SEO de cauda longa

---

## 📄 Licença

© 2025 WordChats. Todos os direitos reservados.

Esta landing page foi desenvolvida exclusivamente para WordChats.

---

**Desenvolvido com ❤️ para WordChats**

*Última atualização: 27 de Janeiro de 2025*
