// ============================================
// XP — Terminal Homepage Scripts
// ============================================

document.addEventListener('DOMContentLoaded', () => {

  // --- Typing Animation (homepage only) ---
  const typingEl = document.getElementById('typing-name');
  const cursorEl = document.getElementById('cursor-name');
  const profileCmd = document.getElementById('profile-cmd');
  const profileOutput = document.getElementById('profile-output');
  const navCmd = document.getElementById('nav-cmd');
  const navOutput = document.getElementById('nav-output');
  const statusCmd = document.getElementById('status-cmd');
  const statusOutput = document.getElementById('status-output');

  if (typingEl) {
    const text = 'Xiaopeng Liu — Cloud DevSecOps Architect';
    let i = 0;

    function typeChar() {
      if (i < text.length) {
        typingEl.textContent += text.charAt(i);
        i++;
        setTimeout(typeChar, 20 + Math.random() * 15);
      } else {
        cursorEl.style.display = 'none';
        setTimeout(showProfile, 200);
      }
    }

    function fadeIn(el, next, delay) {
      if (!el) return;
      el.style.opacity = '1';
      el.style.transition = 'opacity 0.15s';
      if (next) setTimeout(next, delay || 150);
    }

    function showProfile() {
      fadeIn(profileCmd, () => {
        fadeIn(profileOutput, showNav, 250);
      });
    }

    function showNav() {
      fadeIn(navCmd, () => {
        fadeIn(navOutput, showStatus, 250);
      });
    }

    function showStatus() {
      fadeIn(statusCmd, () => {
        fadeIn(statusOutput);
      });
    }

    setTimeout(typeChar, 400);
  }

  // --- Nav scroll effect ---
  const nav = document.getElementById('nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 50);
    }, { passive: true });
  }

  // --- Mobile menu toggle ---
  const toggle = document.getElementById('nav-toggle');
  const mobileMenu = document.getElementById('mobile-menu');

  if (toggle && mobileMenu) {
    toggle.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
    });

    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
      });
    });
  }

  // --- Reveal on scroll (IntersectionObserver) ---
  const reveals = document.querySelectorAll('.reveal');

  if (reveals.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15,
      rootMargin: '0px 0px -50px 0px'
    });

    reveals.forEach(el => observer.observe(el));
  }

  // --- Skill bar animation (works on resume page too) ---
  const skillBars = document.querySelectorAll('.skill-fill');

  if (skillBars.length) {
    const skillObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const bars = entry.target.querySelectorAll('.skill-fill');
          bars.forEach((bar, index) => {
            const width = bar.getAttribute('data-width');
            setTimeout(() => {
              bar.style.width = width + '%';
            }, index * 50);
          });
          skillObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 });

    const skillsContainer = document.querySelector('.skills-grid');
    if (skillsContainer) {
      skillObserver.observe(skillsContainer);
    }
  }

  // --- Blog tag filter ---
  const tagBtns = document.querySelectorAll('.tag-btn');
  const postRows = document.querySelectorAll('.blog-post-row[data-tags]');

  if (tagBtns.length) {
    tagBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        tagBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const tag = btn.getAttribute('data-tag');

        postRows.forEach(row => {
          if (tag === 'all') {
            row.classList.remove('hidden');
          } else {
            const tags = row.getAttribute('data-tags').split(',');
            row.classList.toggle('hidden', !tags.includes(tag));
          }
        });
      });
    });
  }

  // --- Language switcher (post pages) ---
  const langBtns = document.querySelectorAll('.lang-btn');
  const langContents = document.querySelectorAll('.lang-content');

  if (langBtns.length) {
    langBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const lang = btn.getAttribute('data-lang');
        langBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        langContents.forEach(content => {
          content.classList.toggle('active', content.getAttribute('data-lang') === lang);
        });
      });
    });
  }

  // --- Active nav link highlight (homepage only) ---
  const sections = document.querySelectorAll('.section[id]');
  const navLinks = document.querySelectorAll('.nav-links a');

  if (sections.length && navLinks.length) {
    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        if (window.scrollY >= sectionTop) {
          current = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href && href.startsWith('#')) {
          link.style.color = '';
          if (href === '#' + current) {
            link.style.color = 'var(--green)';
          }
        }
      });
    }, { passive: true });
  }

});
