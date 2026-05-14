const loginForm = document.getElementById("loginForm")
const childForm = document.getElementById("childForm")
const result = document.getElementById("result")

loginForm.addEventListener("submit", async (e) => {
    e.preventDefault()

    const formData = new FormData(loginForm)

    const res = await fetch("/login", {
        method: "POST",
        body: formData
    })

    const data = await res.json()

    result.innerHTML = data.message
})

childForm.addEventListener("submit", async (e) => {
    e.preventDefault()

    const formData = new FormData(childForm)

    const res = await fetch("/create_childbot", {
        method: "POST",
        body: formData
    })

    const data = await res.json()

    result.innerHTML = data.message
})
