# -*- coding: utf-8 -*-
import codecs

pricing_section = """
    <!-- Pricing Section -->
    <section class="pricing" id="planos">
        <div class="container">
            <div class="section-header">
                <span class="section-subtitle">
                    <i class="fas fa-tags"></i> Planos e Preços
                </span>
                <h2 class="section-title">
                    Escolha Seu <span class="gradient-text">Plano de IA</span>
                </h2>
                <p class="section-description">
                    Todos os planos incluem 1 WhatsApp. Adicione até 4 conexões extras por apenas R$ 69/mês cada
                </p>
            </div>

            <div class="connection-selector">
                <div class="connection-header">
                    <i class="fas fa-plug"></i>
                    <span>Quantas conexões de WhatsApp você precisa?</span>
                </div>
                <div class="connection-options">
                    <button class="connection-btn active" data-connections="1">
                        <i class="fab fa-whatsapp"></i>
                        <span>1 WhatsApp</span>
                    </button>
                    <button class="connection-btn" data-connections="2">
                        <i class="fab fa-whatsapp"></i>
                        <span>2 WhatsApp</span>
                    </button>
                    <button class="connection-btn" data-connections="3">
                        <i class="fab fa-whatsapp"></i>
                        <span>3 WhatsApp</span>
                    </button>
                    <button class="connection-btn" data-connections="4">
                        <i class="fab fa-whatsapp"></i>
                        <span>4 WhatsApp</span>
                    </button>
                    <button class="connection-btn" data-connections="5">
                        <i class="fab fa-whatsapp"></i>
                        <span>5 WhatsApp</span>
                    </button>
                </div>
                <p class="connection-info">
                    <i class="fas fa-info-circle"></i>
                    Cada conexão adicional: <strong>+R$ 69/mês</strong>
                </p>
            </div>

            <div class="pricing-grid">
                <div class="pricing-card">
                    <div class="pricing-header">
                        <div class="plan-icon">
                            <i class="fas fa-rocket"></i>
                        </div>
                        <h3 class="plan-name">Starter</h3>
                        <p class="plan-subtitle">Para pequenos negócios</p>
                        <div class="pricing-price">
                            <span class="currency">R$</span>
                            <span class="amount" id="price-starter">67</span>
                            <span class="period">/mês</span>
                        </div>
                    </div>
                    <div class="pricing-features">
                        <h4>Recursos de IA:</h4>
                        <ul>
                            <li><i class="fas fa-check"></i> IA Inteligente Básica</li>
                            <li><i class="fas fa-check"></i> Respostas automáticas de texto</li>
                            <li><i class="fas fa-check"></i> Transfere para humano</li>
                            <li><i class="fas fa-check"></i> Detecta quando cliente compra</li>
                        </ul>
                        <h4>Outros recursos:</h4>
                        <ul>
                            <li><i class="fas fa-check"></i> Atendimento 24/7</li>
                            <li><i class="fas fa-check"></i> Fluxos automatizados</li>
                            <li><i class="fas fa-check"></i> Relatórios básicos</li>
                        </ul>
                    </div>
                    <a href="#" class="btn btn-primary btn-block pricing-btn" data-plan="starter">
                        <i class="fas fa-shopping-cart"></i> Assinar Starter
                    </a>
                </div>

                <div class="pricing-card popular">
                    <div class="pricing-badge">Mais Popular</div>
                    <div class="pricing-header">
                        <div class="plan-icon">
                            <i class="fas fa-star"></i>
                        </div>
                        <h3 class="plan-name">Pro</h3>
                        <p class="plan-subtitle">Para médias empresas</p>
                        <div class="pricing-price">
                            <span class="currency">R$</span>
                            <span class="amount" id="price-pro">147</span>
                            <span class="period">/mês</span>
                        </div>
                    </div>
                    <div class="pricing-features">
                        <h4>Tudo do Starter, mais:</h4>
                        <ul>
                            <li><i class="fas fa-check"></i> <strong>IA Avançada</strong></li>
                            <li><i class="fas fa-check"></i> <strong>Responde Áudios Automaticamente</strong></li>
                            <li><i class="fas fa-check"></i> <strong>Follow-up Automático</strong></li>
                            <li><i class="fas fa-check"></i> Envia fotos/vídeos/documentos</li>
                            <li><i class="fas fa-check"></i> Digitação realista</li>
                            <li><i class="fas fa-check"></i> Relatórios avançados</li>
                        </ul>
                    </div>
                    <a href="#" class="btn btn-primary btn-block pricing-btn" data-plan="pro">
                        <i class="fas fa-shopping-cart"></i> Assinar Pro
                    </a>
                </div>

                <div class="pricing-card">
                    <div class="pricing-header">
                        <div class="plan-icon">
                            <i class="fas fa-crown"></i>
                        </div>
                        <h3 class="plan-name">Business</h3>
                        <p class="plan-subtitle">Para grandes volumes</p>
                        <div class="pricing-price">
                            <span class="currency">R$</span>
                            <span class="amount" id="price-business">297</span>
                            <span class="period">/mês</span>
                        </div>
                    </div>
                    <div class="pricing-features">
                        <h4>Tudo do Pro, mais:</h4>
                        <ul>
                            <li><i class="fas fa-check"></i> <strong>IA Ultra Avançada</strong></li>
                            <li><i class="fas fa-check"></i> <strong>Remarketing Completo</strong></li>
                            <li><i class="fas fa-check"></i> Recupera clientes antigos</li>
                            <li><i class="fas fa-check"></i> Suporte prioritário</li>
                            <li><i class="fas fa-check"></i> API completa</li>
                            <li><i class="fas fa-check"></i> Webhooks avançados</li>
                        </ul>
                    </div>
                    <a href="#" class="btn btn-primary btn-block pricing-btn" data-plan="business">
                        <i class="fas fa-shopping-cart"></i> Assinar Business
                    </a>
                </div>
            </div>

            <div class="pricing-guarantee">
                <i class="fas fa-shield-check"></i>
                <div>
                    <h4>Garantia de 7 Dias</h4>
                    <p>Teste sem risco. Se não gostar, devolvemos 100% do seu dinheiro</p>
                </div>
            </div>
        </div>
    </section>

"""

faq_section = """
    <!-- FAQ Section -->
    <section class="faq" id="faq">
        <div class="container">
            <div class="section-header">
                <span class="section-subtitle">
                    <i class="fas fa-question-circle"></i> Perguntas Frequentes
                </span>
                <h2 class="section-title">
                    Dúvidas <span class="gradient-text">Comuns</span>
                </h2>
                <p class="section-description">
                    Tudo o que você precisa saber sobre nossos planos de IA
                </p>
            </div>
            <div class="faq-grid">
                <div class="faq-item">
                    <button class="faq-question">
                        <span>Como a IA responde áudios?</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="faq-answer">
                        <p>Nossa IA usa tecnologia de ponta (Whisper da OpenAI) para transcrever automaticamente os áudios que seus clientes enviam. Depois, ela entende o contexto e responde de forma inteligente e personalizada, como se fosse um atendente humano.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>O que é Follow-up Automático?</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="faq-answer">
                        <p>O Follow-up automático identifica quando um cliente parou de responder no meio de uma conversa. A IA envia mensagens personalizadas para resgatar esse cliente e retomar a negociação, aumentando suas chances de venda.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Como funciona o Remarketing?</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="faq-answer">
                        <p>O Remarketing recupera clientes antigos que não compram há meses. A IA envia mensagens estratégicas para reconquistar esses clientes inativos, oferecendo promoções e novidades relevantes.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Preciso de conhecimento técnico?</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="faq-answer">
                        <p>Não! Nossa plataforma foi desenvolvida para ser extremamente simples. Em menos de 10 minutos você conecta seu WhatsApp, configura a IA e já está vendendo no automático.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Posso usar em quantos WhatsApp?</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="faq-answer">
                        <p>Todos os planos incluem 1 conexão de WhatsApp. Você pode adicionar até 4 conexões extras por apenas R$ 69/mês cada, totalizando até 5 WhatsApp por conta.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>A garantia é mesmo de verdade?</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="faq-answer">
                        <p>Sim! Você tem 7 dias para testar sem risco. Se por qualquer motivo não gostar, basta solicitar e devolvemos 100% do seu investimento. Sem perguntas, sem burocracias.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Qual a diferença entre os níveis de IA?</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="faq-answer">
                        <p><strong>IA Básica (Starter):</strong> Responde textos com inteligência.<br>
                        <strong>IA Avançada (Pro):</strong> Responde textos e áudios, com follow-up.<br>
                        <strong>IA Ultra (Business):</strong> Tudo do Pro + remarketing completo e suporte prioritário.</p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-question">
                        <span>Posso mudar de plano depois?</span>
                        <i class="fas fa-chevron-down"></i>
                    </button>
                    <div class="faq-answer">
                        <p>Sim! Você pode fazer upgrade ou downgrade a qualquer momento. O valor é ajustado proporcionalmente ao período já pago.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

"""

cta_section = """
    <!-- CTA Section -->
    <section class="cta" id="cta">
        <div class="container">
            <div class="cta-content">
                <h2>Pronto Para Automatizar Suas Vendas com IA?</h2>
                <p>Configuração completa em menos de 10 minutos</p>
                <div class="cta-buttons">
                    <a href="#planos" class="btn btn-white btn-lg">
                        <i class="fas fa-rocket"></i> Ver Planos e Começar
                    </a>
                </div>
                <div class="cta-trust">
                    <div class="trust-badge-cta">
                        <i class="fas fa-shield-check"></i>
                        <span>Garantia de 7 dias</span>
                    </div>
                    <div class="trust-badge-cta">
                        <i class="fas fa-infinity"></i>
                        <span>Uso ilimitado</span>
                    </div>
                    <div class="trust-badge-cta">
                        <i class="fas fa-clock"></i>
                        <span>Atendimento 24/7</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

"""

footer_section = """
    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <img src="logo.png" alt="WordChats IA" class="footer-logo">
                    <p>Automatize vendas com Inteligência Artificial no WhatsApp</p>
                </div>
                <div class="footer-links">
                    <h4>Links Rápidos</h4>
                    <ul>
                        <li><a href="#home">Home</a></li>
                        <li><a href="#funcionalidades">Funcionalidades</a></li>
                        <li><a href="#planos">Planos</a></li>
                        <li><a href="#faq">FAQ</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Contato</h4>
                    <ul>
                        <li><i class="fab fa-whatsapp"></i> (81) 97343-1176</li>
                        <li><i class="fas fa-globe"></i> wordchats.com.br</li>
                        <li><i class="fab fa-instagram"></i> @wordchatss</li>
                        <li><i class="fab fa-youtube"></i> @wordchats</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 WordChats. Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>

    <!-- WhatsApp Float Button -->
    <a href="https://wa.me/5581973431176?text=Olá,%20quero%20saber%20mais%20sobre%20os%20planos%20de%20IA"
       class="whatsapp-float"
       target="_blank"
       rel="noopener noreferrer">
        <i class="fab fa-whatsapp"></i>
    </a>

    <script src="js/main.js"></script>
</body>
</html>
"""

# Append all sections
with codecs.open('index_complete.html', 'a', encoding='utf-8') as f:
    f.write(pricing_section)
    f.write(faq_section)
    f.write(cta_section)
    f.write(footer_section)

print("All sections added successfully!")
