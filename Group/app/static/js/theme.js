/* Theme Manager - Dark/Light Mode Management */

class ThemeManager {
    constructor() {
        this.STORAGE_KEY = 'despite-theme-preference';
        this.DARK_MODE = 'dark';
        this.LIGHT_MODE = 'light';
        this.DEFAULT_MODE = 'light';
        this.init();
    }

    init() {
        this.loadTheme();
        this.setupToggle();
        this.observeSystemPreference();
    }

    loadTheme() {
        // Check localStorage first
        const savedTheme = localStorage.getItem(this.STORAGE_KEY);
        if (savedTheme) {
            this.setTheme(savedTheme);
            return;
        }

        // Check system preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            this.setTheme(this.DARK_MODE);
        } else {
            this.setTheme(this.LIGHT_MODE);
        }
    }

    setTheme(theme) {
        if (theme !== this.DARK_MODE && theme !== this.LIGHT_MODE) {
            theme = this.LIGHT_MODE;
        }

        // Set data attribute
        document.documentElement.setAttribute('data-theme', theme);

        // Save to localStorage
        localStorage.setItem(this.STORAGE_KEY, theme);

        // Update toggle button
        this.updateToggleButton(theme);

        // Dispatch event
        this.dispatchThemeChangeEvent(theme);
    }

    getCurrentTheme() {
        return document.documentElement.getAttribute('data-theme') || this.LIGHT_MODE;
    }

    toggleTheme() {
        const currentTheme = this.getCurrentTheme();
        const newTheme = currentTheme === this.DARK_MODE ? this.LIGHT_MODE : this.DARK_MODE;
        this.setTheme(newTheme);
    }

    setupToggle() {
        // Find or create toggle button
        let toggleBtn = document.querySelector('.theme-toggle');
        
        if (!toggleBtn) {
            toggleBtn = this.createToggleButton();
            document.body.appendChild(toggleBtn);
        }

        toggleBtn.addEventListener('click', () => this.toggleTheme());

        // Keyboard shortcut: Alt + T
        document.addEventListener('keydown', (e) => {
            if (e.altKey && e.key === 't') {
                e.preventDefault();
                this.toggleTheme();
            }
        });
    }

    createToggleButton() {
        const btn = document.createElement('button');
        btn.className = 'theme-toggle';
        btn.setAttribute('aria-label', 'Toggle dark/light mode');
        btn.setAttribute('title', 'Toggle theme (Alt+T)');
        btn.innerHTML = '🌙';
        return btn;
    }

    updateToggleButton(theme) {
        const toggleBtn = document.querySelector('.theme-toggle');
        if (toggleBtn) {
            toggleBtn.innerHTML = theme === this.DARK_MODE ? '☀️' : '🌙';
            toggleBtn.setAttribute('aria-label', 
                `Current theme: ${theme}. Click to switch to ${theme === this.DARK_MODE ? 'light' : 'dark'} mode`
            );
        }
    }

    observeSystemPreference() {
        if (window.matchMedia) {
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
                // Only auto-switch if no user preference saved
                if (!localStorage.getItem(this.STORAGE_KEY)) {
                    this.setTheme(e.matches ? this.DARK_MODE : this.LIGHT_MODE);
                }
            });
        }
    }

    dispatchThemeChangeEvent(theme) {
        const event = new CustomEvent('themechange', {
            detail: { theme: theme }
        });
        document.dispatchEvent(event);
    }
}

// Initialize theme manager when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.themeManager = new ThemeManager();
    });
} else {
    window.themeManager = new ThemeManager();
}

// Listen for theme changes if needed elsewhere
document.addEventListener('themechange', (e) => {
    console.log('Theme changed to:', e.detail.theme);
});
