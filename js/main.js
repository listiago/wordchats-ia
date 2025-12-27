// ==================== Mobile Navigation ====================
const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');
const navClose = document.getElementById('nav-close');
const navLinks = document.querySelectorAll('.nav-link');

// Show menu
if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show');
    });
}

// Hide menu
if (navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show');
    });
}

// Hide menu when clicking nav link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('show');
    });
});

// ==================== Header Scroll Effect ====================
const header = document.getElementById('header');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.style.boxShadow = '0 4px 12px rgba(0,0,0,0.1)';
    } else {
        header.style.boxShadow = '0 2px 4px rgba(0,0,0,0.05)';
    }
});

// ==================== Smooth Scroll ====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        // Skip if href is just "#"
        if (href === '#') {
            e.preventDefault();
            return;
        }

        const target = document.querySelector(href);

        if (target) {
            e.preventDefault();

            const headerHeight = header.offsetHeight;
            const targetPosition = target.offsetTop - headerHeight;

            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ==================== FAQ Accordion ====================
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');

    question.addEventListener('click', () => {
        // Close other items
        faqItems.forEach(otherItem => {
            if (otherItem !== item) {
                otherItem.classList.remove('active');
            }
        });

        // Toggle current item
        item.classList.toggle('active');
    });
});

// ==================== Scroll Reveal Animation ====================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in-up');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe elements
const animateElements = document.querySelectorAll(
    '.feature-card-ai, .pricing-card, .faq-item, .stat-card'
);

animateElements.forEach(el => {
    observer.observe(el);
});

// ==================== Active Navigation Link ====================
const sections = document.querySelectorAll('section[id]');

function scrollActive() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 100;
        const sectionId = current.getAttribute('id');
        const navLink = document.querySelector(`.nav-link[href*="${sectionId}"]`);

        if (navLink) {
            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                navLink.style.color = 'var(--primary-color)';
            } else {
                navLink.style.color = 'var(--text-color)';
            }
        }
    });
}

window.addEventListener('scroll', scrollActive);

// ==================== Dynamic Year Update ====================
function updateCurrentYear() {
    const currentYearElement = document.getElementById('current-year');
    if (currentYearElement) {
        const currentYear = new Date().getFullYear();
        currentYearElement.textContent = currentYear;
    }
}

// ==================== Pricing Dynamic Controls ====================
let currentConnections = 1;

// Preços base dos planos (em reais)
const basePrices = {
    starter: 67,
    pro: 147,
    business: 297
};

// ⚠️ IMPORTANTE: Adicione os links dos seus planos aqui
// Array de 5 links por plano (1 conexão, 2 conexões, 3 conexões, 4 conexões, 5 conexões)
const planLinks = {
    starter: [
        '#',  // 1 conexão - SUBSTITUA pelo link real
        '#',  // 2 conexões - SUBSTITUA pelo link real
        '#',  // 3 conexões - SUBSTITUA pelo link real
        '#',  // 4 conexões - SUBSTITUA pelo link real
        '#'   // 5 conexões - SUBSTITUA pelo link real
    ],
    pro: [
        '#',  // 1 conexão - SUBSTITUA pelo link real
        '#',  // 2 conexões - SUBSTITUA pelo link real
        '#',  // 3 conexões - SUBSTITUA pelo link real
        '#',  // 4 conexões - SUBSTITUA pelo link real
        '#'   // 5 conexões - SUBSTITUA pelo link real
    ],
    business: [
        '#',  // 1 conexão - SUBSTITUA pelo link real
        '#',  // 2 conexões - SUBSTITUA pelo link real
        '#',  // 3 conexões - SUBSTITUA pelo link real
        '#',  // 4 conexões - SUBSTITUA pelo link real
        '#'   // 5 conexões - SUBSTITUA pelo link real
    ]
};

// Função para atualizar preços
function updatePrices() {
    Object.keys(basePrices).forEach(plan => {
        const basePrice = basePrices[plan];
        const extraConnections = Math.max(0, currentConnections - 1);
        const newPrice = basePrice + (extraConnections * 69);

        const priceElement = document.getElementById(`price-${plan}`);
        if (priceElement) {
            // Animar mudança de preço
            priceElement.style.transform = 'scale(1.2)';
            setTimeout(() => {
                priceElement.textContent = newPrice;
                priceElement.style.transform = 'scale(1)';
            }, 150);
        }
    });
}

// Função para atualizar textos dos números conectados
function updateConnectionTexts() {
    ['starter', 'pro', 'business'].forEach(plan => {
        const connectionTextElement = document.getElementById(`connection-text-${plan}`);
        if (connectionTextElement) {
            const plural = currentConnections > 1 ? 's' : '';
            const text = `${currentConnections} WhatsApp${plural} conectado${plural}`;
            connectionTextElement.textContent = text;
        }
    });
}

// Função para atualizar links dos botões
function updateLinks() {
    const pricingButtons = document.querySelectorAll('.pricing-btn');

    pricingButtons.forEach(btn => {
        const planType = btn.getAttribute('data-plan');

        if (planType && planLinks[planType]) {
            const link = planLinks[planType][currentConnections - 1] || '#';
            btn.setAttribute('href', link);

            // Se o link for "#", avisar ao usuário (dev mode)
            if (link === '#') {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    alert('Configure os links dos planos no arquivo js/main.js na seção "planLinks"');
                });
            }
        }
    });
}

// Função para atualizar contador
function updateCounter() {
    const counter = document.getElementById('connection-count');
    if (counter) {
        counter.textContent = currentConnections;
    }

    // Atualizar botões de controle
    const decreaseBtn = document.getElementById('decrease-connections');
    const increaseBtn = document.getElementById('increase-connections');

    if (decreaseBtn) {
        if (currentConnections <= 1) {
            decreaseBtn.setAttribute('disabled', 'disabled');
            decreaseBtn.style.opacity = '0.5';
            decreaseBtn.style.cursor = 'not-allowed';
        } else {
            decreaseBtn.removeAttribute('disabled');
            decreaseBtn.style.opacity = '1';
            decreaseBtn.style.cursor = 'pointer';
        }
    }

    if (increaseBtn) {
        if (currentConnections >= 5) {
            increaseBtn.setAttribute('disabled', 'disabled');
            increaseBtn.style.opacity = '0.5';
            increaseBtn.style.cursor = 'not-allowed';
        } else {
            increaseBtn.removeAttribute('disabled');
            increaseBtn.style.opacity = '1';
            increaseBtn.style.cursor = 'pointer';
        }
    }
}

// Função para atualizar tudo
function updateAll() {
    updateCounter();
    updatePrices();
    updateConnectionTexts();
    updateLinks();
}

// Eventos dos controles
document.addEventListener('DOMContentLoaded', () => {
    const decreaseBtn = document.getElementById('decrease-connections');
    const increaseBtn = document.getElementById('increase-connections');

    if (decreaseBtn) {
        decreaseBtn.addEventListener('click', () => {
            if (currentConnections > 1) {
                currentConnections--;
                updateAll();
            }
        });
    }

    if (increaseBtn) {
        increaseBtn.addEventListener('click', () => {
            if (currentConnections < 5) {
                currentConnections++;
                updateAll();
            }
        });
    }

    // Inicializar
    updateAll();
    updateCurrentYear();
});

// ==================== Loading Animation ====================
window.addEventListener('load', () => {
    document.body.classList.add('loaded');

    // Animar hero section
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        heroContent.classList.add('fade-in-up');
    }
});

// ==================== Prevent Default on Empty Links ====================
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href="#"]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
        });
    });
});

// ==================== Add Hover Effect to Cards ====================
const cards = document.querySelectorAll('.feature-card-ai, .pricing-card, .stat-card');

cards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transition = 'all 0.3s ease';
    });
});

// ==================== Performance Monitoring (Dev Mode) ====================
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    console.log('🚀 WordChats IA Landing Page Carregada!');
    console.log('ℹ️ Configure os links dos planos em js/main.js');
    console.log('📊 Planos configurados:', Object.keys(basePrices));
}

// ==================== Analytics Helper (Opcional) ====================
// Descomente e configure conforme necessário

/*
function trackPlanClick(planName, connections) {
    // Google Analytics 4
    if (typeof gtag !== 'undefined') {
        gtag('event', 'plan_click', {
            'plan_name': planName,
            'connections': connections,
            'price': basePrices[planName] + ((connections - 1) * 69)
        });
    }

    // Facebook Pixel
    if (typeof fbq !== 'undefined') {
        fbq('track', 'AddToCart', {
            content_name: planName,
            content_category: 'AI Plans',
            value: basePrices[planName] + ((connections - 1) * 69),
            currency: 'BRL'
        });
    }
}

// Adicionar tracking aos botões de planos
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.pricing-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const planName = btn.getAttribute('data-plan');
            if (planName) {
                trackPlanClick(planName, currentConnections);
            }
        });
    });
});
*/

// ==================== Console Easter Egg ====================
console.log(`
%c
 _       __               ________          __
| |     / /____  _________/ / ____/___ ___  / /______
| | /| / / __ \\/ ___/ __  / /   / __ \`/ / / / ___  /
| |/ |/ / /_/ / /  / /_/ / /___/ /_/ / /_/ (__  )
|__/|__/\\____/_/   \\__,_/\\____/\\__,_/\\__, /____/
                                      /____/
%cInteligência Artificial para WhatsApp 🤖
%c
Precisa de ajuda? WhatsApp: (81) 97337-8920
Site: https://wordchats.com.br
`,
'color: #8b5cf6; font-weight: bold;',
'color: #ec4899; font-size: 14px;',
'color: #6b7280; font-size: 12px;'
);
