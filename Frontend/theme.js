function toggleTheme() {
    document.documentElement.classList.toggle('dark')

    const isDark = document.documentElement.classList.contains('dark')
    localStorage.setItem('theme', isDark ? 'dark' : 'light')
}

(function initTheme() {
    const saved = localStorage.getItem('theme')
    if (saved === 'dark') {
        document.documentElement.classList.add('dark')
    }
})();
