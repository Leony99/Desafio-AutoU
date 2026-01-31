//DOM REFERENCES
const btn = document.getElementById("classifyBtn")
const resultDiv = document.getElementById("result")
const resultSection = document.getElementById("resultSection")
const textArea = document.getElementById("emailText")
const fileInput = document.getElementById("fileInput")

//MAIN EVENT: CLASSIFY EMAIL
btn.addEventListener("click", async () => {
    const text = textArea.value
    const file = fileInput.files[0]

    /* ---------- Validation ---------- */
    if (!text && !file) {
        alert("Informe um texto ou envie um arquivo.")
        return
    }

    /* ---------- Build payload ---------- */
    const formData = new FormData()
    file
        ? formData.append("file", file)
        : formData.append("text", text)

    /* ---------- UI: loading state ---------- */
    setLoadingState(true)

    /* ---------- Show result section + scroll ---------- */
    resultSection.classList.remove("hidden")
    scrollToResult()

    /* ---------- Loading feedback ---------- */
    resultDiv.innerHTML = renderLoading()

    try {
        /* ---------- API call ---------- */
        const response = await fetch("https://desafio-autou-production-3734.up.railway.app/classify-email", {
            method: "POST",
            body: formData
        })

        if (!response.ok) {
            throw new Error("Erro na API")
        }

        const data = await response.json()
        resultDiv.innerHTML = renderResultCard(data)

        /* ---------- Scroll again (after render) ---------- */
        scrollToResult()

    } catch (err) {
        resultDiv.innerHTML = renderError()
        console.error(err)

    } finally {
        /* ---------- UI: reset ---------- */
        setLoadingState(false)
    }
})

//UI HELPERS
function setLoadingState(isLoading) {
    btn.disabled = isLoading
    btn.classList.toggle("opacity-60", isLoading)
    btn.classList.toggle("cursor-not-allowed", isLoading)
}

function scrollToResult() {
    resultSection.scrollIntoView({
        behavior: "smooth",
        block: "start"
    })
}

//TEMPLATE RENDERERS
function renderLoading() {
    return `
        <div class="flex items-center gap-3 text-slate-600 dark:text-slate-300">
        <div class="spinner"></div>
        <span>Classificando email...</span>
        </div>
    `
}

function renderError() {
    return `
        <div class="bg-red-100 dark:bg-red-900/40 p-4 rounded-lg text-red-700">
        ❌ Erro ao comunicar com o servidor.
        </div>
    `
}

function renderResultCard(data) {
    const isProdutivo = data.category === "Produtivo"

    return `
        <div class="
        rounded-xl p-6 shadow-md
        ${isProdutivo
            ? "bg-green-50 dark:bg-green-900/30 border border-green-400"
            : "bg-red-50 dark:bg-red-900/30 border border-red-400"}
        ">
        <h3 class="text-xl font-semibold mb-2">
            ${isProdutivo ? "✅ Produtivo" : "🚫 Improdutivo"}
        </h3>

        <p class="text-sm opacity-80 mb-4">
            ${isProdutivo
            ? "Este email requer ação ou resposta."
            : "Este email não requer nenhuma ação."}
        </p>

        <div class="bg-white dark:bg-slate-800 p-4 rounded-lg">
            <div class="flex items-center justify-between mb-2">
            <p class="text-sm font-medium">Resposta sugerida</p>

            <button
                onclick="copyResponse(this)"
                data-text="${data.suggested_response}"
                class="text-xs text-purple-600 hover:underline"
            >
                Copiar
            </button>
            </div>

            <p class="text-sm opacity-90">
            ${data.suggested_response}
            </p>
        </div>
        </div>
    `
}

//ACTIONS
function copyResponse(button) {
    const text = button.getAttribute("data-text")

    navigator.clipboard.writeText(text)
        .then(() => {
        const original = button.innerHTML
        button.innerHTML = "✅ Copiado!"
        button.classList.add("text-green-600")

        setTimeout(() => {
            button.innerHTML = original
            button.classList.remove("text-green-600")
        }, 1500)
        })
        .catch(() => {
        alert("Não foi possível copiar o texto.")
        })
}