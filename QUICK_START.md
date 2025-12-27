# 🚀 Guia Rápido - WordChats IA Landing Page

## ✅ Começar em 5 Minutos

### Passo 1: Abra o arquivo no navegador

```bash
# Clique duas vezes em:
index.html
```

Ou navegue para a pasta e abra `index.html` no seu navegador favorito.

---

### Passo 2: Configure os Links de Pagamento ⚠️ IMPORTANTE

Abra o arquivo `js/main.js` e procure por `planLinks` (linha ~172):

```javascript
const planLinks = {
    starter: [
        '#',  // ← Cole aqui o link do Kiwify para 1 conexão
        '#',  // ← Cole aqui o link do Kiwify para 2 conexões
        '#',  // ← Cole aqui o link do Kiwify para 3 conexões
        '#',  // ← Cole aqui o link do Kiwify para 4 conexões
        '#'   // ← Cole aqui o link do Kiwify para 5 conexões
    ],
    pro: [
        // Repita para o plano Pro
    ],
    business: [
        // Repita para o plano Business
    ]
};
```

**Exemplo Real:**
```javascript
const planLinks = {
    starter: [
        'https://pay.kiwify.com.br/ABC123',  // 1 conexão - R$67
        'https://pay.kiwify.com.br/DEF456',  // 2 conexões - R$136
        'https://pay.kiwify.com.br/GHI789',  // 3 conexões - R$205
        'https://pay.kiwify.com.br/JKL012',  // 4 conexões - R$274
        'https://pay.kiwify.com.br/MNO345'   // 5 conexões - R$343
    ],
    // ... e assim por diante
};
```

---

### Passo 3: Atualize Informações de Contato

Em `index.html`, procure e substitua:

1. **WhatsApp** (aparece 3 vezes):
   - Linha ~782: Botão flutuante
   - Linha ~765: CTA section
   - Busque por: `5581973378920`

2. **Redes Sociais** (rodapé):
   - Instagram: `https://instagram.com/wordchatss`
   - YouTube: `https://www.youtube.com/@wordchats`

---

### Passo 4: (Opcional) Personalizar Cores

Abra `css/style.css` e encontre as variáveis (linha ~2):

```css
:root {
    --primary-color: #8b5cf6;    /* Mude para sua cor principal */
    --secondary-color: #ec4899;  /* Mude para sua cor secundária */
    --accent-color: #10b981;     /* Mude para cor de destaque */
}
```

---

### Passo 5: Testar Localmente

1. Abra `index.html` no navegador
2. Teste os botões de + e - nas conexões
3. Verifique se os preços mudam corretamente
4. Teste o menu mobile (redimensione a janela)
5. Clique nos links de planos (vão abrir os links do Kiwify)

---

### Passo 6: Fazer Deploy

**Opção Mais Fácil: Netlify (Grátis)**

1. Acesse [netlify.com](https://app.netlify.com/drop)
2. Arraste a pasta `landing-ia` para a página
3. Aguarde o upload (30 segundos)
4. Receba um link: `https://seu-site.netlify.app`
5. Configure domínio personalizado (opcional)

**Opção Alternativa: Vercel (Grátis)**

```bash
npm install -g vercel
cd landing-ia
vercel
```

---

## 📊 Tabela de Preços Configurados

| Plano      | 1 Conexão | 2 Conexões | 3 Conexões | 4 Conexões | 5 Conexões |
|------------|-----------|------------|------------|------------|------------|
| **Starter**  | R$ 67     | R$ 136     | R$ 205     | R$ 274     | R$ 343     |
| **Pro**      | R$ 147    | R$ 216     | R$ 285     | R$ 354     | R$ 423     |
| **Business** | R$ 297    | R$ 366     | R$ 435     | R$ 504     | R$ 573     |

**Fórmula**: Preço Base + (Conexões Extras × R$69)

---

## 🎯 Como Criar Links no Kiwify

Para cada plano, você precisa criar 5 produtos no Kiwify:

### Exemplo: Plano Starter

1. **Starter 1 Conexão** → R$67/mês → Gera link 1
2. **Starter 2 Conexões** → R$136/mês → Gera link 2
3. **Starter 3 Conexões** → R$205/mês → Gera link 3
4. **Starter 4 Conexões** → R$274/mês → Gera link 4
5. **Starter 5 Conexões** → R$343/mês → Gera link 5

Repita para Pro e Business.

**Total de produtos**: 15 (3 planos × 5 variações)

---

## ⚠️ Checklist Antes de Publicar

- [ ] Configurei todos os 15 links de pagamento
- [ ] Atualizei número de WhatsApp
- [ ] Testei no Chrome/Firefox/Safari
- [ ] Testei no celular (modo responsivo)
- [ ] Verifiquei que preços mudam ao clicar +/-
- [ ] Todos os links abrem corretamente
- [ ] SSL/HTTPS está ativo no deploy

---

## 💡 Dicas de Conversão

1. **Anúncios**: Direcione para a seção #planos
   ```
   https://seusite.com/#planos
   ```

2. **WhatsApp Marketing**: Use este texto
   ```
   🤖 Conheça nossos planos de IA para WhatsApp!

   A partir de R$67/mês você automatiza vendas 24/7

   👉 https://seusite.com
   ```

3. **Stories Instagram**: Crie card com:
   - "Automatize vendas com IA"
   - "A partir de R$67/mês"
   - Link: https://seusite.com

---

## 🆘 Problemas Comuns

### Os preços não mudam ao clicar +/-

**Solução**: Verifique se configurou o `planLinks` em `js/main.js`

### Links não funcionam

**Solução**: Substitua todos os `'#'` pelos links reais do Kiwify

### Página não abre

**Solução**: Certifique-se que abriu o arquivo `index.html`, não outro arquivo

### Botão de WhatsApp não funciona

**Solução**: Troque `5581973378920` pelo seu número (com DDI)

---

## 📞 Precisa de Ajuda?

WhatsApp: **(81) 97337-8920**

---

**Boa sorte com as vendas! 🚀**
